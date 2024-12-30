 #1
'''for i in range(3,0,-1):
    username=input('enter your valid username: ')
    password=input('enter your valid password: ')
    if username != "Python" or password != "1234":
        if i == 1:
            continue
        print(i - 1, "attempts left")
    else:
        print("logged in successfully")
        break
else: 
    print("You are blocked!!!")

 #2 
for i in range(1,11):
    print("Softwarica")

 #3
a = [1,2,3,4,5]
sum = 0
for i in range(0,len(a)):
    sum = sum + a[i]
print (sum)

 #4
name = "Legend"
for i in range(len(name)):
    print(name[i])

 #5
list = [6, 8, 10, 12]
result = [x * 2 for x in list]
print(result)

 #6
number = 55
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

 #7
list = [99, 67, 99, 78]
print(list[::-1])

 #8
list = [1, 2, 3, 4]
list.append(5)
print(list)

 #9
list = [1, 2, 3, 4]
print(list[0], list[3])

 #10
list = [1, 2, 3, 4]
print(list[0], list[1], list[3])

 #11
list = [1, 2, 3, 4]
list[1:3] = ["a", 2]
print(list)

#12
list = [1, 2, 3, 4, 5]
even_numbers = []
odd_numbers = []
for i in list:
    if i % 2 == 0:
        even_numbers.append(i)  
    else:
        odd_numbers.append(i)  
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#13
list = [1, 2, 3, "d", 4, 5, "a"]
int_type = []
str_type = []
for i in list:
    if isinstance(i,int) :
        int_type.append(i)  
    elif isinstance(i,str):
        str_type.append(i)  
print("Integer dataype elements:", int_type)
print("String datatype elements:", str_type)

#14
list=[1,2,3,4,"a","b"]
int_type = []
str_type = []
for i in list:
    if isinstance(i,int):
        int_type.append(type(i))
    elif isinstance(i,str):
        str_type.append(type(i))
print("Integer dataype elements:", int_type)
print("String datatype elements:", str_type)

 #15
name = "Legend Is Back 445"
letter = sum(c. isalpha() for c in name)
digit = sum(c. isdigit() for c in name)
space = sum(c. isspace() for c in name)
print("Letter:", letter)
print("Digit:", digit)
print("Space:", space)


 #16
username = input("Enter lucisah3@gmaiol.com: ")
password = input("Enter sidhartha3344: ")
if len(username) >= 10 and len(password) >= 8:
    print("Wrong password")
else:
    print("Right password")

 #17
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


 #18
import math 
num = 6
print(math.factorial(num))

 #19
for number in range(1, 9):
    print(f"Multiplication Table of {number}")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
    print()

 #20
list = [1, 2, 3, 4]
print(list[0], list[1],)

 #21
odd_sum = sum(i for i in range(1, 11) if i % 2 != 0)
print(odd_sum)

 #22
even_sum = sum(i for i in range(1, 11) if i % 2 == 0)
print(even_sum)

 #23
string = "I Am Legend"
spaces = string.count(" ")
print(spaces)

 #24
list = [1, 2, 3, 4]
cube = [x ** 3 for x in list]
print(cube)

#25
a = "programming"
print(a[::-1])

 #26
for i in range(50):
    if i > 7:
        break
    print(i, end=" ")

 #27
string = "Sidhartha"
for char in string:
    print(char)

 #28
list = ["ram", "shyam", 1, 2]
for item in list:
    if isinstance(item, str):
        print(f"Hello!{item}")

 #29
a = ["ram", "shyam"]
prefixed = [f"Dr.{x}" for x in list]
print(prefixed)

 #30
list = [4, 6, 8, 10]
square = [x ** 2 for x in list]
print(square)

 #31
list = [111, 32, -9, -45, -17, 9, 85, -10]
positive = [x for x in list if x > 0]
print(positive)'''

#32
list=[0,1,2,3,4,5,6]
new_list = [ ]
for i in list:
    if (i >= 0 and i < 3) or (i > 3 and i < 6):
        new_list.append(i)
print(new_list)


 #33
list = [1, "a", 3.5, True]
type = [type(x) for x in list]
print(type)

 #34
for i in range(3):
    print(i)
else:
    print("Done")

 #35
for i in range(105, 0, -7):
    print(i, end=" ")

#36
bad_chars = [";", ":", "!", "*"]
string = "py;th*on! ;py ,th:o n"
for char in bad_chars:
    string = string.replace(char, "")
print(string.replace(" ", ""))
 
 #37
list = [1, 2, 3, 4, 5]
odd_count = []
even_count = []
for i in list:
    if i % 2 == 0:
        odd_count.append(i)  
    else:
        even_count.append(i)  
print("Odd numbers:", odd_count)
print("Even numbers:", even_count)

#38
sum = 0
for num in range(3,100):
    if num % 3 == 0 or num % 5 == 0:
        sum += num
print("Sum of all multiples of 3 or 5 from range 3 to 99 is: ",sum)


 #39
sum_even = 0
sum_odd = 0
for num in range(1,101):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers from 1 to 100 is: ",sum_even)
print("Sum of odd numbers from 1 to 100 is: ",sum_odd)

 #40
palindrome = input("Enter a number: ")
if palindrome == palindrome[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

 #41
number = int(input("Enter a number: "))

num_str = str(number)
num_digits = len(num_str)

sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

 #42
str = input("Enter a string: ")
vowel = "aeiouAEIOU"
result = " "
for char in str:
    if char not in vowel:
        result += char

print(result)

 #43
number = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i
if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

 #44

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

common_numbers = list(set(a) & set(b))

print("Common numbers:", common_numbers)

 #45
number = int(input("Enter a number: "))
if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")