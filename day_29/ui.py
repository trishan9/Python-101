from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#ffffff"
GREEN = "#00ff00"
RED = "#ff0000"


class QuizUI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg=WHITE)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Hello World I am Question", font=("Arial", 18, "italic"), width=280)
        self.canvas.grid(
            padx=20, pady=20, row=1, column=0, columnspan=2)

        CHECK_ICON = PhotoImage(file="./images/true.png")
        self.checkicon = Button(
            image=CHECK_ICON, highlightthickness=0, command=self.check_true_answer)
        self.checkicon.grid(row=2, column=0)

        WRONG_ICON = PhotoImage(file="./images/false.png")
        self.wrongicon = Button(
            image=WRONG_ICON, highlightthickness=0, command=self.check_false_answer)
        self.wrongicon.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def check_true_answer(self):
        is_correct = self.quiz.check_answer("True")
        if is_correct:
            self.canvas.config(background=GREEN)
        else:
            self.canvas.config(background=RED)

        self.next_question()

    def check_false_answer(self):
        is_correct = self.quiz.check_answer("False")
        if is_correct:
            self.canvas.config(background=GREEN)
        else:
            self.canvas.config(background=RED)

        self.next_question()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.window.after(1000, self.change_question)

        else:
            self.canvas.itemconfig(
                self.question_text, text="Quiz Completed!!!")

    def change_question(self):
        self.canvas.config(background=WHITE)
        self.canvas.itemconfig(self.question_text, text=self.question)
        self.score_label.config(text=f"Score: {self.quiz.score}")
