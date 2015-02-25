import traceback
from contextlib import contextmanager


@contextmanager
def exceptools_context():
    yield


def exceptools_decorator(func):
    return func


def chain(new_exception):
    return new_exception


def print_exc(limit=None, file=None, chain=True):
    return traceback.print_exc(limit, file)


def print_exception(etype, value, tb, limit=None, file=None, chain=True):
    return traceback.print_exception(etype, value, tb, limit, file)


def format_exc(limit=None, chain=True):
    return traceback.format_exc(limit)


def format_exception(etype, value, tb, limit=None, chain=True):
    return traceback.format_exception(etype, value, tb, limit)
