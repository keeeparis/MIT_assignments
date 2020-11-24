# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:27:25 2020

@author: Vladimir Trotsenko
"""

#########################
#### ASSIGNIMENT ########
#########################
#### FIRST ##############
#########################

annual_salary = float(input('Enter the starting annual salary: '))
portion_saved = float(input('Enter the portion of salary to be saved: '))
total_cost = float(input('Enter the cost of your dream home: '))

portion_down_payment = (0.25)*total_cost
current_savings = 0
r = 0.04
months = 0   
    
while current_savings < portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += portion_saved*(annual_salary/12)
    months += 1
if current_savings >= portion_down_payment:
    print('Number of months:', months)

#########################
#### SECOND #############
#########################

annual_salary = float(input('Enter the starting annual salary: '))
portion_saved = float(input('Enter the portion of salary to be saved: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual salary raise: '))

portion_down_payment = (0.25)*total_cost
current_savings = 0
r = 0.04
months = 0 
   
while current_savings < portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += portion_saved*(annual_salary/12)
    months += 1 
    if months > 1 and months%6 == 1:
        annual_salary += annual_salary*semi_annual_raise 
    
if current_savings >= portion_down_payment:
    print('Number of months:', months)

#########################
#### THIRD ##############
#########################

annual_salary = float(input('Enter the starting annual salary: '))
monthly_salary = annual_salary/12
semi_annual_raise = 0.07
r = 0.04
monthly_r = r/12
total_cost = 1000000
portion_down_payment = (0.25)*total_cost
steps = 0

portion_saved = 1
epsilon = 100
low = 0
high = portion_saved
ans = (low + high)/2.0
total_salary = 0

for i in range(36):
    if i != 1 and i%6 == 1:
        monthly_salary += monthly_salary*semi_annual_raise
    monthly_salary += monthly_salary*monthly_r
    total_salary += monthly_salary
if total_salary < portion_down_payment - 100:
    print('It is not possible to pay the down payment in three years.')
else:
    savings = total_salary*ans
    while abs(savings - portion_down_payment) >= epsilon:
        print('low =', str(low), 'high =', str(high), 'ans =', str(ans))
        steps += 1
        if savings < portion_down_payment:
            low = ans
        else:
            high = ans
        ans = (low + high)/2.0
        savings = total_salary*ans
    print('Best saving rate:', "%.4f" %ans)    ### print 4 digits after decimal
    print('Steps in bisection search:', str(steps))    
