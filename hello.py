#ბიბლიოთეკა Emojize-ის დახმარებით დაწერეთ პროგრამა სადაც მომხარებელი შეძლებს შემოიყვანოს ტექსტი სადაც შესაძლებელია იყოს ემოჯების უნიკოდი მაგალითად 👍. თქვენმა პროგრამამ უნდა დააბრუნოს იგივე ტექსტი ოღონდ უნიკოდის ნაცვლად უნდა იყოს ემოჯი.
from emojize import emojize

def convert_text_with_emojis():
    user_input = input("Enter text with emoji codes: ")
    converted_text = emojize(user_input, language='alias')
    print("Converted text:", converted_text)

convert_text_with_emojis()

#იბლიოთეკა figlet-ის დახმარებით დაწერეთ პროგრამა სადაც მომხარებელი შეძლებს შემოიყვანოს ტექსტი.
#ასევე გამოიყენეთ sys ბიბლიოთეკა საიდანაც შეძლებთ პროგრამის გაშვებისას სასურველი ფონტის აღებას.

#თუ გაშვებისას არ არის მითითებული კონკრეტული ფონტი მაშინ რანდომულად აირჩიეთ ფონტი და მიღებული ტექსი გამობეჭდეთ figlet-ის რანდომული ფონტით.

#თუ გაშვებისას არის მითითებული კონკრეტული ფონტი -f --font მეშვეობით მაშინ ამ კონკრეტული ფონტით გამობეჭდეთ მიღებული ტექსტი

from emojize import emojize

def convert_text_with_emojis():
    user_input = input("Enter text with emoji codes: ")
    converted_text = emojize(user_input, language='alias')
    print("Converted text:", converted_text)

convert_text_with_emojis()

#- პროექტი 66 - Adieu, Adieu
import inflect

def main():
    p = inflect.engine()
    names = []

    try:
        while True:
            name = input("Name: ")
            if name.strip():
                names.append(name)
    except EOFError:
        print()
        farewell = p.join(names, final_sep=" and ")
        print(f"Adieu, adieu, to {farewell}")

if __name__ == "__main__":
    main()

#- პროექტი 67 - Guessing Game
import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            return int(input("Guess: "))
        except ValueError:
            pass

def guessing_game():
    level = get_level()
    secret_number = random.randint(1, level)

    while True:
        guess = get_guess()
        
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

guessing_game()

#- პროექტი 68 - Little Professor
import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        attempts = 0

        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        
        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    ranges = {1: (0, 10), 2: (10, 100), 3: (100, 1000)}
    start, end = ranges[level]
    return random.randint(start, end - 1), random.randint(start, end - 1)

if __name__ == "__main__":
    main()

#- პროექტი 69 - Bitcoin Price Index
import sys
import requests

def get_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    data = response.json()
    return data['bpi']['USD']['rate_float']

def main():
    if len(sys.argv) != 2:
        print("გთხოვთ, მიუთითოთ რიცხვი, მაგალითად: python bitcoin.py 1")
        sys.exit(1)
    
    bitcoin_amount = float(sys.argv[1])
    bitcoin_price = get_bitcoin_price()
    usd_amount = bitcoin_amount * bitcoin_price
    
    print(f"${usd_amount:,.4f}")

if __name__ == '__main__':
    main()

#- პროექტი 70 - Magic 8 Ball
import random

def magic_8_ball():
    responses = ["Yes", "No", "Ask again later"]
    return random.choice(responses)

def main():
    question = input("Whats your question? ")
    print(magic_8_ball())

if __name__ == '__main__':
    main()
#- პროექტი 72 - Password Generator
import string
import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def generate_password(min_length, num_special_chars, num_numbers):
    if min_length < num_special_chars + num_numbers:
        print("Password minimum length should be greater than or equal to the sum of special characters and numbers.")
        return None

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = []

    password.extend(random.choices(string.punctuation, k=num_special_chars))
    password.extend(random.choices(string.digits, k=num_numbers))

    remaining_length = min_length - len(password)
    password.extend(random.choices(string.ascii_letters, k=remaining_length))

    random.shuffle(password)

    return ''.join(password)

def main():
    min_length = get_positive_integer("What's the minimum length? ")
    num_special_chars = get_positive_integer("How many special characters? ")
    num_numbers = get_positive_integer("How many numbers? ")

    password = generate_password(min_length, num_special_chars, num_numbers)
    
    if password:
        print("Your password is")
        print(password)

if __name__ == '__main__':
    main()
#- პროექტი 73 - Guess the Number Game
import random

def get_difficulty_level():
    while True:
        try:
            level = int(input("Pick a difficulty level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please choose between 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def generate_number(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 100)
    elif level == 3:
        return random.randint(1, 1000)

def get_guess():
    while True:
        try:
            guess = int(input("What's your guess? "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def evaluate_guess(guess, number):
    if guess < number:
        return "Too low."
    elif guess > number:
        return "Too high."
    else:
        return "You got it!"

def give_feedback(guesses):
    if guesses == 1:
        return "You're a mind reader!"
    elif 2 <= guesses <= 4:
        return "Most impressive."
    elif 5 <= guesses <= 7:
        return "You can do better than that."
    else:
        return "Better luck next time."

def play_game():
    print("Lets play Guess the Number.")
    
    while True:
        level = get_difficulty_level()
        number = generate_number(level)
        guesses = 0
        guessed_correctly = False

        while not guessed_correctly:
            guess = get_guess()
            guesses += 1
            result = evaluate_guess(guess, number)
            print(result)

            if guess == number:
                guessed_correctly = True
                print(f"You got it in {guesses} guesses!")
                print(give_feedback(guesses))
        
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Goodbye!")
            break

if __name__ == '__main__':
    play_game()

#- პროექტი 75 - speech to text
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("You said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    recognize_speech()

#- პროექტი 76 - Google Search
import webbrowser

def google_search():
    search_query = input("What would you like to search for on Google? ")
    webbrowser.open(search_query)

if __name__ == "__main__":
    google_search()
