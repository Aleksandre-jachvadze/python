 #დაწერეთ პროგრამა სადაც მომხმარებელი შემოიტანს ტექსტს "camelCase" პრინციპით, თქვენმა პროგრამამ იგივე ტექსტი უნდა დააბრუნოს "snake_case" პრინციპით.
import re

def camel_to_snake(text):
    if not re.match(r'^[a-z]+[A-Z][a-zA-Z]*$', text):
        return text
    
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()

user_input = input("camelCase: ")
print("camel_case:", camel_to_snake(user_input))

#წარმოიდგინეთ აპარატის რომელიც ყიდის კოკაკოლას, კოკაკოლის ბოთლი ღირს 50 ცენტი, აპარატს შეუძლია მიიღოს მხოლოდ 25,10,5 ცენტიანი მონეტები.

#დაწერეთ პროგრამა სადაც იმიტაცია იქნება იმ პროცესის როცა აპარატში ვათავსებთ სხვადასხვა ტიპის მონეტებს და გვსურს რომ ვიყიდოთ კოკაკოლა. გაითვალისწინეთ რომ თუ 50 ცენტს გასცდა პროგრამამ დასრულებისას უნდა დააბრუნოს ის ხურდის რაოდენობა რაც ზედმეტად გადახდა მოხდა

#ასევე გაითვალისწინეთ რომ თუ მომხმარებელმა მიუთითა არარსებული მონეტა თავიდან უნდა მოხდეს კითვის დასმა
import os 
def get_coin();
     while True:
        try:
            coin = int(input("Insert Coin: "))
            if coin in [25, 10, 5]:
                return coin
            else:
                print("Invalid coin. Please insert 25, 10, or 5 cents.")
        except ValueError:
            print("Invalid input. Please insert a valid coin.")

def vending_machine():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        amount_due -= get_coin()
    
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    vending_machine()

#დაწერეთ პროგრამა სადაც მომხმარებელი შემოიყვანს ტექსტს, პროგრამამ უნდა დააბრუნოს იგივე ტექსტი ოღონდ ხმოვნების გარეშე. გაითვალისწინეთ რომ მომხმარებელმა შეიძლება შემოიყვანოს როგორც დაბალი ასევე მაღალი რეგისტრის ასოები.
def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return "".join(char for char in text if char not in vowels)

def main():
    user_input = input("Input: ")
    print("Output:", remove_vowels(user_input))

if __name__ == "__main__":
    main()

#დაწერეთ პროგრამა სადაც მომხარებელი შემოიყვანს ტექსტს. თქვენმა პროგრამამ უნდა შეამოწმოს ეს ტექსტი და თუ აკმაყოფილებს ყველა მოთხოვნებს მაშინ გამოპრინტეთ "Valid" სხვა შემთხვევაში "Invalid".

#მოთხოვნები რომლელსაც მომხარებლის ტექსტი უნდა აკმაყოფილებდეს:
#ტექსტის სიგრძე უნდა იყოს მინიმუმ 2 მაქსიმუმ 6 სიმბოლო
#ტექსტის პირველი 2 სიმბოლო აუცილებლად უნდა იყოს ასობგერა
#ტექსტი არ უნდა შეიცავდეს არცერთ პუნქტუაციის ნიშანს
#თუ ტექსტში არის ციფრები პირველი ციფრი არ უნდა იყოს "0"
#თუ ტექსტში არის ციფრები ციფრის მერე არ უნდა იყოს ასობგერა

def main():
    plate = input("plate: ")
     if is_valid(plate):
        print("Valid")
    else:
     print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if any(char in "!@#$%^&*()-_=+[]{}|;:'",.<>?/" for char in s):
        return False
    digits_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not digits_started and char == "0":
                return False
            digits_started = True
        elif digits_started:
            return False
    return True

main()

#აქ მოცემული გვაქვს გარკვეული ხილის ჩამონათვალი და კალორიულობა (იხ. პირველი სვეტი)

#დაწერეთ პროგრამა სადაც მომხამრებელი შემოიყვანს ხილის დასახელებას და თქვენმა პროგრამამ უნდა დააბრუნოს ამ ხილის კალორიულობა.

#გაითვალისწინეთ ის რომ მომხარებელმა შეიძლება შემოიყვანოს მაღალი ან/და დაბალი რეგისტრის ხილის დასახელებები. თუ ხილის დასახელება არ არის სიაში მაშინ არაფერი არ უნდა დააბრუნოს თქვენმა პროგრამამ

#მინიშნება: შექმენით თქვენს პროგრამაში ხილის ჩამონათვალის და კალორიულობის ლექსიკონი
 
 def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime" :20,
        "nectarine":60,
        "orange": 80,
        "peach":60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }
    fruit = input("Fruit: ").strip().lower()
    if fruit in fruits:
        print("Calories:", fruits[fruit])

main()
 
 #შექმენით პროგრამა, რომელიც მომხმარებელს 5-ჯერ ეკითხება რიცხვის input-ს, შემდეგ კი ამ რიცხვების ჯამი გამოაქვს პასუხად.
def main():
    total = 0
    for _ in range(5):
        num = int(input("Enter a number: "))
        total += num
    print("The total is", total)

main()
 
 #ფინანსებში 'Rule 72' არის ფორმულა, რომლითაც ინვესტორები ითვლიან თავიანთი ინვესტიიცის გაორმაგების ვადას. ანუ იმას, თუ რამდენ წელში გაორმაგდება მათი ინვესტიცია. ეს ფორმულა ასე გამოიყურება years = 72/r სადაც r არის საპროცენტო განაკვეთი.

#დაწერეთ პროგრამა სადაც მომხარებელი შემოიყვანს რიცხვს და ამ ფორმულის მეშვეობით მიიღებთ შესაბამის შედეგს. მაგალითად
r = float(input())
years = 72 / r
print(years)
#შექმენით პატარა ლისტი, სადაც შეინახავთ კომპანიაში მომუშავეთა სახელებსა და გვარებს. როცა კოდს გაუშვებთ, ლისტიდან თითიოეული მონაცემი უნდა იბეჭდებოდეს ისე, როგორც მაგალითშია ნაჩვენები. შემდეგ შეეკითხეთ მომხმარებელს, თუ რომელი თანამშრომლის ამოშლა უნდა ამ სიიდან, რის შემდეგაც ეს თანამშრომელი ამოშალეთ და მომუშავეთა სია თავიდან გამოიტანეთ
employees = [
    "John Smith",
    "Jackie Jackson",
    "Chris Jones",
    "Amanda Cullen",
    "Jeremy Goodwin"
]

print(f"There are {len(employees)} employees:")
for employee in employees:
    print(employee)

employee_to_remove = input("\nEnter an employee name to remove: ")

if employee_to_remove in employees:
    employees.remove(employee_to_remove)
    print(f"\n{employee_to_remove} has been removed.")
else:
    print("\nEmployee not found!")

print(f"\nThere are {len(employees)} employees:")
for employee in employees:
    print(employee)

#შექმენით პროგრამა, რომელიც მომხმარებელს შეეკითხება რიცხვებს (საიტებიდან კავშირის გაგზავნა-დაბრუნების დროებს). პროგრამა იქამდე უნდა ეკითხეობდეს მომხმარებელს რიცხვებს, სანამ იგი "done"-ს არ ჩაწერს. ამის შემდეგ პროგრამამ უნდა დაითვალოს შეყვანილი რიცხვებიდან: საშუალო არითმეტიკული, უმცირესი და უდიდეს

def get_numbers():
    numbers =[]
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")
    return numbers

def compute_average(numbers):
    return sum(numbers) / len(numbers)

def compute_minimum(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

def compute_maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def main():
    numbers = get_numbers()
    if numbers:
        print(f"Numbers: {', '.join(map(str, numbers))}")
        print(f"The average is {compute_average(numbers)}.")
        print(f"The minimum is {compute_minimum(numbers)}.")
        print(f"The maximum is {compute_maximum(numbers)}.")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()

#შექმენით პროგრამა, რომელიც მომხმარებელს ეკითხება რიცხვების სიას, რომელიც გამოყოფილია სფეისებით. (იხილეთ მაგალითი) შემდეგ კი გამოიტანეთ იგივე ფორმატით მხოლოდ ლუწი რიცხვები.
def get_numbers():
    user_input =("Enter a list of numbers, separated by spaces")
    numbers = user_input.split()
    return[int(number)for number in numbers]
  
  def filter_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def main():
    numbers = get_numbers()
    even_numbers = filter_even_numbers(numbers)
    print(f"The even numbers are {' '.join(map(str, even_numbers))}.")

if __name__ == "__main__":
    main()

 #შექმენით პროგრამა, რომელიც მომხმარებელს ეკითხება რიცხვების სიას, რომელიც გამოყოფილია სფეისებით. (იხილეთ მაგალითი) შემდეგ კი გამოიტანეთ იგივე ფორმატით მხოლოდ ლუწი რიცხვები.
 def get_numbers():
    user_input = input("Enter a list of numbers, separated by spaces: ")
    numbers = user_input.split()
    return [int(number) for number in numbers]

def filter_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def main():
    numbers = get_numbers()
    even_numbers = filter_even_numbers(numbers)
    print(f"The even numbers are {' '.join(map(str, even_numbers))}.")

if __name__ == "__main__":
    main()

#მოცემულია შემდეგი ცხრილი (იხილეთ მიმაგრებული სტრუქტურა ცვლადით PEOPLE):

#შექმენით პროგრამა, რომელიც ამ ცხრილის ყველა თანამშრომელს გვარების მიხედვით დაასორტირებს. შემდეგ კი მაგალითში ნაჩვენები სახით გამოიტანს.

#საბოლოო შედეგში სია ამ თანმიმდევრობით უნდა იყოს:

from tabulate import tabulate

PEOPLE = [
    {"First Name": "Jake", "Last Name": "Jacobson", "Position": "Programmer", "Separation Date": ""},
    {"First Name": "Tou", "Last Name": "Xiong", "Position": "Software Engineer", "Separation Date": "2016-10-05"},
    {"First Name": "John", "Last Name": "Johnson", "Position": "Manager", "Separation Date": "2016-12-31"},
    {"First Name": "Michaela", "Last Name": "Michaelson", "Position": "District Manager", "Separation Date": "2015-12-19"},
    {"First Name": "Sally", "Last Name": "Weber", "Position": "Web Developer", "Separation Date": "2015-12-18"},
    {"First Name": "Jacquelyn", "Last Name": "Jackson", "Position": "DBA", "Separation Date": ""},
]

def sort_people_by_lastname(people):
    return sorted(people, key=lambda x: x["Last Name"])

def format_people_table(people):
    headers = ["Name", "Position", "Separation Date"]
    table_data = [[f'{p["First Name"]} {p["Last Name"]}', p["Position"], p["Separation Date"]] for p in people]
    return tabulate(table_data, headers=headers, tablefmt="grid")

def main():
    sorted_people = sort_people_by_lastname(PEOPLE)
    print(format_people_table(sorted_people))

if __name__ == "__main__":
    main()

#- პროექტი 50 - Filtering Records
from tabulate import tabulate

PEOPLE = [
    {"First Name": "Jake", "Last Name": "Jacobson", "Position": "Programmer", "Separation Date": ""},
    {"First Name": "Tou", "Last Name": "Xiong", "Position": "Software Engineer", "Separation Date": "2016-10-05"},
    {"First Name": "John", "Last Name": "Johnson", "Position": "Manager", "Separation Date": "2016-12-31"},
    {"First Name": "Michaela", "Last Name": "Michaelson", "Position": "District Manager", "Separation Date": "2015-12-19"},
    {"First Name": "Sally", "Last Name": "Weber", "Position": "Web Developer", "Separation Date": "2015-12-18"},
    {"First Name": "Jacquelyn", "Last Name": "Jackson", "Position": "DBA", "Separation Date": ""},
]

def search_employee(name, people):
    return [p for p in people if p["First Name"].lower() == name.lower()]

def format_people_table(people):
    headers = ["Name", "Position", "Separation Date"]
    table_data = [[f'{p["First Name"]} {p["Last Name"]}', p["Position"], p["Separation Date"]] for p in people]
    return tabulate(table_data, headers=headers, tablefmt="grid")

def main():
    search_name = input("Enter a search string: ").strip()
    results = search_employee(search_name, PEOPLE)

    if results:
        print("\nResults:\n")
        print(format_people_table(results))
    else:
        print(f"\nNo employee found with the name '{search_name}'.")

if __name__ == "__main__":
    main()
#დაწერეთ მარტივი გამოკითხვის პროგრამა სადაც მომხმარებელს დაუსმევთ 5 კითხვას, რომელზეც მომხარებელმა უნდა უპასუხოს yes/no.
def ask_question(question):
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    questions = [
        "Do you like Python?",
        "Do you enjoy coding?",
        "Are you a student?",
        "Do you work remotely?",
        "Is this survey helpful?"
    ]

    yes_count = 0
    no_count = 0

    for question in questions:
        answer = ask_question(question)
        if answer == "yes":
            yes_count += 1
        else:
            no_count += 1

    print(f"\nSummary: {yes_count} yes, {no_count} no")

if __name__ == "__main__":
    main()

#- პროექტი 53 - Budget Planer
def get_expenses():
    expenses = {}
    while True:
        name = input("Expense name (type 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        while True:
            try:
                value = float(input(f"Expense value for {name}: $").strip())
                if value < 0:
                    print("Expense value cannot be negative. Try again.")
                    continue
                expenses[name] = value
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return expenses

def get_income():
    while True:
        try:
            income = float(input("Enter your total monthly income: $").strip())
            if income < 0:
                print("Income cannot be negative. Try again.")
                continue
            return income
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_savings_amount(remaining_balance):
    while True:
        try:
            savings = float(input("Enter your desired monthly savings: $").strip())
            if savings < 0:
                print("Savings amount cannot be negative. Try again.")
                continue
            return savings
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    expenses = get_expenses()
    income = get_income()

    total_expenses = sum(expenses.values())
    remaining_balance = income - total_expenses

    print("\nExpense Breakdown:")
    for name, value in expenses.items():
        print(f"{name}: ${value:.2f}")

    if remaining_balance >= 0:
        print(f"You're saving ${remaining_balance:.2f} this month.")
        savings = get_savings_amount(remaining_balance)
        if savings <= remaining_balance:
            print("You can save that amount this month.")
        else:
            print("You don't have enough remaining balance to save that amount.")
    else:
        print(f"You're short by ${abs(remaining_balance):.2f} this month.")

if __name__ == "__main__":
    main()
