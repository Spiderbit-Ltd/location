# Copyright (c) 2024, Spiderbit LTD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Village(Document):

	def after_save(self):
		if self.cell_id:
			frappe.cache().delete_value(f"cached_villages_{self.cell_id}")

	def on_trash(self):
		if self.cell_id:
			frappe.cache().delete_value(f"cached_villages_{self.cell_id}")
