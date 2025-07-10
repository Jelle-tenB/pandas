student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access row.student or row.score
    pass

alphabet_data = pandas.read_csv(r"day 26 NATO\nato_phonetic_alphabet.csv")
# Keyword Method with iterrows()
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_nato():
    username = input("What is your name?: ").upper()
    try:
        natoname = [alphabet_dict[f"{letter}"] for letter in list(username)]
    except KeyError:
        print("Please enter letters only.")
        generate_nato()
    else:
        print(natoname)

generate_nato()
