import unittest
from app.services.customer_service import add_customer, get_customers

class TestCustomerService(unittest.TestCase):
    def test_add_customer(self):
        add_customer("Test User", "123456789", "test@example.com")
        customers = get_customers()
        self.assertTrue(any(c[1] == "Test User" for c in customers))

if __name__ == '__main__':
    unittest.main()
