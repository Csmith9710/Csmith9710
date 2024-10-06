 # Christopher Smith
 # 10/06/2024
 # P1HW1
 # This assignment is a program that does some basic math on numbers entered.
budget = int()
destination = int()
gasmoney = int()
accom = int()
food = int()
expenses = (gasmoney + accom + food)
print('This program calculates and displays travel expenses')
print()
print('Enter budget:', budget)
print()
print('Enter your travel destination:', destination)
print()
print('How much do you think you will spend on gas?', gasmoney)
print()
print('Approximately, how much will you need for accomodation/hotel?', accom)
print()
print('Last, how much do you need for food?', food)
print()
print('-------------Travel Expenses------------')
print('Location:', destination)
print('Initial Budget:', budget)
print()
print('Fuel:', gasmoney)
print('Accomodation:', accom)
print('Food:', food)
print()
print('Remaining Balance:', budget - expenses)


