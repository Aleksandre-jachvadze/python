#დაწერეთ პროგრამა რომელიც ტერმინალში გამოიტანს შემდეგ სიტყვებს Hello World#
print("Hello World")
#შექმენით პროგრამა რომელიც გკითხავთ "რა გქვია?", დაელოდება თქვენს პასუხს და გიპახუსებთ "გამარჯობა, თქვენი სახელი"
name = input("What is your name? ")
greeting = "Hello, " + name + ", nice to meet you!"
print(greeting)
#შექმენით პროგრამა რომელიც დათვლის სიმბოლოების რაოდენობას მომხმარებლის მიერ შეყვანილ ტექსტში.
user_input = input("what is the input string")
char_count = len(user_input)
print(f"{user_input} has {char_count} characters.")
#დაწერეთ პროგრამა რომელიც მომხმარებლისგან მიიღებს ორ რიცხვს და შემდგომ ტერმინალში გამობეჭდავს ამ
#რიცხვების ჯამს, სხვაობას, ნამრავლს და განაყოფს.
num1 = int(input("first Num:"))
num2 = int(input("Second Num"))
print(f"Sum: {num1 + num2}\nDifference: {num1 - num2}\nProduct: {num1 * num2}\nQuotient: {num1 / num2}")
#შექმენით პროგრამა სადაც მომხმარებელი შეძლებს შემოიტანოს რაიმე ციტატა ტექსტის სახით და შემდეგ შემოიტანოს ამ ციტატის ავტორის სახელი. თქვენმა პროგრამამ უნდა დააბრუნოს ტექსტი სადაც იქნება ავტორის სახელი და ასევე ციტატა ოღონდ “ ან ‘ ბრჭყალებში
qoute = input("what is the qoute?")
author = input("who said it?")
print(author + " says, '" + quote + "'")
#დაწერეთ პროგრამა სადაც მომხმარებელი შემოიყვანს რაიმე ტექსტს და თუ ეს ტექსტი არს მაღალი რეგისტრის ასოებით, პროგრამამ უნდა გამობეჭდოს იგივე ტექსტი მაგრამ ყველა ასო უნდა იყოს დაბალი რეგისტრის.
user_input = input("Enter a text: ")

if user_input.isupper():
    print(user_input.lower())
#დაწერეთ პროგრამა სადაც მომხმარებელი შემოიყვანს რაიმე ტექსტს და თუ ამ ტექსტში არის :) ან/და :(, ყველა ასეთი ჩანაწერი უნდა შეიცვალოს 🙂 ან 🙁 ემოჯით
user_input = input("Enter a text: ")
modified_text = user_input.replace(":)", "🙂").replace(":(", "🙁")
print(modified_text)
#დაწერეთ პროგრამა სადაც მომხმარებელი შემოიყვანს რაიმე რიცხვს და ეინშტეინის ფორმულის E=mc2 მეშვეობით გამოთვალეთ ენერგია. მოცემულ ფორმულაში c არის სინათლის იჩქარე რომელიც დაახლოებით 300000000
c = 300000000
m = float (input("Enter mass (in kilograms): "))
E = m * c * c
print("The energy is", E, "joules.")
