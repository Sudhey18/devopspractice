with open("sampletext.txt", "r") as file:
    words = file.read().split()

print(f"Word Count: {len(words)}")
