
add_new_employee=1
print_all_employees=2
delete_by_age_range=3
update_salary_given_a_name=4
end_program=5
employees= []


while True :
    choice= int(input('enter your choice:'))
    if choice < 1 and choice>5:
        print('invalid range , try again')
    elif choice == 1 :
        print('adiing new employee:')
        name = input('enter your name:')
        age = int(input('enter your age:'))
        salary= float(input('enter your salary:'))
        employees.append({"name": name, "age": age, "salary": salary})

    elif choice ==2 :
        print(employees)
    elif choice ==3 :
        if 25<age<31 :
            employees.remove
    elif choice == 4 :
        name = input("Enter employee name to update the salary: ")
        new_salary = float(input("Enter new salary: "))
        for emp in employees:
            if emp['name'] == name:
                emp['salary'] = new_salary
                print(f"Salary updated for {name}.")
                break
    elif choice == 5 :
        print('program ended')
        break        
            





