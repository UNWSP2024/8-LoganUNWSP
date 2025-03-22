#Logan H's USA Capital Quiz
#

#1st, add warning
print("MAKE SURE TO SPELL EVERYTHING RIGHT AND DON'T ABBREVIATE (Example: St. ≠ Saint)")

#2nd import the random to pick the questions
import random

#3rd, define questions and answers
def quiz_user():
    states_capitals = {
        "Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock",
        "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover",
        "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise",
        "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka",
        "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis",
        "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson",
        "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City",
        "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany",
        "North Carolina": "Raleigh", "North Dakota": "Bismarck",
    }

#4th, keep track of the right/wrong answers
    correct = 0
    incorrect = 0
    states = list(states_capitals.keys())
    random.shuffle(states)

#5th, when over display results
    for state in states:
        answer = input(f"What is the capital of {state}? ").strip()
        if answer.lower() == states_capitals[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect! The capital of {state} is {states_capitals[state]}.")
            incorrect += 1

    print(f"\nQuiz complete! You got {correct} correct and {incorrect} incorrect.")


quiz_user()
