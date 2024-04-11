import json
import difflib 

# Load the JSON file containing the dictionary
def load_dictionary(file_path):
    with open(file_path, 'r') as f:
        dictionary = json.load(f)
    return dictionary

# Function to get the definition of a word
def get_definition(word, dictionary):
    word = word.lower()  # Convert to lowercase for case insensitivity
    if word in dictionary:
        return dictionary[word]
    else:
        # Handle case where word is not found in dictionary
        similar_words = difflib.get_close_matches(word, dictionary.keys(), n=1) #use to find a close match when the word search for is not available
        if similar_words:
            suggestion = similar_words[0]
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found in the dictionary."

# Example usage
dictionary = load_dictionary('C:\\Users\\HP\\Downloads\\data.json')  # Add the file path that has the dictionary
word = input("Enter a word: ")
definition = get_definition(word, dictionary)
print(definition)
