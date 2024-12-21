import frappe
from frappe.utils import flt

def execute(filters=None):
    # Define columns
    columns = [
        {"fieldname": "customer", "label": "Customer", "fieldtype": "Data", "width": 200},
        {"fieldname": "delivery_date", "label": "Delivery Date", "fieldtype": "Date", "width": 150},
        {"fieldname": "sales_order", "label": "Sales Order", "fieldtype": "Link", "options": "Sales Order", "width": 200},
        {"fieldname": "delivery_status", "label": "Delivery Status", "fieldtype": "Data", "width": 150},
    ]

    # Fetch data based on filters
    conditions = []
    if filters.get("customer"):
        conditions.append("customer = %(customer)s")
    if filters.get("delivery_date"):
        conditions.append("delivery_date = %(delivery_date)s")

    condition_str = " AND ".join(conditions)
    if condition_str:
        condition_str = "WHERE " + condition_str + " AND delivery_status IN ('Scheduled', 'Dispatched')"
    else:
        condition_str = "WHERE delivery_status IN ('Scheduled', 'Dispatched')"

    data = frappe.db.sql(
        f"""
        SELECT
            customer, delivery_date, sales_order, delivery_status
        FROM
            `tabDelivery Schedule`
        {condition_str}
        ORDER BY delivery_date ASC
        """,
        filters,
        as_dict=True,
    )

    return columns, data
