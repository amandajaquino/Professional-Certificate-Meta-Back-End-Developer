""" employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]
 
def get_employee(id): 
    for employee in employee_list:
        if employee['id'] == id:
            return employee
 
print(get_employee(12458)) """
# OUTPUT {'id': 12458, 'name': 'Paul', 'department': 'House Floor'}
# The code runs well and will return the user Paul, as its ID, 12458, is matched. The challenge comes when the list gets bigger. 
# You could optimize the code to split the search, but even with this, it still lacks in performance in comparison to other data structures, such as the dictionary.


employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}
 
def get_employee_from_dict(id):
    return employee_dict[id]
 
 
print(get_employee_from_dict(12458))
## OUTPUT{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}