import unittest

class AssertUtil:
    @staticmethod
    def verify_true(condition, message=""):
        assert condition, message

    @staticmethod
    def verify_equals(actual, expected, message=""):
        assert actual == expected, message