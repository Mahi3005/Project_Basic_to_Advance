import pyttsx3

# Read the story from file
with open('story.txt', 'r') as f:
    story = f.read()

# Initialize an empty set for words
words = set()

start_of_word = -1
target_start = '<'
target_end = '>'

# Find all placeholder words enclosed in < and >
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# Prompt the user to provide replacements for each placeholder
answers = {}
for word in words:
    answer = input('Enter a word for ' + word + ': ')
    answers[word] = answer

# Replace each placeholder with user-provided word
for word in words:
    story = story.replace(word, answers[word])

# Print the final story
print(story)

# Initialize text-to-speech engine and read the final story
engine = pyttsx3.init()
engine.say(story)
engine.runAndWait()
