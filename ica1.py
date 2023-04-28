name = input("Enter name :")
sex = input("Enter sex :")
year = int(input("Enter year :"))

if (year <= 1940):
    if(sex == "m"):
        print("Sir, you are ",(2021-year),", and were 100 in ", (year+100))
    elif (sex == "f"):
        print("Madam, you are ",(2021-year),", and were 100 in ", (year+100))
else:
    if (sex == "m"):
        print("Hi ",name,", you are ",(2021-year),", and will be 100 in ",(year+100))
    elif (sex == "f"):
        print("Hello ",name," you are ",(2021-year),", and will be 100 in", (year+100))
        
