import requests
from datetime import datetime
from tkinter import *
from tkcalendar import *
import webbrowser
from tkinter import messagebox


# ______________________________________________FUNCTIONS________________________________________________#
def open_browser():
    webbrowser.open(URL, new=1)


def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    endpoint = "https://pixe.la/v1/users/nineseven8/graphs/graph1/"
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    requests.post(url=endpoint, json=pixel_add, headers=HEADERS)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel added.")


def del_pixel():
    endpoint = f"https://pixe.la/v1/users/nineseven8/graphs/graph1/{format_date()}"
    requests.delete(url=endpoint, headers=HEADERS)
    messagebox.showinfo(message="Pixel deleted.")


def change_pixel():
    endpoint = f"https://pixe.la/v1/users/nineseven8/graphs/graph1/{format_date()}"
    pixel_update = {
        "quantity": user_in.get(),
    }
    requests.put(url=endpoint, json=pixel_update, headers=HEADERS)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel updated.")


# __________________________________________CONSTANTS___________________________________________________#
URL = "https://pixe.la/v1/users/brandon151/graphs/discipline.html"
TODAY = datetime.now()
TOKEN = "####"
USERNAME = "##"

# _____________________________________________WINDOW__________________________________________________#
root = Tk()
root.title("Python Journey")
root.iconphoto(True, PhotoImage(file="619282-middle.png"))
root.resizable(width=False, height=False)
root.config(pady=20, padx=20)

# _________________________________________END POINTS____________________________________________________#
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{pixela_endpoint}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/discipline"

# ____________________________________________CALENDER___________________________________________________#
cal = Calendar(root, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.grid(row=0, column=0, columnspan=4)
units = Label(text="Hours/Day:")
units.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")
user_in = Entry(width=10)
user_in.grid(row=1, column=2, sticky="w")

# _____________________________________________BUTTONS__________________________________________________#
add = Button(text="Add", command=add_pixel)
add.grid(row=2, column=0, pady=10)
update = Button(text="Update", command=change_pixel)
update.grid(row=2, column=1, pady=10, sticky="w")
delete = Button(text="Delete", command=del_pixel)
delete.grid(row=2, column=2, pady=10, sticky="w")
link = Button(text="Show\nJourney", command=open_browser)
link.grid(row=2, column=3)

# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": "discipline",
    "name": "Monk Mode❄",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

root.mainloop()
