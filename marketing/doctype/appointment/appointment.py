#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Appointment(Document):
    def validate(self):
        self.validate_time_slot()
        
    def validate_time_slot(self):
        """Validate that the time matches the selected time slot"""
        time_slots = {
            "9am - 12pm": "09:00:00",
            "10am - 1pm": "10:00:00",
            "11am - 2pm": "11:00:00",
            "12pm - 3pm": "12:00:00",
            "1pm - 4pm": "13:00:00",
            "2pm - 5pm": "14:00:00",
            "3pm - 6pm": "15:00:00",
            "4pm - 7pm": "16:00:00",
            "5pm - 8pm": "17:00:00",
            "6pm - 9pm": "18:00:00",
            "7pm - 10pm": "19:00:00"
        }
        
        if self.time_slot and self.time:
            expected_time = time_slots.get(self.time_slot)
            if expected_time and str(self.time) != expected_time:
                frappe.throw(f"Time {self.time} does not match the selected time slot {self.time_slot}. Expected time: {expected_time}")
        
        if self.qc_time_slot and self.qc_time:
            expected_qc_time = time_slots.get(self.qc_time_slot)
            if expected_qc_time and str(self.qc_time) != expected_qc_time:
                frappe.throw(f"QC Time {self.qc_time} does not match the selected QC time slot {self.qc_time_slot}. Expected time: {expected_qc_time}")
