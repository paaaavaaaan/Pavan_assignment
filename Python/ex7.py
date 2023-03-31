n = input("Enter a list of numbers: ").split()
#Use lambda function and list comprehension to filter out even numbers and double odd numbers
result = [(lambda x: x*1)(int(num)) for num in n if int(num)%2!=0]
print(result)
