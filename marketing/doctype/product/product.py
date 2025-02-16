#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Product(Document):
    def validate(self):
        self.validate_rank()
        self.update_top_10_status()
        
    def validate_rank(self):
        """Validate that rank is between 1 and 10 if set"""
        if self.rank:
            if not (1 <= self.rank <= 10):
                frappe.throw("Rank must be between 1 and 10")
            
            # Check for duplicate ranks in top 10
            existing = frappe.get_all(
                "Product",
                filters={
                    "rank": self.rank,
                    "name": ["!=", self.name]
                }
            )
            if existing:
                frappe.throw(f"Rank {self.rank} is already assigned to another product")
    
    def update_top_10_status(self):
        """Automatically update is_top_10 based on rank"""
        self.is_top_10 = 1 if self.rank and 1 <= self.rank <= 10 else 0
