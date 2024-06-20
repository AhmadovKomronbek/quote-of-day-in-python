import requests
import tkinter

def change_text():
    response = requests.get(url="https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()
    word.config(text=data[0]["q"])
    owner.config(text=data[0]["a"])

window = tkinter.Tk()
window.geometry("500x300")

word = tkinter.Label(text="#", font=("arial", 12, "normal"))
word.grid(column=0, row=0, pady=40)

owner = tkinter.Label(text="#", font=("arial", 8, "normal"))
owner.grid(column=0, row=1, pady=10)

button = tkinter.Button(text="Next", command=change_text)
button.grid(column=0, row=2, pady=50, padx=250)

window.mainloop()
