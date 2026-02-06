#payment of gross salary and amount to be deducted when the salary si paid

salary = float(input("enter gross salary: "))
if salary <= 5999:
    print("payment is 150.00")

elif salary >= 6000 and salary < 7999:
    print("payment is 300.00")

elif salary >= 8000 and salary < 11999:
    print("payment is 400.00")

elif salary >= 12000 and salary < 14999:
    print("payment is 500.00")

elif salary >= 13000 and salary < 19999:
    print("payment is 600.00")

elif salary >= 20000 and salary < 24999:
    print("payment is 700.00")

elif salary >= 25000 and salary < 29999:
    print("payment is 800.00")

elif salary >= 30000 and salary < 49999:
    print("payment is 1000.00")

elif salary >= 50000 and salary < 99999:
    print("payment is 1600.00")

else:
    print("payment is 2000.00")
