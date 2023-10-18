import frappe
import math
@frappe.whitelist()
def calculate_distance(emp_lat, emp_long, branch):
    system_location_data = frappe.db.sql("select latitude,longitude, enable  from `tabBranch` where name = '{0}';".format(branch), as_dict=1)
    invalid_distance = 0

    if system_location_data and system_location_data[0].get('enable')  == 1:
        if not system_location_data[0].latitude or not system_location_data[0].longitude:
            invalid_distance = 1
            frappe.throw('Ask admin to enter latitude & longitude in <b> Branch </b> doctype')    
        else:
            # Radius of the Earth in kilometers
            radius = 6371.0
            # Convert latitude and longitude from degrees to radians
            system_lat = math.radians(system_location_data[0].get('latitude'))
            system_lon = math.radians(system_location_data[0].get('longitude'))
            emp_lat = math.radians(float(emp_lat))
            emp_lon = math.radians(float(emp_long))

            # Haversine formula
            dlon = emp_lon - system_lon
            dlat = emp_lat - system_lat
            a = math.sin(dlat / 2)**2 + math.cos(system_lat) * math.cos(emp_lat) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            employee_distance = radius * c * 1000
            maximum_allowed_distance = frappe.db.sql("select maximum_distance from `tabBranch` where name = '{0}';".format(branch), as_dict=1)

            if maximum_allowed_distance and employee_distance > maximum_allowed_distance[0].get('maximum_distance'):
                invalid_distance = 1
                return invalid_distance
    return invalid_distance




