
from tkinter import *
import math

# CONSTANTS #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Consolas"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# TIMER RESET #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="STUDY TIME!")
    check_marks.config(text="")
    global REPS
    REPS = 0


# TIMER MECHANISM #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    # 8TH REP:
    if REPS % 8 == 0:
        countdown(long_break)
        title_label.config(text="BREAK TIME!", fg=RED)
    # 2ND, 4TH, 6TH REP:
    elif REPS % 2 == 0:
        countdown(short_break)
        title_label.config(text="BREAK TIME!", fg=PINK)
    # 1ST, 3RD, 5TH, 7TH REP:
    else:
        countdown(work_sec)
        title_label.config(text="STUDY TIME!", fg=GREEN)


# COUNTDOWN MECHANISM #
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        study_sessions = math.floor(REPS/2)
        for _ in range(study_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# UI SETUP #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# TITLE LABEL #
title_label = Label(text="STUDY TIME!", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# IMAGE #
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_ing = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_ing)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# START AND RESET BUTTON #
start_button = Button(text="START", highlightthickness=0, font=(FONT_NAME, 16, "bold"), command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="RESET", highlightthickness=0, font=(FONT_NAME, 16, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

# CHECK MARKS #
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()

##########################################################################
#                   🎉 Project Credits 🎉
# ------------------------------------------------------------------------
# Developed during Dr. Angela Yu's "100 Days of Code" Bootcamp. 🚀
# ------------------------------------------------------------------------
##########################################################################
