import random
import re
start_condition = re.compile('^"?[A-Z]')
end_condition = re.compile('[.?!]"?$')

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

word_list = words.split()
# TODO: analyze which words can follow other words
# Your code here
markov_dictionary = {}

for index, word in enumerate(word_list):
    if word not in markov_dictionary:
        if index + 1 < len(word_list):
            markov_dictionary[word] = [word_list[index + 1]]
        else:
            markov_dictionary[word] = [word_list[0]]
    else:
        if index + 1 < len(word_list):
            markov_dictionary[word].append(word_list[index + 1])

# for key, value in markov_dictionary.items():
#     if len(value) > 0:
#         print(f'{key}:{value}')

# TODO: construct 5 random sentences
# Your code here
def generate_markov_sentences():
    start = False
    stop = False
    starts_with_apos = False
    ends_with_apos = False
    key_word = ''
    markov_sentence = ''

    while start == False:
        once_upon_a_time = random.choice(list(markov_dictionary.keys()))
        if start_condition.search(once_upon_a_time):
            key_word = once_upon_a_time
            if key_word[0] == '"':
                starts_with_apos = True
            else:
                starts_with_apos = False
            start = True

    current_word = key_word

    while stop == False:
        if end_condition.search(current_word):
            if current_word[len(current_word) - 1] == '"':
                ends_with_apos = True
            else:
                ends_with_apos = False
            markov_sentence += current_word + '"' if starts_with_apos and not ends_with_apos else current_word
            stop = True
        else:
            markov_sentence += current_word + ' '
            current_word = random.choice(markov_dictionary[current_word])
    
    return markov_sentence

for i in range(5):
    print("")
    print(generate_markov_sentences())
    print("")
