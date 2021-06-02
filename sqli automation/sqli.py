#! /usr/bin/env python3

#Code to automate time based sqli

import requests
import fun

url = input("Enter url: ")
r = requests.get(url)
print("status : ",r.status_code) # prints http status code to check if the site is up

characters = fun.escape(url,"?id")
    



