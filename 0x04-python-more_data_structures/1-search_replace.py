#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy.append(replace)
        else:
            copy.append(my_list[i])
    return copy
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security

