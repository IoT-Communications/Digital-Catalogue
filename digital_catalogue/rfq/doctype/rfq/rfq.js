// Copyright (c) 2022, IoT Communications (Pty) Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('RFQ', {
	refresh: function(frm) {
        frm.add_custom_button('Quote', () => {
            frappe.new_doc('Quotation', {
                product_or_service_category: frm.doc.product_or_service_category,
				rfq_number: frm.doc.name				
            })
        })
        
		}
});
