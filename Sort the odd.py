"""
DESCRIPTION:
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def sort_array(source_array):
    # Return a sorted array.
    arr=[]
    for i in source_array:
        if i%2!=0:
            arr.append(i)
    s_arr=sorted(arr)
    a=0
    new=[]
    for i in source_array:
        if i%2!=0: 
            i=s_arr[a]
            a=a+1
            new.append(i)
        else:
            new.append(i)
    return new