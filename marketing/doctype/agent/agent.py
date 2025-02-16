import frappe
from frappe.model.document import Document

class Agent(Document):
    def before_save(self):
        # Auto-generate full name from first and last name if not set
        if not self.full_name and (self.first_name or self.last_name):
            self.full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
