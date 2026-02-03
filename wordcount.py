sentence = input("Enter a sentence: ")
freq = {}

for word in sentence.lower().split():
    freq[word] = freq.get(word, 0) + 1

print(freq)
