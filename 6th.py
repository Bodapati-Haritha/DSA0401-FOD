import numpy as np
cost=np.array([10,20,30,40,50,60,70,80,90,100])
qu=np.array([2,3,2,5,3,2,1,4,3,2])
dis=5
tax=8
for i in range(len(cost)):
    tot=cost*qu
    tot1=tot-tot*(dis/100)
    tot2=tot1+tot1*(tax/100)
    total=sum(tot2)
print("total purchased amount after discount and tax added :",total)

import numpy as np
item_prices = []
item_size = int(input("Enter the size of the item:"))
for i in range(0,item_size):
    a = int(input("Enter the item price:"))
    item_prices.append(a)
quantities = []
quantities_size = int(input("Enter the size for quantities:"))
for i in range(0,quantities_size):
    b = int(input("Enter the quantities data:"))
    quantities.append(b)        
discount_rate = int(input("Enter the discount rate:"))                 
tax_rate = int(input("Enter the tax_rate:"))                      
subtotal = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))
discount_amount = subtotal * (discount_rate / 100)
total_after_discount = subtotal - discount_amount
tax_amount = total_after_discount * (tax_rate / 100)
final_total_cost = total_after_discount + tax_amount
print("Total cost for the customer's purchase: {:.2f}".format(final_total_cost))
