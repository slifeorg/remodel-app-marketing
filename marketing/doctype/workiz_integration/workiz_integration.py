# Copyright (c) 2024, TRG and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

class WorkizIntegration(Document):
	def validate(self):
		if self.workiz_uuid:
			# UUID format: 8-4-4-4-12 hexadecimal digits
			uuid_pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.I)
			if not uuid_pattern.match(self.workiz_uuid):
				frappe.throw("Invalid Workiz UUID format. Expected format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
