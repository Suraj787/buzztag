from . import __version__ as app_version

app_name = "buzztag"
app_title = "buzztag"
app_publisher = "bizmaptech"
app_description = "buzztag"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@bizmap.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/buzztag/css/buzztag.css"
# app_include_js = "/assets/buzztag/js/buzztag.js"

# include js, css files in header of web template
# web_include_css = "/assets/buzztag/css/buzztag.css"
# web_include_js = "/assets/buzztag/js/buzztag.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "buzztag/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
 "doctype" : "public/js/doctype.js",
 "Project":"public/js/project.js",
 "Task":"public/js/task.js"
 }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "buzztag.install.before_install"
# after_install = "buzztag.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "buzztag.uninstall.before_uninstall"
# after_uninstall = "buzztag.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "buzztag.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Attendance Request": "buzztag.Override.attendance_request.CustomAttendanceRequest",
    "Attendance":"buzztag.Override.attendance.CustomAttendance"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Task":{
        "validate":"buzztag.buzztag.custom_script.task.validate"
	},
	"DocShare":{
        "validate":"buzztag.buzztag.custom_script.docshare.validate"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"buzztag.tasks.all"
# 	],
# 	"daily": [
# 		"buzztag.tasks.daily"
# 	],
# 	"hourly": [
# 		"buzztag.tasks.hourly"
# 	],
# 	"weekly": [
# 		"buzztag.tasks.weekly"
# 	]
# 	"monthly": [
# 		"buzztag.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "buzztag.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "buzztag.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "buzztag.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"buzztag.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
