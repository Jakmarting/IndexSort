"""
Plans for sorting algorithm:
should be able to specify data type for data list
import / export data shouldshow text files only
"""

import random
from os import walk
import os

def Convert_String_To_Num(string):

    integer = 0
    
    for l in range(len(string)):
        integer += ((ord(string[(len(string)-1)-l])-ord('a')) * (26 ** l))

    return integer

def Convert_Num_To_String(integer):
    string = ""

    i = integer

    alpha_len = 1
    a = 0
    
    # nearest power of 26 to the integer?
    while integer > alpha_len:
        alpha_len *= 26
        a += 1
    
    while a >= 0:
        if (i > (26**a)):
            c = i // (26 ** a)
            string += chr(c + ord('a'))
            i -= c * (26 ** a)
        a -= 1

    return string

def IndexSort(data_list):

    largest = max(data_list)
    
    sort_list = [None] * (largest+1)    

    for d in range(len(data_list)):
        sort_list[data_list[d]] = data_list[d]

    sort = True
    c = 0
    while sort:
        if sort_list[c] == None:
            del sort_list[c]
        else:
            c += 1

        if (c >= len(sort_list)):
            sort = False       
    
    return sort_list


def IndexSortFilter(data_list):

    if len(data_list) <= 0:
        return
    
    elif type(data_list[0]) == "<class 'str'>":
        str_to_int_list = []
        for string in data_list:
            str_to_int_list.append(Convert_String_To_Num(string))
        sorted_list = IndexSort(str_to_int_list)
        int_to_string = []
        for integer in sorted_list:
            int_to_string.append(Convert_Num_To_String(integer))
        return int_to_string
    else:
        minimum = 0

        for n in data_list:
            if n < minimum:
                minimum = n

        if minimum < 0:
            offset_list = []
            for data in data_list:
                offset_list.append(data-minimum)
            sorted_neg_list = IndexSort(offset_list)
            
            for n in range(len(sorted_neg_list)):
                sorted_neg_list[n] += minimum
                
            return sorted_neg_list
        else:
            return IndexSort(data_list)


def create_menu(func_list):

    user_input_menu = ""
    
    for i in range(len(menu_list)):
        user_input_menu += f"{i+1}:\t{menu_list[i]}\n"

    userI = str(input(user_input_menu))

    if userI.isdigit():

        input_int = int(userI)-1

        if input_int < len(func_list):
        
            eval(func_list(input_int))

def GetFiles(mypath):
    filenames = next(walk(mypath), (None, None, []))[2]
    return filenames
        
def menu():

    data = []
    data_type = "int"
    max_val = 1000
    
    userI = ""
    stay_in_loop = True

    menu_funcs = []
    
    # Menu: 1. 2. 3. 4. 5.
    # importing/exporting file, setting data type
    
    while stay_in_loop:

        userI = str(input(f"Data:\t{data}\n1.Sort Data\n2.Populate Data.\n3.Sort Settings\n4.File Import\\Export\n5.Exit\n"))

        if userI == "1":
            print(f"Sorted Data:\t{IndexSortFilter(data)}\n")
            
        elif userI == "2":

            num = int(input("How much data should be added:\t"))

            for i in range(num):
                data.append(random.randint(0,max_val))
        elif userI == "3":
            max_val = int(input(f"Enter new max value(Old value {max_val}):\t"))
        elif userI == "4":
            print(GetFiles(os.getcwd()))
        elif userI == "5":
            stay_in_loop = False
menu()
        
