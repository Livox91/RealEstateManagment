import importlib
from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_SOCIETY = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame5")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_Society(path: str) -> Path:
    return ASSETS_PATH_SOCIETY / Path(path)
def Society_window():
    SocietyWindow = Toplevel()
    SocietyWindow.geometry("800x600")
    SocietyWindow.configure(bg = "#FFFFFF")

    SocietyCanvas = Canvas(
        SocietyWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    SocietyCanvas.place(x = 0, y = 0)
    SocietyLogo = PhotoImage(
        file=relative_to_assets_Society("image_1.png"))
    SocietyCanvas.create_image(
        120.0,
        80.0,
        image=SocietyLogo
    )

    SocietyCanvas.create_text(
        296.0,
        51.0,
        anchor="nw",
        text=" Society Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    SocietyCanvas.create_text(
        126.0,
        243.0,
        anchor="nw",
        text="Society_ID: ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    SocietyCanvas.create_text(
        405.0,
        243.0,
        anchor="nw",
        text="City: ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    SocietyCanvas.create_text(
        96.0,
        315.0,
        anchor="nw",
        text="Society Name: ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    SocietyIDEntry_img = PhotoImage(
        file=relative_to_assets_Society("entry_1.png"))
    SocietyCanvas.create_image(
        287.0,
        257.5,
        image=SocietyIDEntry_img
    )
    SocietyIDEntry = Entry(
        SocietyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    SocietyIDEntry.place(
        x=261.0,
        y=243.0,
        width=52.0,
        height=27.0
    )

    SocietyCanvas.create_text(
        102.0,
        394.0,
        anchor="nw",
        text="No.of Houses",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    SocietyCityEntry_img = PhotoImage(
        file=relative_to_assets_Society("entry_2.png"))
    SocietyCanvas.create_image(
        294.0,
        402.5,
        image=SocietyCityEntry_img
    )
    SocietyCityEntry = Entry(
        SocietyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    SocietyCityEntry.place(
        x=261.0,
        y=388.0,
        width=66.0,
        height=27.0
    )

    SocietyCanvas.create_text(
        405.0,
        394.0,
        anchor="nw",
        text="No.of Plots: ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    SocietyNameEntry_img = PhotoImage(
        file=relative_to_assets_Society("entry_3.png"))
    SocietyCanvas.create_image(
        586.0,
        402.5,
        image=SocietyNameEntry_img
    )
    SocietyNameEntry = Entry(
        SocietyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    SocietyNameEntry.place(
        x=554.0,
        y=388.0,
        width=64.0,
        height=27.0
    )

    SocietyNoofHousesEntry_img = PhotoImage(
        file=relative_to_assets_Society("entry_4.png"))
    SocietyCanvas.create_image(
        580.0,
        257.5,
        image=SocietyNoofHousesEntry_img
    )
    SocietyNoofHousesEntry = Entry(
        SocietyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    SocietyNoofHousesEntry.place(
        x=512.0,
        y=243.0,
        width=136.0,
        height=27.0
    )

    SocietyNoofPlotsEntry_img = PhotoImage(
        file=relative_to_assets_Society("entry_5.png"))
    SocietyCanvas.create_image(
        454.5,
        331.0,
        image=SocietyNoofPlotsEntry_img
    )
    SocietyNoofPlotsEntry = Entry(
        SocietyWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    SocietyNoofPlotsEntry.place(
        x=261.0,
        y=315.0,
        width=387.0,
        height=30.0
    )

    BackBtn_img = PhotoImage(
        file=relative_to_assets_Society("button_1.png"))
    BackBtn = Button(
        SocietyWindow,
        image=BackBtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(SocietyWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    Submitbtn_img = PhotoImage(
        file=relative_to_assets_Society("button_2.png"))
    Submitbtn = Button(
        SocietyWindow,
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

    SocietyWindow.mainloop()

