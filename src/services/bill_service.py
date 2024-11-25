from data_access.queries import *

class BillService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def generate_bill(self, order_id, total_amount):
        """Generate a bill for an order."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(CREATE_BILL, (order_id, total_amount))
        self.db_connection.connection.commit()
        bill_id = cursor.lastrowid
        cursor.close()
        return bill_id

    def get_bill_details(self, bill_id):
        """Retrieve bill details."""
        cursor = self.db_connection.connection.cursor(dictionary=True)
        cursor.execute(GET_BILL_BY_ID, (bill_id,))
        bill = cursor.fetchone()
        cursor.close()
        return bill

    def mark_bill_as_paid(self, bill_id):
        """Mark a bill as paid."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(UPDATE_BILL_STATUS, (bill_id,))
        self.db_connection.connection.commit()
        cursor.close()