import frappe
from frappe.model.document import Document

class Lead(Document):
    def validate(self):
        # Validate phone number format
        if self.phone_number and not self.phone_number.isdigit():
            frappe.throw("Phone Number should contain only digits")
        
        if self.alternate_phone_number and not self.alternate_phone_number.isdigit():
            frappe.throw("Alternate Phone Number should contain only digits")
        
        # Ensure state is uppercase
        if self.state:
            self.state = self.state.upper()
