annual_salary = input("What is your annual salary? ")
portion_saved = input("What is the portion of your salary to be saved? Eg. write 0.1 for 10% ")
total_cost = input("What is the cost of your home? ")

current_savings = 0
portion_down_payment = 0.25 #25% assumed
r = 0.04 #annual return of 4&
down_payment_cost = float(total_cost) * float(portion_down_payment)
months = 0 

while float(down_payment_cost) > float(current_savings):
    months +=1
    current_savings += (current_savings*r)/12
    current_savings += (float(annual_salary)/12) * float(portion_saved)


print("It will take", months, "months to complete payment")    
