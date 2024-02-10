import unittest
from Unittest import shoppinglist

# 单元测试类
class TestShoppinglist(unittest.TestCase):
    def setUp(self):
        self.shoppinglist1_test = shoppinglist({'apple': 2, 'banana': 3, 'orange': 5})

    def test_get_item_count(self):
        self.assertEqual(self.shoppinglist1_test.get_item_count(), 3)
        print("Test case 1 passed\n")


    def test_get_total_price(self):
        self.assertEqual(self.shoppinglist1_test.get_total_price(), 110)
        print("\nTest case 2 passed\n")

# if __name__ == '__main__':
#     unittest.main()

