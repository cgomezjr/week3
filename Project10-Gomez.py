print("This program will calculate an employee's total weekly pay")

#input of the hourly pay
hourlyWage =  float(input("What is your hourly wage?\n"))

#input of the regular hours. No overtime
regularHours =  float(input("What is your total regular hours?\n"))

#input of the overtime hours.
overtimeHours =  float(input("What is your overtime hours?\n"))

#calculate the total weekly pay
weeklyPay = (hourlyWage * regularHours) + (1.5 * hourlyWage * overtimeHours)

print("\nThis is your total weekly pay: $" + str(weeklyPay))

