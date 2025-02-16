# Copyright (c) 2024, TRG and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Address(Document):
	def validate(self):
		# Add validation logic here if needed
		pass
