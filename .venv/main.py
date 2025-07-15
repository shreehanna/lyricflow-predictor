from collections import defaultdict
import random

# Step 1: Load lyrics
with open("90210.txt", "r", encoding="utf-8") as f:
    raw = f.read().lower()

# Step 2: Tokenize manually (just split on space)
tokens = raw.split()

# Step 3: Build 2-word → next word model
model = defaultdict(list)
for i in range(len(tokens) - 2):
    key = (tokens[i], tokens[i + 1])
    next_word = tokens[i + 2]
    model[key].append(next_word)

# Step 4: Predict function
def predict_next_word(context, top=3):
    words = context.lower().split()
    if len(words) < 2:
        return ["Please enter 2 words!"]
    key = (words[-2], words[-1])
    options = model.get(key, [])
    return random.sample(options, min(len(options), top)) if options else ["[no match]"]

# Step 5: Run it
print("🎤 TravisBot Lite is live. Type any 2 words from the lyrics:")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    predictions = predict_next_word(user_input)
    print("🔥 Prediction:", predictions)

