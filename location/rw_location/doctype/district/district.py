# Copyright (c) 2024, Spiderbit LTD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class District(Document):

	def after_save(self):
		frappe.cache().delete_value("cached_districts")

	def on_trash(self):
		frappe.cache().delete_value("cached_districts")
