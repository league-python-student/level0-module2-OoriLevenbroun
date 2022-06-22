import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment
    if random_number == 1:
        messagebox.showerror(title='U DuMb', message='you are not the sharpest tool in the shed')
    if random_number == 2:
        messagebox.showinfo(title='U B4raB1è', message='you are ok')
    if random_number == 3:
        messagebox.showinfo(message='you are nice')
    if random_number == 4:
        messagebox.showinfo(message='you are the best person in the galaxy')
    if random_number == 5:
        messagebox.showinfo(message='you are the best person in the muliverse of multiverses!')
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
