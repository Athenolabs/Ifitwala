# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "farm_management"
app_title = "Farm Management"
app_publisher = "Ifitwala Farm Ltd."
app_description = "An app to complement ERPNext for commercial farmers"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "francois@ifitwala.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/farm_management/css/farm_management.css"
# app_include_js = "/assets/farm_management/js/farm_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/farm_management/css/farm_management.css"
# web_include_js = "/assets/farm_management/js/farm_management.js"

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

# before_install = "farm_management.install.before_install"
# after_install = "farm_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "farm_management.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"farm_management.tasks.all"
# 	],
# 	"daily": [
# 		"farm_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"farm_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"farm_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"farm_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "farm_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "farm_management.event.get_events"
# }

