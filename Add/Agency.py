import importlib
from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import Functionality.add_agency

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_AGENCY = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame2")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_agency(path: str) -> Path:
    return ASSETS_PATH_AGENCY / Path(path)
def Agency_window():
    AgencyWindow = Toplevel()
    AgencyWindow.geometry("800x600")
    AgencyWindow.configure(bg = "#FFFFFF")

    AgencyCanvas = Canvas(
        AgencyWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    AgencyCanvas.place(x = 0, y = 0)
    AgencyLogo = PhotoImage(
        file=relative_to_assets_agency("image_1.png"))
    AgencyCanvas.create_image(
        120.0,
        80.0,
        image=AgencyLogo
    )
    AgencyCanvas.create_text(
        292.0,
        51.0,
        anchor="nw",
        text=" Agency Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )
    AgencyCanvas.create_text(
        74.0,
        243.0,
        anchor="nw",
        text="Agency_Id:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )
    AgencyCanvas.create_text(
        51.0,
        318.0,
        anchor="nw",
        text="Agency_Name:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    AgencyIDEntry_img = PhotoImage(
        file=relative_to_assets_agency("entry_1.png"))
    AgencyCanvas.create_image(
        422.5,
        266.0,
        image=AgencyIDEntry_img
    )
    AgencyIDEntry = Entry(
        AgencyWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    AgencyIDEntry.place(
        x=261.0,
        y=250.0,
        width=323.0,
        height=30.0
    )

    AgencyNameEntry_img = PhotoImage(
        file=relative_to_assets_agency("entry_2.png"))
    AgencyCanvas.create_image(
        422.5,
        341.0,
        image=AgencyNameEntry_img
    )
    AgencyName_entry = Entry(
        AgencyWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    AgencyName_entry.place(
        x=261.0,
        y=325.0,
        width=323.0,
        height=30.0
    )

    BackBtn_img = PhotoImage(
        file=relative_to_assets_agency("button_1.png"))
    BackBtn = Button(
        AgencyWindow,
        image=BackBtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(AgencyWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    Submitbtn_img = PhotoImage(
        file=relative_to_assets_agency("button_2.png"))
    Submitbtn = Button(
        AgencyWindow,
        image=Submitbtn_img,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: add(),
        relief="flat"
    )
    Submitbtn.place(
        
        x=627.0,
        y=472.0,
        width=107.0,
        height=51.0
    )
   
    def add():
        name = AgencyName_entry.get()
        id = AgencyIDEntry.get()
        Functionality.add_agency.add_agency(name=name,id=id)

    AgencyWindow.mainloop()
