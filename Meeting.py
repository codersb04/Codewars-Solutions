"""
DESCRIPTION:
John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
"""

def meeting(s):
    # your code
    new_s=s.upper()
    friend=new_s.split(";")
    new_lst=[]
    for i in friend:
        item=i.split(":")
        new_lst.append(item)
    new_lst.sort()
    new_lst.sort(key=lambda x:x[1])
    final=""
    for i in new_lst:
        final+="("+i[1]+", "+i[0]+")"
    return final