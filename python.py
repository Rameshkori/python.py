# name = "Ramesh"
# age = 25
# salary = 50000.50
# print ("salary")

# age = 12
# if age >= 18:
#     print("Adult")
# elif age < 18:
#     print("Minor")
# else:
#     print("Invalid")

# for i in range(1,50):
#     print(i)


# Initialization
# i = 1 
# while i <= 15:
#     print(i)
#     i = i + 1

# for i in range(5):
#     if i == 2:
#         break
#     print(i)
    
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# sum value of 2 numbers
# a = 10
# b = 20
# print(a + b)

# Facorial of a number
# n = 10
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

# polindrome
# s = "madAm"
# print(s.lower() == s.lower()[::-1])  # True

# sam as polindrome but with case sensitivity
# s = "madam"
# print(s == s[::-1])
# reverse_string = s[::-1]
# print("Reversed string:", reverse_string)


# print("Python3 is working")

        
# multiply 3 numbers
# a = 2
# b = 3
# c = 4
# print(a * b * c)

# factorial of a number
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

# Swap two numbers
# a, b = 5, 10
# a, b = b, a
# print(a, b)

# Find largest of two numbers
# a,b = 10, 20
# print("Largest number is:", max(a,b))

# Even or Odd
# n = 121
# print("Even" if n % 2 ==0 else "Odd")
# print(n, "is", "Even number" if n % 2 ==0 else "Odd number")

# Sum of first N numbers
# n = 5
# print(sum(range(1, n+1)))

# prime number check
# n = 28
# for i in range(2,n):
#     if n % i == 0:
#         print(n, "is not a prime number")
#         break
# else:
#     print(n, "is a prime number")
    
    
    
    
# df = pd.read_csv("../input/data.csv")

# import pandas as pd

# df = pd.read_csv("../input/data.csv")

# print(df.head())
# print(df.info())

import json


# Your Python data (can come from API, ETL, dataframe, etc.)
data = {
    "project": "Insurance Claims1",
    "platform": "AWS Databricks",
    "language": "PySpark",
    "experience": 3.8
}
# data =
# {
#   "name": "Ramesh",
#   "role": "AWS Data Engineer"
# }


# Write to JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)
    
#     with open("/path/to/ram.json") as f:
#         data = json.load(f)
# print(data)

import json

with open("ram.json", "r") as f:
    data = json.load(f)

print(data)


