import tkinter as tk
from tkinter import messagebox
import requests
import random

qns = [
"https://opentdb.com/api.php?amount=50&category=9&type=multiple",

"https://opentdb.com/api.php?amount=25&category=18&type=multiple",

"https://opentdb.com/api.php?amount=50&category=10&type=multiple",

"https://opentdb.com/api.php?amount=50&category=16&type=multiple",

"https://opentdb.com/api.php?amount=45&category=17&type=multiple",

"https://opentdb.com/api.php?amount=50&category=28&type=multiple",

"https://opentdb.com/api.php?amount=50&category=22&type=multiple"
]


response = requests.get(random.choice(qns))
data = response.json()
questions = data["results"]
root = tk.Tk()
root.title("qn")
root.geometry("500x300")
question_index = 0
correct_answers = 0

def load_question():
    global question_index

    question_data = questions[question_index]
    question_label.config(text=question_data["question"])

    options = [question_data["correct_answer"]] + question_data["incorrect_answers"]
    random.shuffle(options)

    for i in range(4):
        option_buttons[i].config(text=options[i], state='normal')
        option_buttons[i].config(variable=clicked, value=options[i])

def show_results():
    percent_correct = (correct_answers / len(questions)) * 100
    messagebox.showinfo("Results", f"You got {correct_answers} out of {len(questions)} questions correct.  Bruh!, How!!!! .That is {percent_correct:.2f}%.")
def skipbro():
    global question_index, correct_answers

    for btn in option_buttons:
        btn.config(state='disabled')

    print("SA: ", ":( Skipped")
    correct_answer = questions[question_index]["correct_answer"]
    print("CA: ", correct_answer)

    if question_index < len(questions) - 1:
        question_index += 1
        load_question()
    else:
        show_results()

def check_answers():
    global question_index, correct_answers

    for btn in option_buttons:
        btn.config(state='disabled')

    selected_answer = clicked.get()
    print("SA: ", selected_answer)
    correct_answer = questions[question_index]["correct_answer"]
    print("CA: ", correct_answer)

    if selected_answer == correct_answer:
        correct_answers += 1

    if question_index < len(questions) - 1:
        question_index += 1
        load_question()
    else:
        show_results()

question_label = tk.Label(root, text="", wraplength=400)
question_label.pack()

option_buttons = []
clicked = tk.StringVar()

for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=clicked, value="")
    btn.pack()
    option_buttons.append(btn)

load_question()

submit_button = tk.Button(root, text="Submit", command=check_answers)
submit_button.pack()

skip_button = tk.Button(root, text="Skip Qn", command=skipbro)
skip_button.pack()

root.mainloop()
