maximum_order = 100
minimum_order = 1
price = 7.99
def Cheese_Order():
    order_amount = float(input ("what is your cheese order weight: "))
    if order_amount < minimum_order:
        print("cheese order weight is under minimum order amount")
    elif order_amount > maximum_order:
        print("cheese order weight is over maximum order amount")
    else:
        print("cheese order weight is within maximum and minimum, the price is", order_amount*price)
