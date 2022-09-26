employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
print(employee_file.read())

employee_file.close()


employee_file = open("employees.txt", "a")

print(employee_file.write("\nToby - Human Resources"))

employee_file.close()



