import random
import csv
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

angels = []
Future_tellers = ['Ipos', 'Vassago', 'Purson', 'Orobas', 'Valac', 'Decarabia']

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def make_celtic_cross_spread():
    positions = ['Present Situation', 'Challenges', 'Subconscious Influences', 'Root Cause', 'Recent Past',
                 'Higher Power', 'Near Future', 'You', 'External Influences', 'Outcome/Future']

    spread_dict = {position: None for position in positions}

    random_angels = random.sample(angels, k=10)

    for i, angel in enumerate(random_angels):
        position = positions[i] if i < len(positions) else f"Extra Card {i - len(positions) + 1}"
        spread_dict[position] = angel

    if spread_dict['Outcome/Future']['Name'] in Future_tellers:
        three_card_draw = random.sample(angels, k=3)
        speak("3-Card Draw for Past, Present, and Future:")
        for i, card in enumerate(three_card_draw):
            speak(f"{['Past', 'Present', 'Future'][i]}: {card['Name']}")
        speak("")

    for position, angel in spread_dict.items():
        speak(f"{position}:")
        if angel:
            speak(f"Name: {angel['Name']}")
            speak(f"Rank: {angel['Rank']}")
            speak("Abilities:")
            for ability in angel['Abilities']:
                speak(f"- {ability}")
            speak(f"Goal: {angel['Goal']}")
            speak(f"Backstory: {angel['Backstory']}")
        else:
            speak("No Angel")
        speak("")

def load_angels():
    with open('Angels.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        
        for row_index, angel in enumerate(reader, start=1):
            # Handle missing 'Abilities' key in CSV
            if 'Abilities' not in angel:
                speak(f"Warning: 'Abilities' not found in row {row_index}. Skipping this row.")
                continue

            abilities = angel.get('Abilities', '').split(',')
            angels.append({
                'Name': angel.get('Name', ''),
                'Rank': angel.get('Rank', ''),
                'Abilities': abilities,
                'Goal': angel.get('Goal', ''),
                'Backstory': angel.get('Backstory', '')
            })




            

# Populate the angels list before creating the Celtic Cross spread
load_angels()
make_celtic_cross_spread()