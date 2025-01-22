sentence = "Phyton is fun and Phyton is easy to learn!"

vowels = "aeiouAEIOU"
modified_sentence = ""

for letter in sentence:
    if letter in vowels:
        modified_sentence += letter.upper()
    else:
        modified_sentence += letter

print(modified_sentence)
