basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
number_of_camera = int(input("Enter the number of camera sold: "))
price = float(input("Enter the total prices: "))
bonus = (bonus_rate * number_of_camera)
commission = (commission_rate * number_of_camera * price)
print("Bonus        =%6.2f" % bonus)
print("Commision = %6.2f" % commission)
print("Gross salary = %6.2f" % (basic_salary + bonus + commission))

