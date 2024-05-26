
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fredr\Desktop\Prosjekter\NewPassManager\build\assets\frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1800x900")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 900,
    width = 1800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    914.0,
    461.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    917.0,
    195.0,
    image=image_image_2
)

canvas.create_rectangle(
    659.0,
    272.0,
    1141.0,
    841.0,
    fill="#A3B939",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=768.0,
    y=629.0,
    width=264.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=768.0,
    y=703.0,
    width=264.0,
    height=65.0
)

canvas.create_text(
    829.0,
    789.0,
    anchor="nw",
    text="NestSafe v1.0",
    fill="#000000",
    font=("Noto Sans", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    914.0,
    547.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=763.0,
    y=514.0,
    width=302.0,
    height=65.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    914.0,
    427.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=763.0,
    y=394.0,
    width=302.0,
    height=65.0
)

canvas.create_text(
    839.0,
    484.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("LexendDeca Bold", 24 * -1)
)

canvas.create_text(
    836.0,
    360.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("LexendDeca Bold", 24 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1077.0,
    y=551.0,
    width=37.0,
    height=35.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=1079.0,
    y=499.0,
    width=37.0,
    height=35.0
)

canvas.create_text(
    726.0,
    291.0,
    anchor="nw",
    text="CREATE ACCOUNT",
    fill="#000000",
    font=("LexendDeca Bold", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
