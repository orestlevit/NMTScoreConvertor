from pathlib import Path
import tkinter
from tkinter import ttk, messagebox
from customtkinter import *

# <----- Base ----->
root1 = CTk()
root1.minsize(1100, 500)
root1.title("Convertor")
frame = CTkFrame(root1, fg_color="#2e2e2e")
# <----- Base ----->

# <----- Labels ----->
label = CTkLabel(root1, text="✩░▒▓▆▅▃▂▁ 𝐍𝐌𝐓 𝐄𝐱𝐚𝐦 𝐬𝐜𝐨𝐫𝐞 𝐜𝐨𝐧𝐯𝐞𝐫𝐭𝐨𝐫 ▁▂▃▅▆▓▒░✩", font=('ITALIC', 25))
label.pack(pady=(10, 0))

label1 = CTkLabel(frame, font=('ITALIC', 17))

subject_label = CTkLabel(frame, text="𝑺𝒆𝒍𝒆𝒄𝒕 𝒚𝒐𝒖𝒓 𝒔𝒄𝒉𝒐𝒐𝒍 𝒔𝒖𝒃𝒋𝒆𝒄𝒕", font=('', 25))
subject_label.pack(padx=(40, 40), pady=(0, 10))

result_label = CTkLabel(frame, font=("", 40))

arrow_label = CTkLabel(frame, text="⇓", font=("", 60))
# <----- Labels ----->


# <----- Comboboxes ----->
combobox_list = ["Math", "Foreign language", "History", "Ukrainian"]
combobox = CTkComboBox(frame, values=combobox_list, width=200, font=("", 15))
combobox.pack(pady=(0, 10))
# <----- Comboboxes ----->

# <----- Buttons ----->
apply_button = CTkButton(frame, text="Apply", command=lambda: [label_change(combobox), activate()], width=150,
                         fg_color="green", hover_color="#005a00", font=('', 17))
apply_button.pack(pady=(0, 10))

button = CTkButton(frame, text="Convert",
                   command=lambda: [get_score(combobox.get(), value_check(entry)), valid_score_check(combobox, entry),
                                    arrow_label.pack(), result_label.pack(pady=(0, 20))],
                   fg_color="green", hover_color="#005a00", font=('', 17))
# <----- Buttons ----->

# <----- Entries ----->
entry = CTkEntry(frame, font=('', 15))


# <----- Entries ----->

# <----- Codes/Logics ----->
def label_change(combobox_name):
    if combobox.get() == "Math":
        label1.configure(text="Exam Score: Math(5-32)")
    elif combobox.get() == "Foreign language":
        label1.configure(text="Exam Score: Foreign language(5-32)")
    elif combobox.get() == "History":
        label1.configure(text="Exam Score: History(8-54)")
    elif combobox.get() == "Ukrainian":
        label1.configure(text="Exam Score: Ukrainian(5-45)")
    else:
        return messagebox.showerror("𝑺𝒖𝒃𝒋𝒆𝒄𝒕 𝒅𝒐𝒆𝒔 𝒏𝒐𝒕 𝒆𝒙𝒊𝒔𝒕",
                                    "𝑷𝒍𝒆𝒂𝒔𝒆, 𝒔𝒆𝒍𝒆𝒄𝒕 𝒚𝒐𝒖𝒓 𝒔𝒄𝒉𝒐𝒐𝒍 𝒔𝒖𝒃𝒋𝒆𝒄𝒕")


def activate():
    label1.pack()
    entry.pack(pady=(0, 10))
    button.pack(pady=(0, 10))


def get_score(answer, score):
    if answer == "Ukrainian":
        path = Path("scores_table/ukrainian.txt")
    elif answer == "Math":
        path = Path("scores_table/math.txt")
    elif answer == "History":
        path = Path("scores_table/history.txt")
    elif answer == "Foreign language":
        path = Path("scores_table/foreignlang.txt")
    else:
        return messagebox.showerror("𝑺𝒖𝒃𝒋𝒆𝒄𝒕 𝒅𝒐𝒆𝒔 𝒏𝒐𝒕 𝒆𝒙𝒊𝒔𝒕",
                                    "𝑷𝒍𝒆𝒂𝒔𝒆, 𝒔𝒆𝒍𝒆𝒄𝒕 𝒚𝒐𝒖𝒓 𝒔𝒄𝒉𝒐𝒐𝒍 𝒔𝒖𝒃𝒋𝒆𝒄𝒕")

    file_content = path.read_text()

    split_file = file_content.split("\n\n")

    b = [int(i) for i in split_file]

    def convertor(list1):
        n = len(list1)
        converted_dict = {}
        for i in range(0, n, 2):
            converted_dict.update({list1[i]: list1[i + 1]})
        return converted_dict

    converted_scores = dict(convertor(b))
    result_label.configure(text=converted_scores.get(score))


def value_check(some_entry):
    if some_entry.get():
        return int(some_entry.get())
    else:
        return messagebox.showerror("𝑺𝒄𝒐𝒓𝒆 𝒅𝒐𝒆𝒔 𝒏𝒐𝒕 𝒆𝒙𝒊𝒔𝒕", "𝑷𝒍𝒆𝒂𝒔𝒆, 𝒆𝒏𝒕𝒓𝒚 𝒚𝒐𝒖𝒓 𝒔𝒄𝒐𝒓𝒆 ")


def valid_score_check(some_combobox, some_entry):
    if some_combobox.get() == "Ukrainian":
        score_range = range(5, 45)
    elif some_combobox.get() == "Math":
        score_range = range(5, 32)
    elif some_combobox.get() == "History":
        score_range = range(8, 54)
    elif some_combobox.get() == "Foreign language":
        score_range = range(5, 32)
    else:
        exit()

    if int(some_entry.get()) < score_range.start or int(some_entry.get()) > score_range.stop:
        return messagebox.showerror("𝑾𝒓𝒐𝒏𝒈 𝒔𝒄𝒐𝒓𝒆", "𝑷𝒍𝒆𝒂𝒔𝒆, 𝒆𝒏𝒕𝒓𝒚 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒔𝒄𝒐𝒓𝒆")


# <----- Codes/Logics ----->

frame.pack(pady=(20, 0))
root1.mainloop()
