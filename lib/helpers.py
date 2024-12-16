from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
            print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    else:
        print(f"Employee {name} not found")



def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    else:
        print(f"Employee {id_} not found")

def create_employee():
    try:
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        department_id = int(input("Enter the employee's department id: "))
        
        employee = Employee.create(name, job_title, department_id)
        
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error creating employee: {e}")


def update_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(employee_id)
        
        if employee:
            name = input("Enter the employee's new name: ")
            job_title = input("Enter the employee's new job title: ")
            department_id = int(input("Enter the employee's new department id: "))
            
            employee.name = name
            employee.job_title = job_title
            employee.department_id = department_id
            
            employee.update()
            print(f"Success: {employee}")
        else:
            print(f"Employee with id {employee_id} not found")
    
    except ValueError as e:
        print(f"Error updating employee: {e}")


def delete_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(employee_id)
        
        if employee:
            employee.delete()
            print(f"Employee {employee_id} deleted")
        else:
            print(f"Employee with id {employee_id} not found")
    
    except ValueError as e:
        print(f"Error deleting employee: {e}")


def list_department_employees():
    try:
        department_id = int(input("Enter the department's id: "))
        
        department = Department.find_by_id(department_id)
        
        if department:
            employees = department.employees()
            if employees:
                for employee in employees:
                    print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
            else:
                print(f"No employees found in Department {department_id}")
        else:
            print(f"Department with id {department_id} not found")
    
    except ValueError as e:
        print(f"Error: {e}")