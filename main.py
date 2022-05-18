import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN =0.1
LONG_BREAK_MIN = 0.3
timer1=None
reps=0
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer1)
    canvas.itemconfig(timer, text="00:00")
    tick_label.config(text="")
    timer_label.config(text="Timer",fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    print("start time called")
    global reps
    reps +=1

    work_sec=math.floor(WORK_MIN * 60)
    short_break_sec=math.floor(SHORT_BREAK_MIN * 60)
    long_break_min=math.floor(LONG_BREAK_MIN * 60)

    if reps % 8 ==0:
        count_down(long_break_min)
        print("countdown finished")
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        print("countdown finished")
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        print("countdown finished")
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    print("count down called")
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec==0 or count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer1
        timer1=window.after(1000, count_down, count - 1)
    else:
        print("countdown end inside countdown")
        print("invoke start time inside count down")
        start_timer()
        print("start timer finished inside count down")
        print(reps)
        tick_mark=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            tick_mark +="✔"
        tick_label.config(text=tick_mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 37, "bold"), bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)

tick_label = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
tick_label.grid(row=3, column=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
