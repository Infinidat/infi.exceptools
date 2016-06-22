__import__("pkg_resources").declare_namespace(__name__)

import sys


PY2 = sys.version_info[0] == 2
if PY2:
    from .py2 import *
else:
    from .py3 import *


__all__ = [ 'InfiException', 'extract_stack', 'extract_tb', 'format_exception', 'format_exception_only', 'format_list',
            'format_stack', 'format_tb', 'print_exc', 'format_exc', 'print_exception', 'print_last', 'print_stack',
            'print_tb', 'exceptools_decorator', 'exceptools_context']

__doc__ = """Exception utils and traceback replacement module.

This module provides chained exception mechanism (Python 3 style) with formatting and printing facilities like Python's
built-in traceback module.

Except for adding a new method called chain(), this module provides all the methods that exist in traceback and is
interface and output compatible.

Also, there's a new class called InfiException that can be used as a base exception class for all Infinidat code base.

>>> try:
>>>     1 / 0
>>> except:
>>>     raise chain(MyException("This is a wrapper exception that wraps another exception"))
"""

class InfiException(Exception):
    pass


extract_stack = traceback.extract_stack
extract_tb = traceback.extract_tb
format_exception_only = traceback.format_exception_only
format_list = traceback.format_list
format_stack = traceback.format_stack
format_tb = traceback.format_tb
print_stack = traceback.print_stack
print_tb = traceback.print_tb



if __name__ == '__main__':
    print("An example of a chained exception printing:\n")
    try:
        try:
            1 / 0
        except:
            raise chain(InfiException("wrapper exception"))
    except:
        print_exc()

    print("\nAn example of a chained exception printing without the chain:\n")
    try:
        try:
            1 / 0
        except:
            raise chain(InfiException("wrapper exception"))
    except:
        print_exc(chain=False)

