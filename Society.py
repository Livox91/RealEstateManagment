import importlib
from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_ADDSOCIETY = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame5")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_addSociety(path: str) -> Path:
    return ASSETS_PATH_ADDSOCIETY / Path(path)
def addSociety_window():
    addSocietyWindow = Toplevel()
    addSocietyWindow.geometry("800x600")
    addSocietyWindow.configure(bg = "#FFFFFF")

    addSocietyCanvas = Canvas(
        addSocietyWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    addSocietyCanvas.place(x = 0, y = 0)
    addSocietyLogo = PhotoImage(
        file=relative_to_assets_addSociety("image_1.png"))
    addSocietyCanvas.create_image(
        120.0,
        80.0,
        image=addSocietyLogo
    )

    addSocietyCanvas.create_text(
        296.0,
        51.0,
        anchor="nw",
        text="ADD Society Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    addSocietyCanvas.create_text(
        126.0,
        243.0,
        anchor="nw",
        text="Society_ID: ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addSocietyCanvas.create_text(
        405.0,
        243.0,
        anchor="nw",
        text="City: ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addSocietyCanvas.create_text(
        96.0,
        315.0,
        anchor="nw",
        text="Society Name: ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    AddSocietyIDEntry_img = PhotoImage(
        file=relative_to_assets_addSociety("entry_1.png"))
    addSocietyCanvas.create_image(
        287.0,
        257.5,
        image=AddSocietyIDEntry_img
    )
    AddSocietyIDEntry = Entry(
        addSocietyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    AddSocietyIDEntry.place(
        x=261.0,
        y=243.0,
        width=52.0,
        height=27.0
    )

    addSocietyCanvas.create_text(
        102.0,
        394.0,
        anchor="nw",
        text="No.of Houses",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addSocietyCityEntry_img = PhotoImage(
        file=relative_to_assets_addSociety("entry_2.png"))
    addSocietyCanvas.create_image(
        294.0,
        402.5,
        image=addSocietyCityEntry_img
    )
    addSocietyCityEntry = Entry(
        addSocietyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addSocietyCityEntry.place(
        x=261.0,
        y=388.0,
        width=66.0,
        height=27.0
    )

    addSocietyCanvas.create_text(
        405.0,
        394.0,
        anchor="nw",
        text="No.of Plots: ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addSocietyNameEntry_img = PhotoImage(
        file=relative_to_assets_addSociety("entry_3.png"))
    addSocietyCanvas.create_image(
        586.0,
        402.5,
        image=addSocietyNameEntry_img
    )
    addSocietyNameEntry = Entry(
        addSocietyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addSocietyNameEntry.place(
        x=554.0,
        y=388.0,
        width=64.0,
        height=27.0
    )

    addSocietyNoofHousesEntry_img = PhotoImage(
        file=relative_to_assets_addSociety("entry_4.png"))
    addSocietyCanvas.create_image(
        580.0,
        257.5,
        image=addSocietyNoofHousesEntry_img
    )
    addSocietyNoofHousesEntry = Entry(
        addSocietyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addSocietyNoofHousesEntry.place(
        x=512.0,
        y=243.0,
        width=136.0,
        height=27.0
    )

    addSocietyNoofPlotsEntry_img = PhotoImage(
        file=relative_to_assets_addSociety("entry_5.png"))
    addSocietyCanvas.create_image(
        454.5,
        331.0,
        image=addSocietyNoofPlotsEntry_img
    )
    addSocietyNoofPlotsEntry = Entry(
        addSocietyWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    addSocietyNoofPlotsEntry.place(
        x=261.0,
        y=315.0,
        width=387.0,
        height=30.0
    )

    BackBtn_img = PhotoImage(
        file=relative_to_assets_addSociety("button_1.png"))
    BackBtn = Button(
        addSocietyWindow,
        image=BackBtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(addSocietyWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    Submitbtn_img = PhotoImage(
        file=relative_to_assets_addSociety("button_2.png"))
    Submitbtn = Button(
        addSocietyWindow,
        image=Submitbtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Submitbtn clicked"),
        relief="flat"
    )
    Submitbtn.place(
        
        x=627.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    addSocietyWindow.mainloop()

