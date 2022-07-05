import frappe

def validate(doc,method):
	pass
	# set_permissions(doc)

def set_permissions(doc):
	reports_to_list = make_reports_to_data(doc)
	if reports_to_list:
		for report_to in reports_to_list:
			user = frappe.db.get_value("Employee", {'name':report_to}, 'user_id')
			if user:
				if not check_duplicate_permission(doc,user):
					user_permission=frappe.new_doc("User Permission")
					user_permission.applicable_for="Task"
					user_permission.user=user
					user_permission.allow="Employee"
					user_permission.for_value=doc.assign_to_user
					user_permission.apply_to_all_doctypes=0
					user_permission.reference_doctype=doc.doctype
					user_permission.reference_docname=doc.name
					user_permission.save()
			elif report_to:
				frappe.msgprint("User id is missing for '{0}' assign_to_user whose report to of '{1}'".format(report_to,doc.assign_to_user))
	else:
		frappe.msgprint("Please add report to for '{0}' assign_to_user".format(doc.assign_to_user))

def make_reports_to_data(doc):
	reports_to_list = []
	if doc.assign_to_user:
		reports_to_list.append(doc.assign_to_user)
		reports_to = frappe.db.get_value("Employee", {'name':doc.assign_to_user}, 'reports_to')
		while reports_to != None:
			reports_to_list.append(reports_to)
			reports_to = frappe.db.get_value("Employee", {'name':reports_to}, 'reports_to')
		return reports_to_list
	else:
		frappe.msgprint("Please add value in assign_to_user field .")

def check_duplicate_permission(doc,user):
	return  frappe.db.get_all("User Permission", filters={
			'allow': "Employee",
			'for_value': doc.assign_to_user,
			'user': user,
			'applicable_for': "Task",
			'name': ['!=', doc.name]
		}, limit=1)