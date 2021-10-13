#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 22:22:07 2021

@author: tyler
"""


ask_diameter = input("Please enter the diameter of your pizza: ")
pizza_diameter = int(ask_diameter)

if (pizza_diameter > 24 or pizza_diameter < 8):
    print("ENTRY ERROR.")
    print('Pizza must have a diameter in the range of 8" to 24" inclusive!')
else:    
    pizza_diameter = input("Please enter the diameter of your pizza: ")