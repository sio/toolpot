"""
Tests for toolpot.python.adapters
"""

import unittest


from toolpot.python.adapters import CompositionAdapter
class testCompositionAdapter(unittest.TestCase):
    def setUp(self):
        class Inner(object):
            def __init__(self):
                self.hello = "Hello world"
        class Outer(CompositionAdapter):
            @classmethod
            def _constructor(cls):
                return Inner()
        self.instance = Outer()

    def test_inner_object_method(self):
        self.assertEqual(self.instance.hello.upper(), "HELLO WORLD")

    def test_non_existing_method(self):
        with self.assertRaises(AttributeError):
            self.instance.nonexistent_attribute

    def test_creating_attr_on_outer_object(self):
        t = self.instance
        t.world = True
        self.assertTrue("world" in t.__dict__)
        self.assertTrue("world" not in t._object.__dict__)

    def test_setattr_on_inner_object(self):
        t = self.instance
        setattr(t._object, "newattr", [])
        t.newattr = [1,2,3]
        self.assertIs(t.newattr, t._object.newattr)
        self.assertEqual(t.newattr[0], 1)
