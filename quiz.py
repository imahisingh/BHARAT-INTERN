import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.configure(bg='lightblue')

        self.score = 0
        self.question_index = 0

        self.questions = [
            {"question": "What is the capital of India?", "options": ["Punjab", "U.P", "New Delhi", "J&K"], "answer": "New Delhi"},
            {"question": "What is 2 + 6?", "options": ["4", "3", "8", "6"], "answer": "8"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
        ]

        self.question_label = tk.Label(root, text="", font=("Arial", 14), bg='lightblue')
        self.question_label.pack()

        self.radio_var = tk.StringVar()
        self.radio_buttons = []

        for i, option in enumerate(self.questions[0]["options"]):
            radio = tk.Radiobutton(root, text=option, variable=self.radio_var, value=option, font=("Arial", 12), bg='lightblue')
            radio.pack()
            self.radio_buttons.append(radio)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12), bg='green', fg='white')
        self.submit_button.pack()

        self.next_button = tk.Button(root, text="Next", state=tk.DISABLED, command=self.next_question, font=("Arial", 12), bg='blue', fg='white')
        self.next_button.pack()

        self.show_next_question()

    def show_next_question(self):
        if self.question_index < len(self.questions):
            question_text = self.questions[self.question_index]["question"]
            self.question_label.config(text=question_text)
            self.radio_var.set("")

            for i, option in enumerate(self.questions[self.question_index]["options"]):
                self.radio_buttons[i].config(text=option)

            self.submit_button["state"] = tk.NORMAL
            self.next_button["state"] = tk.DISABLED
        else:
            result_text = f"Your score: {self.score}/{len(self.questions)}"
            self.question_label.config(text=result_text)
            self.submit_button["state"] = tk.DISABLED
            self.next_button["state"] = tk.DISABLED
            messagebox.showinfo("Quiz Completed", result_text)

    def check_answer(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.questions[self.question_index]["answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.question_index += 1
        self.show_next_question()

    def next_question(self):
        self.question_index += 1
        self.show_next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
