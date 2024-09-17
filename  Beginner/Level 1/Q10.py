def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

input_sentence = input("Enter a sentence: ")

print("Output after reverse:", reverse_words(input_sentence))