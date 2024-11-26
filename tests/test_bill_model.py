import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from models.bill import Bill

class TestBillModel(unittest.TestCase):

    def test_bill_creation(self):
        # Test that a bill can be created
        bill = Bill(1, 1, 50.00, '2024-11-25')
        self.assertEqual(bill.bill_id, 1)
        self.assertEqual(bill.order_id, 1)
        self.assertEqual(bill.total_amount, 50.00)
        self.assertEqual(bill.payment_status, 'unpaid')

    def test_mark_bill_as_paid(self):
        # Test that a bill can be marked as paid
        bill = Bill(1, 1, 50.00, '2024-11-25')
        bill.mark_as_paid()
        self.assertEqual(bill.payment_status, 'paid')

    def test_bill_to_dict(self):
        # Test that a bill can be converted to a dictionary
        bill = Bill(1, 1, 50.00, '2024-11-25')
        bill_dict = bill.to_dict()
        self.assertEqual(bill_dict['bill_id'], 1)
        self.assertEqual(bill_dict['payment_status'], 'unpaid')

if __name__ == '__main__':
    unittest.main()
