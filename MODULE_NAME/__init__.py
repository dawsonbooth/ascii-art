"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

```python
foo = ClassFoo()
bar = foo.FunctionBar()
```
"""


def repeat_string(s: str, n: int) -> str:
    """Repeat a string an integer number of times!"""

    return s * n


__all__ = ["repeat_string"]
