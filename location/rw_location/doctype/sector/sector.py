# Copyright (c) 2024, Spiderbit LTD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Sector(Document):
	def after_save(self):
		if self.district_id:
			frappe.cache().delete_value(f"cached_sectors_{self.district_id}")

	def on_trash(self):
		if self.district_id:
			frappe.cache().delete_value(f"cached_sectors_{self.district_id}")
