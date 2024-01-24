import frappe
from frappe import _
from frappe.model.document import Document
from erpnext.hr.doctype.attendance_request.attendance_request import AttendanceRequest
from frappe.utils import add_days, date_diff, getdate

from erpnext.hr.doctype.employee.employee import is_holiday
from erpnext.hr.utils import validate_active_employee, validate_dates



class CustomAttendanceRequest(AttendanceRequest):

    def validate(self):
        # self.validate_max_days()
        validate_active_employee(self.employee)
        # validate_dates(self, self.from_date, self.to_date)
        if self.half_day:
            if not getdate(self.from_date) <= getdate(self.half_day_date) <= getdate(self.to_date):
                frappe.throw(_("Half day date should be in between from date and to date"))

    def validate_max_days(self):
        max_days =2 
        if (nowdate.getdate>max_days):
            frppae.throw(("You can not allowed to apply for this many days."))
