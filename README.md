Overview
========
This module features exception chaining.

Usage
-----

Here's an example on how to use this module:

```python
In [1]: from infi.exceptools import chain

In [2]: def example():
   ...:     try:
   ...:         raise RuntimeError()
   ...:     except:
   ...:         raise chain(Exception())
   ...:     

In [3]: try:
   ...:     example()
   ...: except Exception, exc:
   ...:     pass
   ...: 

In [4]: exc.__class__
Out[4]: Exception

In [5]: exc.__cause__.__class__
Out[5]: RuntimeError
```

Checking out the code
=====================

This project uses buildout and infi-projector, and git to generate setup.py and __version__.py.
In order to generate these, first get infi-projector:

    easy_install infi.projector

    and then run in the project directory:

        projector devenv build
