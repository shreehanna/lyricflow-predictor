from collections import defaultdict
import random
import string

with open("Good Luck, Babe!.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()
    text = text.translate(str.maketrans("", "", string.punctuation))  # 🧼 Clean it!
    tokens = text.split()
    print("📄 Sample tokens:", tokens[:50])  # see the first 50 tokens

model=defaultdict(list)
for i in range(len(tokens) - 2):
    key = (tokens[i],tokens[i+1])
    model[key].append(tokens[i+2])
def predict_next_word(context,top=3):
    words=context.lower().split()
    if len(words) < 2:
        return ["pls enter 2 words!"]
    key=(words[-2],words[-1])
    options=model.get(key,[])
    return random.sample(options, min(top,len(options))) if options else ["no match"]
print("🎤 ChapelBot Lite is live. Type any 2 words from the lyrics:")
while True:
    user_input = input("you:")
    if user_input.lower() in["exit","quit"]:
        break
    print("🔥 Prediction:",predict_next_word(user_input))


