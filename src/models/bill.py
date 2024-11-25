class Bill:
    def __init__(self, bill_id, order_id, total_amount, billing_date, payment_status='unpaid'):
        self.bill_id = bill_id
        self.order_id = order_id
        self.total_amount = total_amount
        self.billing_date = billing_date
        self.payment_status = payment_status

    def mark_as_paid(self):
        """Mark the bill as paid."""
        self.payment_status = 'paid'

    def to_dict(self):
        """Return a dictionary representation of the bill."""
        return {
            'bill_id': self.bill_id,
            'order_id': self.order_id,
            'total_amount': self.total_amount,
            'billing_date': self.billing_date,
            'payment_status': self.payment_status
        }
