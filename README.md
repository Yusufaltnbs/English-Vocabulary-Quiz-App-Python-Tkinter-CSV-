# 🧠 English Vocabulary Quiz App (Python + Tkinter + CSV)

This is a lightweight GUI-based vocabulary quiz application built with **Python**, **Tkinter**, and **Pandas**. It randomly selects an English word from a CSV file and prompts the user to type its correct **Turkish meaning**. It is ideal for English learners who want to reinforce their vocabulary through active recall, hints, and feedback.

---

## ✨ Features

- ✅ Uses an external CSV file with English–Turkish word pairs
- 🎯 Randomly displays a new word each round
- ⌨️ Users can answer by pressing **Enter** (no mouse required)
- ❌ Wrong answers provide **progressive letter-by-letter hints**
- 🔁 "Skip Word" button allows the user to move to the next word
- 🟢 Correct answers increase the score and immediately show a new word
- 🟡 Real-time feedback is displayed on-screen (green for correct, red for incorrect, orange for skipped)
- 📊 The score is shown at the bottom of the app
- 🪶 Clean, simple, and responsive interface built with Tkinter

---

## 🗂️ Folder Structure

vocab-quiz/
│
├── vocab_game.py # Main Python file with GUI and logic
├── words.csv # English–Turkish word list (your source)
└── README.md # You're reading it!

---

## 📦 Requirements

Ensure you have Python installed (version 3.8+ is recommended). Then, install required libraries:

```bash
pip install pandas
▶️ How to Run
Simply run the Python file with:

python vocab_game.py
Make sure that the words.csv file is in the same folder as the Python script.

🧠 How the Code Works (Explanation)
The program loads the CSV file using pandas.read_csv.

A random index is selected, and the English word is shown.

The user types their guess. On incorrect guesses, the app reveals one more letter of the correct Turkish meaning as a hint.

If the user answers correctly, the score increases, a green message appears, and a new word is automatically shown.

If the user presses the "Skip Word" button, the current word is skipped and replaced.

Everything happens within a Tkinter GUI, including the feedback messages.

Snippet of Logic:

if answer == correct_translation:
    score += 1
    load_new_word()
else:
    hint += correct_translation[next_letter]

📝 To Do (Optional Enhancements)
 Add reverse mode: Turkish → English

 Track wrong answers and show final score

 Save stats to file (date, score, skipped, etc.)

 Include multiple difficulty levels

🙋‍♂️ Author
Developed by Yusuf Altunbaş
Computer Engineering Student — Çanakkale Onsekiz Mart University
