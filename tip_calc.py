print("Welcome to the tip calculator!")
bill  = int(input("enter the total amount to be paid :-"))
tip =int(input("how much tip you want to give ? 10,12 or 15 :-"))
people = int(input("total no of people want to split the bill is: "))
amount = (bill + bill*tip/100)/people
print(f'the total amount to be paid by each person is {amount}') 