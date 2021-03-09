import platform
import shutil
from pathlib import Path

from invoke import call, task
from invoke.context import Context
from invoke.runners import Result

ROOT = Path(__file__).parent


def _run(c: Context, command: str, *args: str) -> Result:
    return c.run(f"{command} {' '.join(args)}", pty=platform.system() != "Windows")


@task
def clean_build(c):
    """Clean up build"""
    shutil.rmtree(ROOT / "dist", ignore_errors=True)


@task
def clean_docs(c):
    """Clean up files from documentation builds"""
    shutil.rmtree(ROOT / "site", ignore_errors=True)


@task
def clean_python(c):
    """Clean up python file artifacts"""
    _run(c, f"pyclean {ROOT / 'MODULE_NAME'} {ROOT / 'tests'}")


@task
def clean_tests(c):
    """Clean up files from testing"""
    shutil.rmtree(ROOT / ".pytest_cache", ignore_errors=True)


@task
def clean_type_checking(c):
    """Clean up files from type-checking"""
    shutil.rmtree(ROOT / ".mypy_cache", ignore_errors=True)


@task(pre=[clean_build, clean_docs, clean_python, clean_tests, clean_type_checking])
def clean(c):
    """Run all clean sub-tasks"""


@task(name="format", help={"check": "Checks if source is formatted without applying changes"})
def format_(c, check=False):
    """Format code"""
    autoflake_args = ["-r", "--remove-all-unused-imports"]
    isort_args = []
    black_args = ["--quiet"]

    if check:
        isort_args += ["--check-only", "--diff"]
        black_args += ["--diff", "--check"]
    else:
        autoflake_args += ["-i"]

    _run(c, f"autoflake {ROOT}", *autoflake_args)
    _run(c, f"isort {ROOT}", *isort_args)
    _run(c, f"black {ROOT}", *black_args)


@task
def type_check(c):
    """Run type-checking"""
    _run(c, f"mypy {ROOT} --ignore-missing-imports")


@task(pre=[call(format_, check=True), type_check])
def lint(c):
    """Run all linting"""
    flake8_args = ["--max-line-length 119", "--extend-ignore E203,W503", "--exclude .venv"]
    _run(c, f"flake8 {ROOT}", *flake8_args)


@task
def test(c):
    """Run tests"""
    _run(c, "pytest")


@task(
    pre=[clean_docs], help={"serve": "Build the docs and watch for changes", "deploy": "Deploy docs to GitHub pages"}
)
def docs(c, serve=False, deploy=False):
    """Build documentation"""
    _run(c, "portray as_html")
    if deploy:
        _run(c, "ghp-import site -pf")
    if serve:
        _run(c, "portray server")


@task
def tag(c):
    """Create GitHub tag"""
    version = _run(c, "poetry version -s").stdout.rstrip()

    _run(c, f"git tag v{version}")
    _run(c, f"git push origin v{version}")


@task
def publish(c):
    """Publish to PyPI"""
    _run(c, "poetry publish --build")
