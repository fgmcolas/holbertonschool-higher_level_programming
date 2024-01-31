#!/usr/bin/python3

def uniq_add(my_list=[]):
    set_list = set(my_list)
    result = 0
    for element in set_list:
        result += element
    return result
