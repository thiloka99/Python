price = float(input("Enter your price = "))
x = price%5
if x<2.5 :
    price = price - x
    print(price)
else :
    price = price +(5-x)
    print(price)
