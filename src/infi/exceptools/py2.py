import sys
import mock
from StringIO import StringIO
from infi.pyutils.contexts import contextmanager
from infi.pyutils.contexts import wraps
from traceback import print_tb, format_exception_only
import traceback


# Implementation borrows heavily from Python 3.2's traceback module, except that we do an array-based optimized
# format_xxx implementation.
def _print(file, str='', terminator='\n'):
    file.write(str+terminator)


def print_last(limit=None, file=None, chain=True):
    print_exception(sys.last_type, sys.last_value, sys.last_traceback, limit, file, chain)


def _iter_chain(value, tb):
    out = []
    if hasattr(value, '__cause__'):
        cause = getattr(value, '__cause__')
        if cause is not None:
            out += _iter_chain(cause, None)
            out.append(("\nThe above exception was the direct cause of the following exception:\n", None))
    if tb is None and hasattr(value, '__traceback__'):
        tb = value.__traceback__
    out.append((value, tb))
    return out


def _print_formatted_tb(file, tb, limit):
    for i in xrange(0, (limit or len(tb)) - 1):
        _print(file, tb[i])
    _print(file, "  " + tb[-1].strip())


def print_exception(etype, value, tb, limit=None, file=None, chain=True):
    if file is None:
        file = sys.stderr
    if chain:
        values = _iter_chain(value, tb)
    else:
        values = [ (value, tb) ]

    for value, tb in values:
        if isinstance(value, str):
            _print(file, value)
            continue
        if tb:
            _print(file, 'Traceback (most recent call last):')
            if isinstance(tb, list):
                _print_formatted_tb(file, tb, limit)
            else:
                print_tb(tb, limit, file)
        lines = format_exception_only(type(value), value)
        for line in lines:
            _print(file, line, '')


def print_exc(limit=None, file=None, chain=True):
    try:
        etype, value, tb = sys.exc_info()
        print_exception(etype, value, tb, limit, file, chain)
    finally:
        etype = value = tb = None


def format_exc(limit=None, chain=True):
    try:
        etype, value, tb = sys.exc_info()
        return format_exception(etype, value, tb, limit, chain)
    finally:
        etype = value = tb = None


def format_exception(etype, value, tb, limit=None, chain=True):
    buf = StringIO()
    print_exception(etype, value, tb, limit, buf, chain)
    res = buf.getvalue()
    buf.close()
    return res


def chain(new_exception):
    try:
        etype, value, tb = sys.exc_info()

        # First, if the current exception is really an exception (and not something bizarre such as a string), we want
        # to keep the traceback on it. Note that we don't keep the raw traceback object, we just keep the formatted one.
        if isinstance(value, BaseException) and not hasattr(value, '__traceback__'):
            setattr(value, '__traceback__', traceback.format_tb(tb))

        setattr(new_exception, '__cause__', value)
        return new_exception
    finally:
        etype = value = tb = None


@contextmanager
def exceptools_context():
    with mock.patch("traceback.format_exception") as patched_format_exception, mock.patch("traceback.print_exception") as patched_print_exception, mock.patch("traceback.format_exception") as patched_format_exception:
        patched_format_exception.side_effect = format_exception
        patched_print_exception.side_effect = print_exception
        yield


def exceptools_decorator(func):
    @wraps(func)
    def callee(*args, **kwargs):
        with exceptools_context():
            return func(*args, **kwargs)
    return callee
