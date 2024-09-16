# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

OUTPUT_DIRECTORY = "./Output/ReadyToSend/"

# Open the text file and read the lines
with open('./Input/Names/invited_names.txt', 'r') as file:
    # Read the file and strip newline characters
    names_list = [line.strip() for line in file]

with open('./Input/Letters/starting_letter.txt', 'r') as file:
    letter_text = file.read()

# Loop through the names and replace [name] in the letter for each person
for name in names_list:
    personalized_letter = letter_text.replace('[name]', name)

    # Create a filename for each person
    filename = f"{OUTPUT_DIRECTORY}letter_for_{name}.txt"

    # Save the personalized letter to a file
    with open(filename, 'w') as file:
        file.write(personalized_letter)

