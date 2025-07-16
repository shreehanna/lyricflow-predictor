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
#output
<img width="1600" height="324" alt="Screenshot 1947-04-25 at 11 06 27 PM" src="https://github.com/user-attachments/assets/dcbc5465-4f27-4472-9e00-caaf57b3d800" />
