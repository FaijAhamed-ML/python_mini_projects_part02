

num1= float(input("Enter the first number : "))
num2= float(input("Enetr the second number : "))

print("+-----------------Comparision Reslts----------------------+")

if num1 == num2:
    print(f"Both numbers are equal: {num1}")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2 :
    print(f"{num1} is less than {num2}")
    
    
if num1 ==0 or num2 == 0:
    print("\nAt least one number is zero.")
else :
    print("\nBoth numbers are non-zero.")
    
