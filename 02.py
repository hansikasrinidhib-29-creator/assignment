annual_salary=float(input("Enter the annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save,as a decimal:"))
dream_house=float(input("Enter the dream house money:"))
semi_raise=float(input("Enter the semi-annual raise,as a decimal:"))
down_payment=0.25*dream_house
months=0
annual_interest=0.04
initial_savings=0
while initial_savings<down_payment:
    monthly_salary=annual_salary/12
    initial_savings+=initial_savings*(annual_interest/12)
    initial_savings+=monthly_salary*portion_saved
    months+=1
    if months%6==0:
        annual_salary+=annual_salary*semi_raise
print(f"number of months:{months}")