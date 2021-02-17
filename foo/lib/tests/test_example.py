# coding: utf-8

import pytest


def setup_module(module):
    pass


class TestExample:

    @classmethod
    def setup_class(cls):
        pass

    def setup_method(self):
        pass

    def test_foo(self):
        i = 1
        assert i == 1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0
