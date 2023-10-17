import frappe
import math
@frappe.whitelist()
def calculate_distance(emp_lat, emp_long):
    system_latitude = frappe.db.sql("select value from `tabSingles` where doctype = 'Attendance Setting' and field = 'latitude';", as_dict=1)
    system_longitude = frappe.db.sql("select value from `tabSingles` where doctype = 'Attendance Setting' and field = 'longitude';", as_dict=1)
    if not system_latitude or not system_longitude:
        frappe.throw('Ask admin to enter latitude & longitude in attendance setting')
        return {
            'invalid_distance' : 1
        }
    else:
        # Radius of the Earth in kilometers
        radius = 6371.0

        # Convert latitude and longitude from degrees to radians
        system_lat = math.radians(float(system_latitude[0].get('value')))
        system_lon = math.radians(float(system_longitude[0].get('value')))
        emp_lat = math.radians(float(emp_lat))
        emp_lon = math.radians(float(emp_long))

        # Haversine formula
        dlon = emp_lon - system_lon
        dlat = emp_lat - system_lat
        a = math.sin(dlat / 2)**2 + math.cos(system_lat) * math.cos(emp_lat) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        employee_distance = radius * c * 1000
        maximum_allowed_distance = frappe.db.sql("select value from `tabSingles` where doctype = 'Attendance Setting' and field = 'maximum_distance';", as_dict=1)[0].get('value')
        if employee_distance > float(maximum_allowed_distance):
            return {
                'invalid_distance' : 1
            }

def validate_attendance(doc, method):
    enable_location = maximum_allowed_distance = frappe.db.sql("select value from `tabSingles` where doctype = 'Attendance Setting' and field = 'enable';", as_dict=1)[0].get('value')
    if doc.invalid_distance == 1 and enable_location == 1:
        maximum_allowed_distance = frappe.db.sql("select value from `tabSingles` where doctype = 'Attendance Setting' and field = 'maximum_distance';", as_dict=1)[0].get('value')
        frappe.throw("You can not mark attendance as your distance is greater than {0} meter".format(maximum_allowed_distance))

