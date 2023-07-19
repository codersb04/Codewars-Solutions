"""
DESCRIPTION:
Let us begin with an example:

A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000. He wants to keep his old car until he can buy the secondhand one.

He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per month. Furthermore this percent of loss increases of 0.5 percent at the end of every two months. Our man finds it difficult to make all these calculations.

Can you help him?

How many months will it take him to save up enough money to buy the car he wants, and how much money will he have left over?

Parameters and return of function:

parameter (positive int or float, guaranteed) start_price_old (Old car price)
parameter (positive int or float, guaranteed) start_price_new (New car price)
parameter (positive int or float, guaranteed) saving_per_month 
parameter (positive float or int, guaranteed) percent_loss_by_month

nbMonths(2000, 8000, 1000, 1.5) should return [6, 766] or (6, 766)

"""

def nbMonths(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    month = 1
    saving=0
    while start_price_old < start_price_new:
        if month%2==0:
            percent_loss_by_month+=0.5
        start_price_old-=(start_price_old*(percent_loss_by_month/100))
        start_price_new-=(start_price_new*(percent_loss_by_month/100))
        money_left=(saving+saving_per_month)-(start_price_new-start_price_old)
        saving+=saving_per_month
        if money_left > 0:
            return [month,round(money_left)]
        month+=1
    else:
        return [0,start_price_old-start_price_new]