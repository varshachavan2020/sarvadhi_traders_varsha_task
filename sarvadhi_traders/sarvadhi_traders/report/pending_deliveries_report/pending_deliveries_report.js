frappe.query_reports["Pending Deliveries Report"] = {
    filters: [
        {
            fieldname: "customer",
            label: __("Customer"),
            fieldtype: "Link",
            options: "Customer",
            reqd: 0,
        },
        {
            fieldname: "delivery_date",
            label: __("Delivery Date"),
            fieldtype: "Date",
            reqd: 0,
        },
    ],
    onload: function(report) {
        // Ensure the report fetches fresh data when filters are cleared
        report.refresh();
    },
    get_data: function(filters) {
        // Reset the filters object when fields are cleared
        if (!filters.delivery_date) {
            delete filters.delivery_date;
        }
        return filters;
    },
};
