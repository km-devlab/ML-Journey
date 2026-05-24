import time
import random

# List of sentences
sentences = [
    "python is fun and powerful",
    "coding builds strong logic",
    "practice makes you better",
    "consistency beats motivation",
    "debugging improves your skills"
]

# Pick random sentence
sentence = random.choice(sentences)

print("Type this sentence as fast as you can:\n")
print(sentence)

input("\nPress Enter when ready...")

# Start timer
start = time.time()

typed = input("\nStart typing: ")

# End timer
end = time.time()

time_taken = end - start

# Words per minute
words = len(sentence.split())
wpm = (words / time_taken) * 60

# Accuracy calculation
correct = 0
for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
        correct += 1

accuracy = (correct / len(sentence)) * 100

# Results
print("\n--- RESULT ---")

if typed == sentence:
    print("✅ Perfect typing!")
else:
    print("❌ Some mistakes were made.")

print(f"⏱ Time: {round(time_taken, 2)} seconds")
print(f"⚡ Speed: {round(wpm, 2)} WPM")
print(f"🎯 Accuracy: {round(accuracy, 2)}%")
