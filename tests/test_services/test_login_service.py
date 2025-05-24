
import unittest
from app.services.login_service import authenticate_user

class TestLoginService(unittest.TestCase):
    def test_valid_login(self):
        result = authenticate_user("alihassan", "1234")
        self.assertIsNotNone(result)

    def test_invalid_login(self):
        result = authenticate_user("invalid", "wrong")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
