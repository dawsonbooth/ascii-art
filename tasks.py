import os
import platform
import shutil
from pathlib import Path

from invoke import call, task
from invoke.context import Context
from invoke.runners import Result

ROOT = Path(__file__).parent


def _run(c: Context, command: str) -> Result:
    if platform.system() == "Windows":
        return _run(c, command)
    return _run(c, command, pty=True)


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
    _run(c, f"pyclean {ROOT}")


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
    isort_options = ["--check-only", "--diff"] if check else []
    _run(c, f"isort {ROOT / 'MODULE_NAME'} {' '.join(isort_options)}")
    black_options = ["--diff", "--check"] if check else ["--quiet"]
    _run(c, f"black {ROOT / 'MODULE_NAME'} {' '.join(black_options)}")


@task
def type_check(c):
    """Run type-checking"""
    _run(c, f"mypy {ROOT / 'MODULE_NAME'} --ignore-missing-imports")


@task(pre=[call(format_, check=True), type_check])
def lint(c):
    """Run all linting"""
    _run(c, f"flake8 {ROOT / 'MODULE_NAME'} --max-line-length 119 --extend-ignore E203,W503")


@task
def test(c):
    """Run tests"""
    _run(c, f"pytest {ROOT / 'MODULE_NAME' / 'test'}")


@task(help={"serve": "Build the docs and watch for changes", "deploy": "Deploy docs to GitHub pages"})
def docs(c, serve=False, deploy=False):
    """Build documentation"""
    os.makedirs(ROOT / "docs", exist_ok=True)
    _run(c, f"pydoc-markdown -p {ROOT / 'MODULE_NAME'} > {ROOT / 'docs' / 'api.md'}")
    shutil.copy(ROOT / "README.md", ROOT / "docs")
    _run(c, "mkdocs build --clean")
    if deploy:
        _run(c, "mkdocs gh-deploy")
    if serve:
        _run(c, "mkdocs serve")


@task
def tag(c):
    """Create GitHub tag"""
    version = _run(c, "poetry version -s").stdout.rstrip()

    _run(c, f'git commit -m "v{version}"')
    _run(c, f"git tag v{version}")
    _run(c, f"git push origin v{version}")


@task
def publish(c):
    """Publish to PyPI"""
    _run(c, "poetry publish --build")
