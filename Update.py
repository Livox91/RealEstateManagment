from pathlib import Path
from tkinter import Tk, Toplevel,Canvas, Entry, Text, Button, PhotoImage
import importlib
import globalVars
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame14")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_update(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Update_window(parent_window): 
    window = Toplevel()
    window.geometry("800x600")
    window.configure(bg = "#FFFFFF")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    Logo = PhotoImage(
        file=relative_to_assets_update("image_1.png"))
    canvas.create_image(
        400.0,
        155.0,
        image=Logo
    )

    canvas.create_text(
        344.0,
        342.0,
        anchor="nw",
        text="Enter ID",
        fill="#000000",
        font=("Lexend Regular", 26 * -1)
    )

    id_entry_img = PhotoImage(
        file=relative_to_assets_update("entry_1.png"))
    canvas.create_image(
        407.0,
        421.5,
        image=id_entry_img
    )
    id_entry = Entry(
        window,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    id_entry.place(
        x=381.0,
        y=407.0,
        width=52.0,
        height=27.0
    )

    BackBtn_ = PhotoImage(
        file=relative_to_assets_update("button_1.png"))
    BackBtn = Button(
        window,
        image=BackBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(window),
        relief="flat"
    )
    BackBtn.place(
        x=73.0,
        y=499.0,
        width=107.0,
        height=51.0
    )
   
    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_update("button_2.png"))
    SubmitBtn = Button(
        window,
        image=SubmitBtn_,
        borderwidth=0,
        highlightthickness=0,
        command= lambda:update_id(),
        relief="flat"
    )
    SubmitBtn.place(
        x=633.0,
        y=494.0,
        width=107.0,
        height=51.0
    )
    
    window.resizable(False, False)
    window.mainloop()