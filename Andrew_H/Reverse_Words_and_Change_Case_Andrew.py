#Reverse Words and Change Case Andrew Hayes 2/21/2025


def reverse_words_and_change_case(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the words
    words = words[::-1]
    # Change the case of the words
    words = [word.swapcase() for word in words]
    # Join the words into a sentence
    sentence = ' '.join(words)
    return sentence

sentence = "Hello world you are not cool" #Output: "COOL NOT ARE YOU WORLD HELLO"
result = reverse_words_and_change_case(sentence)
print(result)