#!/usr/bin/python3
def uniq_add(my_list=[]):
    final_list = []
    res = 0

    for i in my_list:
        if i not in final_list:
            final_list.append(i)
    for unique in final_list:
        res += unique
    return res
