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

Run the following:

    easy_install -U infi.projector
    projector devenv build
