#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:43:25 2023

@author: carlosalonzo
"""

initial_cost = 5000000
interim_standard = 900000

def Alternative_M(year, inflation_rate):

    initial_cost
    annual_cost_1 = 200000
    expansion_year = year + 2
    expanded_construction_cost = 6000000

    # Calculate present value of profits
    current_profit=0
    for i in range(expansion_year - 1):
        current_profit+=interim_standard-annual_cost_1

    expanded_profit=0
    for i in range(expansion_year, 30):
        expanded_profit+=(interim_standard-annual_cost_1)*2
       
    profit_M = current_profit+expanded_profit-(expanded_construction_cost+initial_cost)
    
    present_value_m=profit_M*(1/(1+inflation_rate)**(year))
    
    return present_value_m


def Alternative_S(year, inflation_rate):

    construction_cost_initial = initial_cost + 1150000
    construction_cost_later = 3000000
    annual_cost_initial = 250000
    annual_cost_later = 400000
    expansion_year = year + 1

    # Calculate present value of profits
    current_profit = 0
    for i in range(expansion_year - 1):
        current_profit+=interim_standard-annual_cost_initial

    expanded_profit = 0
    for i in range(expansion_year, 30):
        expanded_profit+=(interim_standard*2)-annual_cost_later

    profit_S = current_profit+expanded_profit-(construction_cost_later+construction_cost_initial)
    
    present_value_s=profit_S*(1/(1+inflation_rate)**(year))
    
    return present_value_s


def Alternative_C(year, inflation_rate):
    construction_cost_initial = 9000000
    annual_cost = 400000
    annual_earnings = 100000
    expansion_year = year

    # Calculate present value of profits
    current_profit = 0
    for i in range(expansion_year - 1):
        current_profit += annual_earnings + interim_standard - 400000
        
    expanded_profit=0
    for i in range(expansion_year,30):
        expanded_profit +=(interim_standard*2)-annual_cost
        
    profit_C = expanded_profit+current_profit-construction_cost_initial
    
    
    present_value_c=profit_C*(1/(1+inflation_rate)**(year))
    
    return present_value_c



def rateFunction(rateinput):
    print("{0:<20}{1:<20}{2:<20}{3:<20}{4:<10}".format("Effective Year", "Minimal-Profit", "Staged-Profit", "Complete-Profit", "Best Alternative"))
    for i in range(1,31):
        list_best=[]
        profit_M = Alternative_M(i, rateinput)
        profit_S = Alternative_S(i, rateinput)
        profit_C = Alternative_C(i, rateinput)
        list_best.append(profit_C)
        list_best.append(profit_S)
        list_best.append(profit_M)

        if  profit_M  == max(list_best):
            best= "Minimal"
        elif profit_S ==  max(list_best):
            best= "Staged"
        elif profit_C == max(list_best):
            best="Complete"
   
        print("{0:<20}{1:<20,.2f}{2:<20,.2f}{3:<20,.2f}{4:<10}".format(i,profit_M,profit_S,profit_C,best))

print("table for a rate of 3%")
rateFunction(.003)
print("table for a rate of 4%")
rateFunction(.004)
        



