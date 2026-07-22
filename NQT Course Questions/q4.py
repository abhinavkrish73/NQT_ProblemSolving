n = int(input())
sales={}
totalrev=0
maxrev=""
maxval = 0
for _ in range(n) :
    name,qty,price = input().split()
    qty = int(qty)
    price = int(price)
    rev = price * qty
    sales[name]=rev
    totalrev+=rev
for key in sales :
    if sales[key] > maxval :
        maxval = sales[key]
        maxrev = key
print("Most Sold Item : ",maxrev)
print("Total Revenue : ",totalrev)
print("Average Revnue Per Entry : ",totalrev/2)
