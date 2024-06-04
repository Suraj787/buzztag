import frappe
from hrms.hr.doctype.attendance.attendance import Attendance
from frappe.utils import getdate, nowdate


class CustomAttendance(Attendance):


    	def validate_attendance_date(self):
            date_of_joining = frappe.db.get_value("Employee", self.employee, "date_of_joining")

            # leaves can be marked for future dates
            if (
                self.status != "On Leave"
                and not self.leave_application
                and getdate(self.attendance_date) > getdate(nowdate())
            ):
                # frappe.throw(_("Attendance can not be marked for future dates"))
                pass
            elif date_of_joining and getdate(self.attendance_date) < getdate(date_of_joining):
                frappe.throw(_("Attendance date can not be less than employee's joining date"))
