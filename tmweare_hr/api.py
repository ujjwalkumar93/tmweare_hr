import frappe

def validate_salary_slip(doc, method):
    payroll_entry_doc = frappe.get_doc('Payroll Entry', doc.get('payroll_entry'))
    
    print('###22'*300)
    print(payroll_entry_doc)
    for emp in payroll_entry_doc.employees:
        print('____', emp.get('employee'))
        ssa = frappe.get_doc('Salary Structure Assignment', {
            'employee' : emp.get('employee'),
            'salary_structure' : 'Worker - Salary Structure -1'
        })
        print(ssa)
        total = ssa.get('base') + ssa.get('dearness_allowance') + ssa.get('hra') + ssa.get('conveyance') + ssa.get('medical_allowance') + ssa.get('other_allowance') + ssa.get('special_allowance') + ssa.get('education')
        print('total: ', total)

