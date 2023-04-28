x = int(input("Enter first num = "))
y = int(input("Enter second num = "))
mini = 0
maxi = 0
if(x < y):
    mini = x
else:
    mini = y

i = mini
while i >= 2:
    if (x%i==0 and y%i==0 ):
        maxi = i
        break
    i=i-1
print(i)
