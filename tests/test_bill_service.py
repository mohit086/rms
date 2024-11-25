import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import MagicMock
from services.bill_service import BillService

class TestBillService(unittest.TestCase):
    def setUp(self):
        # Create a mock database connection
        self.db_mock = MagicMock()
        self.bill_service = BillService(self.db_mock)

    def test_generate_bill(self):
        # Simulate generating a bill
        self.db_mock.connection.cursor.return_value.lastrowid = 1
        bill_id = self.bill_service.generate_bill(1, 50.00)
        self.assertEqual(bill_id, 1)

    def test_get_bill_details(self):
        # Simulate fetching bill details
        self.db_mock.connection.cursor.return_value.fetchone.return_value = {'bill_id': 1, 'order_id': 1, 'total_amount': 50.00, 'payment_status': 'unpaid'}
        bill = self.bill_service.get_bill_details(1)
        self.assertEqual(bill['bill_id'], 1)
        self.assertEqual(bill['total_amount'], 50.00)

    def test_mark_bill_as_paid(self):
        # Simulate marking a bill as paid
        self.db_mock.connection.cursor.return_value.execute.return_value = None
        self.bill_service.mark_bill_as_paid(1)
        self.db_mock.connection.cursor.return_value.execute.assert_called_once_with(
            "UPDATE bills SET payment_status = 'paid' WHERE bill_id = %s;", (1,)
        )

if __name__ == '__main__':
    unittest.main()
