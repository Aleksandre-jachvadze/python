print("Hello World")

name = input("What is your name? ")
greeting = "Hello, " + name + ", nice to meet you!"
print(greeting)

text = input()
print(len(text))

quote = input("What is the quote? ")
author = input("Who said it? ")
print(author + " says, \"" + quote + "\"")

length = float(input("What is the length of the room in feet? "))
width = float(input("What is the width of the room in feet? "))

area_feet = length * width
area_meters = area_feet * 0.092903

print(f"You entered dimensions of {length} feet by {width} feet.")
print("The area is")
print(f"{area_feet} square feet")
print(f"{area_meters} square meters")
