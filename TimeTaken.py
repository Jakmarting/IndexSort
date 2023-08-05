# Objective - Give user a list of programs in DIR then select one to run, time the run and print back to user#

# imports

import time
from datetime import datetime
import sys
import os



def time_program(other_program):
    
    # Timing the python code
    program_start_time = datetime.now()
    start_time = time.time()

    # Run Other Program here
    exec(open(other_program).read())

    delta_time = time.time() - start_time
    program_end_time = datetime.now()
    program_delta_time = program_end_time - program_start_time

    print(f"\nExecution in {delta_time}s")
    print(f"{program_delta_time}")



def get_runnables():

    arr = os.listdir() # lists all files / directories but we'd prefer just python files
    counter = 0
    
    while (counter < len(arr)):
        # Check if the program is a python file
        if (arr[counter][-3:] != ".py"):
            arr.remove(arr[counter])
            # If the program is not a python file then don't increment counter as the current file has been removed
        else:
            counter += 1
    
    return arr


   

def format_runnables():
    python_programs = get_runnables()

    format_string = ""

    # Gather up the python programs and give them each a number to be selected
    for p in range(len(python_programs)):
        format_string += f"\t[{p}]\r{python_programs[p]}\n"
    
    chosen_program = str(input("[+] Please Enter a program to run or X to end:\n "+format_string))

    invalid = False
    if (chosen_program.isdigit()):
        if (not (0 < int(chosen_program) < len(python_programs))):
            invalid = True
    else:
        invalid = True
    
    # Check for valid input
    while (invalid):
        print("Invalid Input")
        chosen_program = str(input("[+] Please Enter a program to run:\n "+format_string))
        
        if (chosen_program == "X"):
            exit(0)

        invalid = False
        
        if (chosen_program.isdigit()):
            if (not (0 < int(chosen_program) < len(python_programs))):
                invalid = True
        else:
            invalid = True
    
    time_program(python_programs[int(chosen_program)])



if __name__ == "__main__":
    
    format_runnables()
    
    # time_program(sys.argv[1])

# run the program with the format python TimeTaken.py (OtherProgramNameHere).py for this commented out approach
