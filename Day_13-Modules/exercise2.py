
"""
Flatten the following list of lists of lists to one dimensional list:
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

def flatten_list_of_list_of_list(lists):
    return [number for outerList in lists for rows in outerList for number in rows]

print(flatten_list_of_list_of_list(list_of_lists))