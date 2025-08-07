# Copyright (c) 2024, Spiderbit LTD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Cell(Document):
    def after_save(self):
        if self.sector_id:
            frappe.cache().delete_value(f"cached_cells_{self.sector_id}")

    def on_trash(self):
        if self.sector_id:
            frappe.cache().delete_value(f"cached_cells_{self.sector_id}")
