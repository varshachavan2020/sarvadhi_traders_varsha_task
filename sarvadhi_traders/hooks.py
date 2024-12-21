app_name = "sarvadhi_traders"
app_title = "Sarvadhi Traders"
app_publisher = "varsha"
app_description = "Sarvadhi Traders"
app_email = "varsha.r.chavan2020@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sarvadhi_traders/css/sarvadhi_traders.css"
# app_include_js = "/assets/sarvadhi_traders/js/sarvadhi_traders.js"

# include js, css files in header of web template
# web_include_css = "/assets/sarvadhi_traders/css/sarvadhi_traders.css"
# web_include_js = "/assets/sarvadhi_traders/js/sarvadhi_traders.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sarvadhi_traders/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sarvadhi_traders.utils.jinja_methods",
# 	"filters": "sarvadhi_traders.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sarvadhi_traders.install.before_install"
# after_install = "sarvadhi_traders.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sarvadhi_traders.uninstall.before_uninstall"
# after_uninstall = "sarvadhi_traders.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sarvadhi_traders.utils.before_app_install"
# after_app_install = "sarvadhi_traders.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sarvadhi_traders.utils.before_app_uninstall"
# after_app_uninstall = "sarvadhi_traders.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sarvadhi_traders.notifications.get_notification_config"

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

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sarvadhi_traders.tasks.all"
# 	],
# 	"daily": [
# 		"sarvadhi_traders.tasks.daily"
# 	],
# 	"hourly": [
# 		"sarvadhi_traders.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sarvadhi_traders.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sarvadhi_traders.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sarvadhi_traders.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sarvadhi_traders.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sarvadhi_traders.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sarvadhi_traders.utils.before_request"]
# after_request = ["sarvadhi_traders.utils.after_request"]

# Job Events
# ----------
# before_job = ["sarvadhi_traders.utils.before_job"]
# after_job = ["sarvadhi_traders.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sarvadhi_traders.auth.validate"
# ]
