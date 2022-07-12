import frappe

def validate(doc,method):
    if doc.share_doctype == 'Task':
        assign_task_for_share_user(doc)

def assign_task_for_share_user(doc):
    if not check_duplicate_todo(doc):
        todo = frappe.new_doc("ToDo")
        todo.owner = doc.user
        todo.assigned_by = frappe.session.user
        todo.description = frappe.db.get_value("Task", {'name':doc.share_name},'subject')
        todo.date = frappe.db.get_value("Task", {'name':doc.share_name},'exp_end_date')
        todo.reference_type = "Task"
        todo.reference_name = doc.share_name
        todo.insert(ignore_permissions=True)

def check_duplicate_todo(doc):
    return  frappe.db.get_all("ToDo", filters={
            'owner' : doc.user,
            'assigned_by' : frappe.session.user,
            'description' : frappe.db.get_value("Task", {'name':doc.share_name},'subject'),
            'date' : frappe.db.get_value("Task", {'name':doc.share_name},'exp_end_date'),
            'reference_type' : "Task",
            'name': ['!=', doc.share_name]
        }, limit=1)
