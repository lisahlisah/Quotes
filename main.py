import requests
from tkinter import *
import os
from PIL import Image, ImageTk
import threading
import sys
#

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

BACKGROUND_COLOR = "#FFF7CD"

background_path = resource_path("background.png")
star_path = resource_path("star.png")

def fetch_data():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        data = response.json()

        quote = data["slip"]["advice"]
        quote_id = data["slip"]["id"]

        canvas.itemconfig(quote_text, text=f"#{quote_id}\n\n{quote}")

    except Exception as e:
        canvas.itemconfig(quote_text, text="Waiting...")
        print(f"Error: {e}")

def get_quote():
    canvas.itemconfig(quote_text, text="Fetching...")
    threading.Thread(target=fetch_data).start()

window = Tk()
window.title("Quotezzz")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

pil_img = Image.open(star_path)
pil_img = pil_img.resize((100, 100))

canvas = Canvas(width=300,height=414, highlightthickness=0, bg=BACKGROUND_COLOR)
background_img = PhotoImage(file=background_path)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="What's your advice?", width=250, font=("Arial", 20, "bold"), fill="white", justify="center")
canvas.grid(row=0, column=0)

star_img = ImageTk.PhotoImage(pil_img)
star_button = Button(image=star_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, cursor="hand2", command=get_quote)
star_button.grid(row=1, column=0)

window.mainloop()
