import frappe

def validate(doc,method):
	set_permissions(doc)

def set_permissions(doc):
	if not check_duplicate_permission(doc):
		user_permission=frappe.new_doc("User Permission")
		user_permission.applicable_for="Task"
		user_permission.user=doc.assign_task
		user_permission.allow="Employee"
		user_permission.for_value=frappe.db.get_value("Employee", {'user_id':doc.assign_task}, 'name')
		user_permission.apply_to_all_doctypes=0
		user_permission.reference_doctype=doc.doctype
		user_permission.reference_docname=doc.name
		user_permission.save()

def check_duplicate_permission(doc):
	return  frappe.db.get_all("User Permission", filters={
			'allow': "Employee",
			'for_value': frappe.db.get_value("Employee", {'user_id':doc.assign_task}, 'name'),
			'user': doc.assign_task,
			'applicable_for': "Task",
			'name': ['!=', doc.name]
		}, limit=1)