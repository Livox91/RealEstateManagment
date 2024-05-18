from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_ADDAGENT = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame4")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_addAgent(path: str) -> Path:
    return ASSETS_PATH_ADDAGENT / Path(path)
def addAgent_window():
    addAgentWindow = Toplevel()
    addAgentWindow.geometry("800x600")
    addAgentWindow.configure(bg = "#FFFFFF")

    addAgentCanvas = Canvas(
        addAgentWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    addAgentCanvas.place(x = 0, y = 0)
    addAgentLogo = PhotoImage(
        file=relative_to_assets_addAgent("image_1.png"))
    addAgentCanvas.create_image(
        120.0,
        80.0,
        image=addAgentLogo
    )

    addAgentCanvas.create_text(
        309.0,
        51.0,
        anchor="nw",
        text="ADD Agent Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    addAgentCanvas.create_text(
        106.0,
        250.0,
        anchor="nw",
        text="Agent_id:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addAgentCanvas.create_text(
        77.0,
        357.0,
        anchor="nw",
        text="Agent Name:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addAgentIDEntry_img = PhotoImage(
        file=relative_to_assets_addAgent("entry_1.png"))
    addAgentCanvas.create_image(
        295.0,
        266.0,
        image=addAgentIDEntry_img
    )
    addAgentIDEntry = Entry(
        addAgentWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addAgentIDEntry.place(
        x=261.0,
        y=250.0,
        width=68.0,
        height=30.0
    )

    addAgentCanvas.create_text(
        102.0,
        304.0,
        anchor="nw",
        text="Agency_Id",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addAgentNameEntry_img = PhotoImage(
        file=relative_to_assets_addAgent("entry_2.png"))
    addAgentCanvas.create_image(
        295.0,
        320.0,
        image=addAgentNameEntry_img
    )
    addAgentNameEntry = Entry(
        addAgentWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addAgentNameEntry.place(
        x=261.0,
        y=304.0,
        width=68.0,
        height=30.0
    )

    addAgentContactEntry_img = PhotoImage(
        file=relative_to_assets_addAgent("entry_3.png"))
    addAgentCanvas.create_image(
        626.0,
        266.0,
        image=addAgentContactEntry_img
    )
    addAgentContactEntry = Entry(
        addAgentWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addAgentContactEntry.place(
        x=592.0,
        y=250.0,
        width=68.0,
        height=30.0
    )

    addAgentSocietyIdEntry_img = PhotoImage(
        file=relative_to_assets_addAgent("entry_4.png"))
    addAgentCanvas.create_image(
        419.5,
        373.0,
        image=addAgentSocietyIdEntry_img
    )
    addAgentSocietyIdEntry = Entry(
        addAgentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    addAgentSocietyIdEntry.place(
        x=258.0,
        y=357.0,
        width=323.0,
        height=30.0
    )

    addAgentCanvas.create_text(
        119.0,
        415.0,
        anchor="nw",
        text="Contact:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addAgentCanvas.create_text(
        385.0,
        245.0,
        anchor="nw",
        text="Affliated Society_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addAgentAgencyIDEntry_img = PhotoImage(
        file=relative_to_assets_addAgent("entry_5.png"))
    addAgentCanvas.create_image(
        419.5,
        431.0,
        image=addAgentAgencyIDEntry_img
    )
    addAgentAgencyIDEntry = Entry(
        addAgentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    addAgentAgencyIDEntry.place(
        x=258.0,
        y=415.0,
        width=323.0,
        height=30.0
    )
    BackBtn_img = PhotoImage(
        file=relative_to_assets_addAgent("button_1.png"))
    BackBtn = Button(
        addAgentWindow,
        image=BackBtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(addAgentWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=472.0,
        width=107.0,
        height=51.0
    )
    def getValue():
        name = addAgentNameEntry.get()
        print(name)
    
    Submitbtn_img = PhotoImage(
        file=relative_to_assets_addAgent("button_2.png"))
    Submitbtn = Button(
        addAgentWindow,
        image=Submitbtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: getValue(),
        relief="flat"
    )
    Submitbtn.place(
        
        x=627.0,
        y=472.0,
        width=107.0,
        height=51.0
    )
    addAgentWindow.mainloop()
