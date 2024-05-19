"""
DESCRIPTION:
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
"""

def multiplication_table(size):
    arr=[]
    for i in range(1,size+1):
        arr.append([num*i for num in range(1,size+1)])
    return arr
        