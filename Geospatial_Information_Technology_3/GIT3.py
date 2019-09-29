 # -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:50:44 2019

@author: Petronium
"""

# Exercise 2 ------------------------------------------------------------------

def input_mail_parser():
    """
    Function to automatically generate email addresses
    
    Args:
        None
    Returns:
        automatically generate email adress
    
    """
    
    first_name = input("Enter your first name: ")
    family_name = input("Enter your family name: ")
    birth_date = input("Enter your date of birth in format dd-mm-yyyy: ")
    
    mail = first_name[0].lower() + '.' + family_name[:5].lower() + birth_date[-2:] + '@aau.dk'
   
    return mail

#print(input_mail_parser())


names = [['Issac', 'Newtoon', '25-12-1642'],['Piotr', 'Michalak', '22-01-1996'], 
         ['John', 'Harrison', '24-03-1693']]


def list_mail_parser(nested_list):
    """
    Function to automatically generate email addresses based on nested list
    
    Args:
        nested_list (list): the nested list to be parser
    Returns:
        automatically generate list of email adresses
    
    """
    
    mail_list = []
    
    for i in nested_list:
        mail = i[0][0].lower() + '.' + i[1][:5].lower() + i[2][-2:] + '@aau.dk'
        mail_list.append(mail)
        
    return mail_list


#print(list_mail_parser(names))
    

# Exercise 3 ------------------------------------------------------------------

def adding_odds(range1, range2):
    """
    Function that sums all ods numbers between range 1 and range 2 (both inclusive)
    
    Args:
        range1(int): first range 
        range2(int): second range
    Returns:
        sum of all ods numbers between two ranges
    
    """
    
    some_list = []
    
    for i in range(range1, range2+1):
        if i % 2 == 0:
            some_list.append(i)
            
    return sum(some_list)
    

#print(adding_odds(1,100))


def finding_primes(max_range):
    """
    Function to finding and printing primes between 0 and max_range
    
    Args:
        max_range(int): max range
    Returns:
        None
    
    """
    
    for i in range (1, max_range, 2): #odd numbers can not be primes
            for n in range(2,i):
                if i % n == 0:
                    break
            else:
                print(i)
        
#print(finding_primes(100))

# Exercise 4 ------------------------------------------------------------------

import random

def guessing():
    """
    Function to guessing random number between (1,100)
    
    Args:
        None
    Returns:
        None
    
    """
    number = random.randint(1, 100)
    guess = 0
    attempts = 0
    
    while guess != number and guess != "exit":
        guess = input("What's your guess? \n")
    
        if guess == "exit":
            print("Try next time!")
            break
    
        guess = int(guess)
        attempts += 1
    
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You got it!")
            print("And it only took you", attempts, "tries!")
            
#print(guessing())

# Exercise 5 ------------------------------------------------------------------

import pandas as pd

def detection_xyz(filename):
    """
    Function to check the outlier points in .txt file and return two separate 
    files - first with incorrect dataset, second with correct.
    
    Args:
        filename(file): name of the file/access path
    Returns:
        string information about completing the task
    
    """
    
    
    colnames = ['X','Y','Z']
    dataframe = pd.read_csv(filename, sep=' ', names=colnames)
    
    outlier = (dataframe['Z'] > 80) | (dataframe['Z'] < 75)
    print("You have", outlier['Z'].count(), "outliner points")
    outlier.to_csv("outlier_data.txt", sep=' ', header=False, index=False, float_format='%.3f')
    
    pts = pd.concat([outlier,dataframe]).drop_duplicates(keep=False)
    print("You have", pts['Z'].count(), "correct points")
    pts.to_csv("pts_data.txt", sep=' ', header=False, index=False, float_format='%.3f')
    
    return 'Done!'
    
#print(detection_xyz('Data.txt'))