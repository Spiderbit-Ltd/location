# Copyright (c) 2024, Spiderbit LTD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Province(Document):

	def after_save(self):
		frappe.cache().delete_value("cached_provinces")

	def on_trash(self):
		frappe.cache().delete_value("cached_provinces")
