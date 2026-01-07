#a quiz program that checks if the user knows the capital of
questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Norway": "Oslo",
    "Sweden": "Stockholm",
    "Portugal": "Lisbon",
    "Austria": "Vienna"
}

for country, capital in questions.items():
    answer = input("What is the capital of " + country + "? ")

    if answer.strip().lower() == capital.lower():
        print("Correct!")
    else:
        print("Wrong! The correct answer is " + capital + ".")
