from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text=f"Score: 0", bg=THEME_COLOR, foreground="white")
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="Question", font=FONT,
                                                fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.right_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.right_image, highlightthickness=0, command=self.true_option)
        self.true_button.grid(row=2, column=0)
        self.wrong_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.wrong_image, highlightthickness=0, command=self.false_option)
        self.false_button.grid(row=2, column=1)
        self.next_card()
        self.window.mainloop()

    def next_card(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_option(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_option(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.next_card)
