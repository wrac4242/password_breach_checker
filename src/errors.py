'''error classes'''
# pylint: disable=unnecessary-pass

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ArgsTooSmallError(Error):
    """Raised when the arg length is too small"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

class ValueNotInt(Error):
    """Raised when the input value is too large"""
    pass
