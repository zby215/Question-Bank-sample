import pandas as pd
import random
import tkinter as tk
from PIL import Image, ImageTk

questions_df = pd.read_excel('question.xlsx')

window = tk.Tk()
window.title('Question Bank')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))
# 全屏
# window.attributes('-fullscreen', True)


# 设置背景图片
background_image = Image.open('background.jpg')
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# 问题和答案显示参数
question_label = tk.Label(
    window, text='Click "New Question" to get started!', font=('Arial', 40, 'bold'), wraplength=1300, highlightthickness=1, bd=0)
question_label.place(relx=0.5, rely=0.15, anchor=tk.N)

answer_label = tk.Label(window, text='', font=(
    'Arial', 50, 'bold'), fg='green', wraplength=1000, highlightthickness=1, bd=0)
answer_label.place(relx=0.5, rely=0.65, anchor=tk.N)

question_displayed = False


def get_random_question():
    global question_displayed
    num_questions = len(questions_df)
    random_index = random.randint(0, num_questions - 1)
    question_text = questions_df.iloc[random_index]['question']
    answer_text = questions_df.iloc[random_index]['answer']
    question_label.config(text=question_text)
    answer_label.config(text='')
    question_label.answer = answer_text
    question_displayed = True


def show_answer():
    answer_text = question_label.answer
    global question_displayed
    answer_label.config(text=answer_text)
    question_displayed = False

# 按钮显示
new_question_button = tk.Button(
    window, text='New Question', font=('Arial', 20), command=get_random_question)
# new_question_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

answer_button = tk.Button(window, text='Show Answer', underline=0,
                          font=('Arial', 20), command=show_answer)
# answer_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

window.bind('<Return>', lambda event: show_answer()
            if question_displayed else get_random_question())


def resize_background_image(event):
    global background_photo
    global background_label

    window_width = event.width
    window_height = event.height

    resized_image = background_image.resize((window_width, window_height))
    background_photo = ImageTk.PhotoImage(resized_image)

    background_label.config(image=background_photo)


window.bind('<Configure>', resize_background_image)

window.mainloop()
