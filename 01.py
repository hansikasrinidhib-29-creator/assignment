annual_salary=int(input("enter the annual salary:"))
portion_saved=float(input("enter the percent of your salary to save,as a decimal:"))
dream_home_cost=int(input("enter the dream home cost:"))
down_payment=0.25*(dream_home_cost)
monthly_salary=annual_salary/12
initial_savings=0
annual_return=0.04
months=0
while initial_savings<down_payment:
    initial_savings+=initial_savings*(annual_return/12)
    initial_savings+=monthly_salary*portion_saved
    months+=1
print(f"Number of months:{months}")