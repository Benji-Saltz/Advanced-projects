#########################################
# Programmer: Mrs. G
# Date: 04.05.2014
# File Name: search_template.py
# Description: This is a template to write 4 search functions.
#              The examples in the docstring demonstrate how these functions should work.
#########################################

##def linear_search_1(lst, value):
##    """(list, object) -> int
##
##    Return the index of the first occurrence of value in lst, or return
##    -1 if value is not in lst.
##
##    >>> linear_search_1([2, 5, 1, -3], 5)
##    1
##    >>> linear_search_1([2, 4, 2], 2)
##    0
##    >>> linear_search_1([2, 5, 1, -3], 4)
##    -1
##    >>> linear_search_1([], 5)
##    -1
##    """
##    # write your code here
##    pass
###################################################################################
##def linear_search_2(lst, value):
##    """(list, object) -> int
##
##    Return the index of the first occurrence of value in lst, or return
##    -1 if value is not in lst.
##
##    >>> linear_search_2([2, 5, 1, -3], 5)
##    1
##    >>> linear_search_2([2, 4, 2], 2)
##    0
##    >>> linear_search_2([2, 5, 1, -3], 4)
##    -1
##    >>> linear_search_2([], 5)
##    -1
##    """
##    # write your code here
##    pass
###################################################################################
##def linear_search_3(lst, value):
##    """(list, object) -> int
##
##    Return the index of the first occurrence of value in lst, or return
##    -1 if value is not in lst.
##
##    >>> linear_search_3([2, 5, 1, -3], 5)
##    1
##    >>> linear_search_3([2, 4, 2], 2)
##    0
##    >>> linear_search_3([2, 5, 1, -3], 4)
##    -1
##    >>> linear_search_3([], 5)
##    -1
##    """
##    # write your code here
##    pass
#################################################################################
def binary_search_recursive(lst, value, left=0, right=1):
    """(list, object, int, int) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> binary_search_recursive([2,4,6],2,0,2)
    0
    >>> binary_search_recursive([2,4,6],4,0,2)
    1
    >>> binary_search_recursive([-3,1,2,5],5,0,3)
    3
    >>> binary_search_recursive([3,5,7],1,0,2)
    -1
    >>> binary_search_recursive([3,5,7],9,0,2)
    -1
    >>> binary_search_recursive([-3,1,2,5],4,0,3)
    -1
    >>> binary_search_recursive([],5,0,-1)
    -1
    >>> binary_search_recursive([2],2,0,0)
    0
    >>> binary_search_recursive([2,2,4],2,0,2)
    0
    """
    if len(lst) == 0:
        return -1
    if right < left:
        return -1
    middle = (left+right)//2
    if lst[middle] == value:
        if middle > 0:
            if lst[middle-1] == value:
                return binary_search_recursive(lst, value, left, middle-1)
        return middle
    elif lst[middle] > value:
        return binary_search_recursive(lst, value, left, middle-1)
    else:
        return binary_search_recursive(lst, value, middle+1, right)

#################################################################################
def binary_search_iterative(lst, value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> binary_search_iterative([-3, 1, 2, 5], 5)
    3
    >>> binary_search_iterative([2, 2, 4], 2)
    0
    >>> binary_search_iterative([-3, 1, 2, 5], 4)
    -1
    >>> binary_search_iterative([], 5)
    -1
    """
    left = 0
    right = len(lst)
    while left <= right and len(lst) != 0:
        middle = (left+right)//2
        if lst[middle] == value:
            if middle > 0:
                if lst[middle-1] == value:
                    right = middle-1
            if right != (middle-1):
                return middle
        elif lst[middle] > value:
            right = middle-1
        else:
            left = middle+1
    return -1
#################################################################################
if __name__ == '__main__':
    import doctest
    doctest.testmod()
lst  = [1,8,9,11,15,5]
value = 2
left = 0
right = 2
print("List for all searches:",lst)
print("Value for all searches:",value)
print()
print("left value for recursive search:",left)
print("right value for recursive search:",right)
print("Recursive binary search output:",binary_search_recursive(lst, value,0,3))
lst  = [2,2,4]
value = 2
print("Iterative binary search output:",binary_search_iterative(lst, value))
