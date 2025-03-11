#შექმენტით პროგრამა სადაც მომხმარებელს შემოყავს თანხა $ ნიშნით, მაგალითად $50.00, და პროცენტი, მაგალითად 10%.
#თქვენმა პროცენტმა უნდა გამოთვალოს რამდენია თანხის მოცემული პროცენტი, ანუ რამდენია მაგალითად 50-ის 10 პროცენტი

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip()
    if d.startswith("$"):
        d = d[1:]
    return float(d)


def percent_to_float(p):
    p = p.strip()
    if p.endswith("%"):
        p = p[:-1]
    return float(p) / 100


if __name__ == "__main__":
    main()

#დაწერეთ პროგრამა სადაც მომხმარებელი შემოიტანს რაღაც ტექსტს. შეამოწმეთ ეს ტექსტი და თუ იგი იწყება hello მაშინ გამოპრინტეთ $0, თუ იწყება h მაშინ  $20 სხვა ყველა შემთხვევაში $100

def main():
    text = input("Say something: ").strip().lower()
    
    if text.startswith("hello"):
        print("$0")
    elif text.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()

#დაწერეთ პროგრამა სადაც მომხარებელი შემოიყვანს მათემატიკურ განტოლებას, მაგალითად 25 - 15. თქვენმა პროგრამა უნდა დააბრუნოს სწორი მათემატირკური გამოთვლის შედეგად მიღებული პასუხი
def main():
    expression = input("Enter a math expression (e.g., 25 - 15): ").strip()
    print(evaluate_expression(expression))


def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception:
        return "Invalid expression"


if __name__ == "__main__":
    main()
#დაწერეთ პროგრამა სადაც მომხმარებელი შემოიყვანს საათს, მაგალითად 7:30. თუ შემოყვანილი საათი არის 7:00-8:00 მაშინ უნდა გამობეჭდოთ breakfast time, თუ 12:00-13:00 მაშინ lunch time, თუ 18:00-19:00 მაშინ dinner time, სხვა შემთხვევაში არაფერი არ უნდა გამოიბეჭდოს.
def main():
    time = input("What time is it? ").strip()
    hour = convert(time)
    
    if 7.0 <= hour < 8.0:
        print("breakfast time")
    elif 12.0 <= hour < 13.0:
        print("lunch time")
    elif 18.0 <= hour < 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60


if __name__ == "__main__":
    main()

#შექმენით მარტივი პაროლების ვალიდატორი. ჩათვალე, რომ გაქვს შენახული რაიმე პაროლი ცვლადად. შეეკითხე მომხმარებელს username და password, შემდეგ კი შეამოწმე ემთხვევა თუ არა მომხმარებლის მიერ შეყვანილი პაროლი შენს პაროლს, რომლიც ცვლადად გაქვს. თუ ემთხვევა, მაშინ გამოიტანე 'Welcome!', თუ არა - 'I don't know you.'
stored_password = "mySecretPassword123"
username = input("Enter your username: ")
password = input("Enter your password: ")

if password == stored_password:
    print("Welcome!")
else:
    print("I don't know you.")
#შექმენით პროგრამა, რომელიც გარდაქმნის ტემეპრატურას ფარენჰეიტიდან ცელსიუსში და პირიქით. პროგრამამ უნდა შეეკითხოს მომხმარებელს კონვერტაციის ტიპი და შემდეგ გარდაქმნას შესაბამისად. ფორმულები:

print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
choice = input("Your choice: ")

if choice == 'C' or choice == 'c':
    fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature in Celsius is", celsius)
elif choice == 'F' or choice == 'f':
    celsius = float(input("Please enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("The temperature in Fahrenheit is", fahrenheit)
else:
    print("Invalid choice")
