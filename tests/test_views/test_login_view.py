import unittest
import tkinter as tk
from app import LoginView

class TestLoginView(unittest.TestCase):
    def test_login_view_loads(self):
        root = tk.Tk()
        def dummy_callback():
            pass
        view = LoginView(root, on_success_callback=dummy_callback)
        self.assertIsNotNone(view)
        root.destroy()

if __name__ == '__main__':
    unittest.main()
