import frappe

def validate(doc, method):
	if not doc.is_new():
		assign_to_task(doc)

def after_insert(doc, method):
	assign_to_task(doc)

# get users to create doc share permission - Anuradha(08/07/2024)
def assign_to_task(doc):
	if doc.task_assign_to:
		create_doc_share(doc, doc.task_assign_to)
	if frappe.session.user:
		create_doc_share(doc, frappe.session.user)
	for assign in doc.assign_to:
		if assign.user:
			create_doc_share(doc, assign.user)

# create doc share permission for user - Anuradha(08/07/2024)
def create_doc_share(doc, user):
	if len(frappe.get_all('DocShare',{'user':user,"share_doctype": 'Task',"share_name": doc.name})) == 0: 
		doc_share = frappe.new_doc("DocShare")
		doc_share.update({
	        'share_doctype' : 'Task',
	        'user' : user,
	        'share_name':doc.name,
	        'read':True,
	        'write':True,
	        'share':False,
	        'submit':False,
	        'everyone':False,
	        'notify_by_email':False
	    })
		doc_share.insert(ignore_permissions=True)

		# frappe.response['message'] = "hello"
