# converter with an input

# def converter(celsius):
#     temp = (celsius *9/5) +32
#     msg_1 = " degrees Celsius is " 
#     msg_2 =   " degrees Farenheit."
#     return str(celsius) + msg_1 + str(temp) + msg_2

# cel= input("Enter a tempature in degrees Celsius: ")
# result = converter(float(cel))
# print(result)

# user_input = input("Enter a first number: ")
# user_input_2 = input("Enter a secound number: ")
# result = int(user_input)-int(user_input_2)

# if result>10:
#     print("result bigger than 10")
# elif 10>result>0:
#     print("result bigger than 0 but not 10")
# elif result == 0:
#     print("result equal zero")
# else:
#     print("result is negative")
    

## And exercice

# input1 = input("Enter a first nuber: ")
# input2 = input("Enter a secound nuber: ")

# if int(input1) > 10 and int(input2) > 10:
#     print("Both numbers are greater than 10")
# else:
#     print(" At least one of the numbers is not greater than 10")

# weather = input("What is the weather Today? It is: ")
# heat = input("How warm is it today? It is: ")

# if weather == "Raining" and heat =="Cold":
#     print("Take an umbrella and a warm jacket")
# elif weather == "Raining" and heat == "Warm":
#     print("Take an umbrella and a tshirt")
# elif weather == "Sunny" and heat == "Cold":
#     print("Take an sunglasses and a warm jacket")
# elif weather == "Sunny" and heat == "Warm":
#     print("Take an sunglasses and a tshirt")
# else:
#     print("Stay Home!!")


# def play():
#     number = input("Give me a number between 1 and 20: ")
#     color = input("Give me a color: ")

#     if int(number) == 12 and color == "Blue":
#         print("You've found both the secret number and color") 
#     elif int(number) == 12 or color == "Blue":
#         print("you found at least one")
#     else:
#         print("Found none")
#     print("Try again")

# play()


# def greet(name, age):
#     message = "Your name is" + name + " and you are " + age + " years old."
#     return message

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(greet(name, age))

# def add(a, b):
#     return int(a) + int(b)

# def subtract(a, b):
#     return int(a) - int(b)

# num_one = input("Enter a number: ")
# num_two = input("Enter another number: ")

# message = "The result of " + str(num_one) + " + " + str(num_two) + " is " + str(add(num_one, num_two))
# print(message)

# message = "The result of " + str(num_two) + " - " + str(num_one) + " is " + str(subtract(num_one, num_two))
# print(message)

def get_result(answer):
    if answer == "a":
        return True
    else:
        return False

print("Do you like programing?")
print("a. Yes")
print("b. No")
result = input("Enter a or b: ")

if get_result(result):
    print("Awesome! Programming is really fun!")
else:
    print("Hang in there! It's an acquired taste!")

print("Hello")
