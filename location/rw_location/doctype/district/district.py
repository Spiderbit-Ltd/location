# Copyright (c) 2024, Spiderbit LTD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class District(Document):

	def after_save(self):
		if self.province_id:
			frappe.cache().delete_value(f"cached_districts_{self.province_id}")

	def on_trash(self):
		if self.province_id:
			frappe.cache().delete_value(f"cached_districts_{self.province_id}")
