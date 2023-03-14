#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [4,6,7,9,1]
idx = 2
element = 22
new_list = replace_in_list(my_list,idx,element)
print(new_list)
print(my_list)
