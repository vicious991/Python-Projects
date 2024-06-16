#This Python script is designed to read a text file, identify specific words enclosed in angle brackets < >,
#  prompt the user to provide replacement words for each identified word, and then output the modified text 
# with the replacements.


with open ("story.txt","r") as f: #opening the story.txt as f # it should be in same folder

    story = f.read() 
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

#Identify words enclosed in angle brackets and store them in the words set.
for i ,char in enumerate(story):
    if char == target_start:
        start_of_word= i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

#Prompt the user to enter replacement words for each identified word and store them in the answers dictionary.
answers = {}

for word in words:
    answer  = input("Enter A Word For"+ word + ": ")
    answers[word]= answer

#Replace the identified words in the story with the user-provided replacements.
for word in words:
    story = story.replace(word,answers[word])

# Print the modified story with the replacements.
print(story)
