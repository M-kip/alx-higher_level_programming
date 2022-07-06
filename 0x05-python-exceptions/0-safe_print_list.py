#!/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        for num in range(x):
            print(my_list[num])
    except AttributeError as error:
        print(error)
