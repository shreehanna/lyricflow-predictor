# 🎤 LyricFlow Predictor

A next-word prediction bot trained on the iconic *Good Luck, Babe!* lyrics by Chappell Roan. You type 2 words from the song, it predicts what comes next — like autocomplete, but make it ✨queer pop genius✨.

## 💡 What It Does

- Takes **2 words** from the lyrics as input
- Uses a **3-word N-gram model** to guess the next word
- Returns up to **3 top predictions**
- Built in Python, powered by `collections.defaultdict` & `random`

## 🛠 How to Run

```bash
# Clone the repo
git clone https://github.com/shreehanna/lyricflow-predictor.git
cd lyricflow-predictor

# Run it
python main.py

🧠 Sample Usage

you: it's fine
🔥 Prediction: ["it's", "cool", "you"]

you: i don't
🔥 Prediction: ["wanna", "call", "it"]

📁 Files
main.py – The magic prediction logic
Good Luck, Babe!.txt – Raw lyrics dataset
.gitignore – Keeps PyCharm + .venv clutter out
README.md – This vibe doc

📌 Project Goals
🎓 Add to my USC Transfer + Apple AIML Internship Portfolio
🧠 Explore N-gram modeling + NLP basics
🚀 First step toward building FashionGPT + HoloPlug

👩‍💻 Built by
@shreehanna
