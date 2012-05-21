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

This project uses buildout, and git to generate setup.py and __version__.py.
In order to generate these, run:

    python -S bootstrap.py -d -t
    bin/buildout -c buildout-version.cfg
    python setup.py develop

In our development environment, we use isolated python builds, by running the following instead of the last command:

    bin/buildout install development-scripts

