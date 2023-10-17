# Copyright (c) 2023, ranbir and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	data = []
	columns = [
		{
            'fieldname': 'emp_id',
            'label': _('Employee Id'),
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'employee_name',
            'label': ('Employee Name'),
            'fieldtype': 'data'
        },
        {
            'fieldname': 'father_name',
            'label': ('Father Name'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'gender',
            'label': ('Gender'),
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'designation',
            'label': ('Designation'),
            'fieldtype': 'data'
        },
        {
            'fieldname': 'date_of_joining',
            'label': ('DOJ'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'esi_no',
            'label': ('ESI No'),
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'pf_no',
            'label': ('PF No'),
            'fieldtype': 'data'
        },
        {
            'fieldname': 'wage_fixed',
            'label': ('Wage Fixed Including VDA'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'gender',
            'label': ('Gender'),
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'designation',
            'label': ('Designation'),
            'fieldtype': 'data'
        },
        {
            'fieldname': 'doj',
            'label': ('DOJ'),
            'fieldtype': 'Data'
        }
	]
	query = """
		select
			employee_name,
			emp_id, gender,
			date_of_joining,
			designation from `tabEmployee`
			where status = 'active';
	"""
	employee_list = frappe.db.sql(query, as_dict = True)
	print('########'*30)
	print(employee_list)
	return columns, employee_list
