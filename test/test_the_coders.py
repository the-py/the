import unittest
from helper import world, the, safe


class TestTheCoders(unittest.TestCase):
    def setUp(self):
        self.eq = self.assertEqual
        self.neq = self.assertNotEqual

    # ---- coders keyworld ----

    # true
    @safe
    def test_true_is_true(self):
        the(True).true
        self.eq(len(world.errors), 1)
        self.eq(world.errors[0][1], None)

    @safe
    def test_anything_else_is_not_true(self):
        the(False).true
        self.eq(len(world.errors), 1)
        self.neq(world.errors[0][1], None)

    # false
    @safe
    def test_false_is_false(self):
        the(False).false
        self.eq(len(world.errors), 1)
        self.eq(world.errors[0][1], None)

    @safe
    def test_anythin_else_is_not_false(self):
        the(True).false
        self.eq(len(world.errors), 1)
        self.neq(world.errors[0][1], None)

    # Not
    @safe
    def test_not(self):
        the(True).Not.false
        self.eq(len(world.errors), 1)
        self.eq(world.errors[0][1], None)

    # none
    @safe
    def test_none_is_none(self):
        the(None).none
        self.eq(len(world.errors), 1)
        self.eq(world.errors[0][1], None)

    @safe
    def test_anything_else_is_not_none(self):
        the(1).none
        self.eq(len(world.errors), 1)
        self.neq(world.errors[0][1], None)

    # exist
    @safe
    def test_anthing_not_none_is_exist(self):
        the(1).exist
        self.eq(len(world.errors), 1)
        self.eq(world.errors[0][1], None)

    @safe
    def test_none_is_not_exist(self):
        the(None).exist
        self.eq(len(world.errors), 1)
        self.neq(world.errors[0][1], None)

    @safe
    def test_ok(self):
        the(1).ok
        self.eq(len(world.errors), 1)
        self.eq(world.errors[0][1], None)

    @safe
    def test_not_ok(self):
        the([]).ok
        self.eq(len(world.errors), 1)
        self.neq(world.errors[0][1], None)

    @safe
    def test_empty(self):
        the([]).empty
        self.eq(len(world.errors), 1)
        self.eq(world.errors[0][1], None)

    @safe
    def test_not_empty(self):
        the(1).empty
        self.eq(len(world.errors), 1)
        self.neq(world.errors[0][1], None)

if __name__ == '__main__':
    unittest.main()

