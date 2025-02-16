// Copyright (c) 2024, TRG and contributors
// For license information, please see license.txt

frappe.ui.form.on('Workiz Integration', {
	refresh: function(frm) {
		// Add custom client-side logic here
	},

	workiz_uuid: function(frm) {
		if (frm.doc.workiz_uuid) {
			const uuidPattern = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
			if (!uuidPattern.test(frm.doc.workiz_uuid)) {
				frappe.msgprint(__('Invalid Workiz UUID format. Expected format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'));
				frm.doc.workiz_uuid = '';
				frm.refresh_field('workiz_uuid');
			}
		}
	}
});
