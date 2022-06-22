import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3
    simpledialog.askstring(title='welcome to the all seeing eye(definitely not of the illuminati because it definitely does not exist)', prompt='enter a question for the magic 8 ball')
    # If the random number is 0
    ans = random.randint(0, 3)
        # tell the user "Yes"
    if ans == 0:
        messagebox.showinfo(title='...', message='yes')
    # If the random number is 1
    if ans == 1:
        messagebox.showinfo(title='...', message='no')
        # tell the user "No"

    # If the random number is 2
    if ans == 2:
        messagebox.showinfo(title='...', message='...... ok maybe I do not know that much but google definitely does(and does not belong to the illuminati the does not exist)')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if ans == 3:
        messagebox.showerror(title='virus detected')
        # write your own answer
