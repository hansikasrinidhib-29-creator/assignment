annual_salary=int(input("enter the annual salary:"))
house_cost=1000000
down_payment=0.25*house_cost
annual_return=0.04
semi_annual_return=0.07
months=36
salary=annual_salary
current_savings=0
for i in range (1,months+1):
    monthly_salary=salary/12
    current_savings+=current_savings*(annual_return/12)
    current_savings+=monthly_salary*1.0
    if i%6==0:
        salary+=salary*semi_annual_return
if current_savings<down_payment:
    print("the person cannot pay the down payment if he save monthly salary all money")
else:
    low=0
    high=1
    steps=0
    best_savings=0
    while True:
        rate=(low+high)/2
        steps+=1
        current_savings=0
        salary=annual_salary
        for i in range(1,months+1):
            monthly_salary=salary/12
            current_savings+=current_savings*(annual_return/12)
            current_savings+=monthly_salary*rate
            if i%6==0:
                salary+=salary*semi_annual_return
        if abs(current_savings-down_payment)<=100:
            best_rate=rate
            break
        elif current_savings<down_payment:
            low=rate
        else:
            high=rate
    print(f"best rate: {round(best_rate,4)}")