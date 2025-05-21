# === tkinter_app/app/tests/test_views/test_dashboard_view.py ===

import unittest
from app import Dashboard

class TestDashboardView(unittest.TestCase):
    def setUp(self):
        self.root = Dashboard()
        self.root.update()  # Ensure the Tkinter main loop initializes elements

    def tearDown(self):
        self.root.destroy()

    def test_dashboard_title_and_size(self):
        self.assertEqual(self.root.title(), "Inventory & Sales Management System")
        self.assertEqual(self.root.winfo_geometry(), "1100x650+0+0")

    def test_sidebar_buttons_exist(self):
        expected_buttons = [
            "Product Management",
            "Stock In/Out",
            "Sales Invoice",
            "Customers",
            "Suppliers",
            "Reports"
        ]
        actual_buttons = [btn[0] for btn in self.root.sidebar_buttons]
        self.assertEqual(actual_buttons, expected_buttons)

    def test_default_view_is_product_view(self):
        # Checks if current frame is ProductView
        current_frame_class = self.root.current_frame.__class__.__name__
        self.assertEqual(current_frame_class, "ProductView")

    def test_switch_to_stock_view(self):
        self.root.load_stock_view()
        self.root.update()
        current_frame_class = self.root.current_frame.__class__.__name__
        self.assertEqual(current_frame_class, "StockView")

    def test_switch_to_sales_view(self):
        self.root.load_sales_view()
        self.root.update()
        self.assertEqual(self.root.current_frame.__class__.__name__, "SalesView")

if __name__ == '__main__':
    unittest.main()
