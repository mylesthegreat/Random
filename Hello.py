#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

s = 'do goat sheep boat'
replace_s = s.find('goat')
print(replace_s)

if s.startswith('do'):
    print('It does begin with \"do\"')

user_input = input('Please klll me : ')

if user_input.startswith('hello'):
    sys.exit()


def string_touppercase(string):
    upper_string = string.upper()
    print(upper_string)


def string_touppercfase():
    string = input("Enter string to convert to captitals")
    upper_string = string.upper()
    print(upper_string)

string_touppercase("fr")
string_touppercfase()
