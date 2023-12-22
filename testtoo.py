import unittest

from src.Tool import Tool


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tool = Tool()
        sum = tool.sub(1, 2)
        print(sum)
        self.assertEqual(tool.sub(1, 2), 3)

    def testcomp(self):
        comp = Tool()
        self.assertTrue(comp.cmopar(2, 3))

    def testcomp2(self):
        comp = Tool()
        self.assertTrue(comp.cmopar(2, 3))
