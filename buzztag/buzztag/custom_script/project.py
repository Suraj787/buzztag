# -*- coding: utf-8 -*-
# Copyright (c) 2020, bizmap technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import datetime ,timedelta
import calendar
from dateutil import rrule
from dateutil.relativedelta import relativedelta
from frappe.model.mapper import get_mapped_doc
import json


    
@frappe.whitelist()
def allocate_user(userdetails,project_name):
    doc1 = frappe.new_doc('User Permission')
    doc1.user= userdetails
    doc1.allow="Project"
    doc1.for_value= project_name
    doc1.insert(
           ignore_permissions=True,
           ignore_links=True,
           ignore_if_duplicate=True,
           ignore_mandatory=True 
        
        )

        
