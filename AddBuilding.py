from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame8")


def relative_to_assets_addBuilding(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def PropertyWindowModule():
    PropertyModule = importlib.import_module("AddProperty")
    PropertyModule.addProperty_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()

def addBuilding_window():
    addBuildingWindow = Toplevel()

    addBuildingWindow.geometry("800x600")
    addBuildingWindow.configure(bg = "#FFFFFF")


    AddBuildingCanvas = Canvas(
        addBuildingWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    AddBuildingCanvas.place(x = 0, y = 0)
    addBuildingLogo = PhotoImage(
        file=relative_to_assets_addBuilding("image_1.png"))
    AddBuildingCanvas.create_image(
        120.0,
        80.0,
        image=addBuildingLogo
    )

    AddBuildingCanvas.create_text(
        272.0,
        51.0,
        anchor="nw",
        text="ADD Building DATA",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    AddBuildingCanvas.create_text(
        109.0,
        205.0,
        anchor="nw",
        text="Society_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    societyID_entry_img = PhotoImage(
        file=relative_to_assets_addBuilding("entry_1.png"))
    AddBuildingCanvas.create_image(
        294.0,
        221.0,
        image=societyID_entry_img
    )
    societyID_entry = Entry(
        addBuildingWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    societyID_entry.place(
        x=260.0,
        y=205.0,
        width=68.0,
        height=30.0
    )

    AddBuildingCanvas.create_text(
        101.0,
        254.0,
        anchor="nw",
        text="Building_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    buildingID_entry_img = PhotoImage(
        file=relative_to_assets_addBuilding("entry_2.png"))
    AddBuildingCanvas.create_image(
        294.0,
        270.0,
        image=buildingID_entry_img
    )
    buildingID_entry = Entry(
        addBuildingWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    buildingID_entry.place(
        x=260.0,
        y=254.0,
        width=68.0,
        height=30.0
    )

    AddBuildingCanvas.create_text(
        87.0,
        302.0,
        anchor="nw",
        text="Building Name",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    buildingName_entry_img = PhotoImage(
        file=relative_to_assets_addBuilding("entry_3.png"))
    AddBuildingCanvas.create_image(
        423.5,
        317.0,
        image=buildingName_entry_img
    )
    buildingName_entry = Entry(
        addBuildingWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    buildingName_entry.place(
        x=260.0,
        y=301.0,
        width=327.0,
        height=30.0
    )

    AddBuildingCanvas.create_text(
        440.0,
        196.0,
        anchor="nw",
        text="No. of Shops",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    Noshops_entry_img = PhotoImage(
        file=relative_to_assets_addBuilding("entry_4.png"))
    AddBuildingCanvas.create_image(
        627.0,
        212.0,
        image=Noshops_entry_img
    )
    Noshops_entry = Entry(
        addBuildingWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    Noshops_entry.place(
        x=593.0,
        y=196.0,
        width=68.0,
        height=30.0
    )

    AddBuildingCanvas.create_text(
        399.0,
        254.0,
        anchor="nw",
        text="No. of Apartment",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    Noapartments_entry_img = PhotoImage(
        file=relative_to_assets_addBuilding("entry_5.png"))
    AddBuildingCanvas.create_image(
        627.0,
        270.0,
        image=Noapartments_entry_img
    )
    Noapartments_entry = Entry(
        addBuildingWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    Noapartments_entry.place(
        x=593.0,
        y=254.0,
        width=68.0,
        height=30.0
    )

    BackBtn_ = PhotoImage(
        file=relative_to_assets_addBuilding("button_1.png"))
    BackBtn = Button(
        addBuildingWindow,
        image= BackBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showPropertyWindow(addBuildingWindow),
        relief="flat"
    )
    BackBtn.place(
        x=67.0,
        y=514.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_addBuilding("button_2.png"))
    SubmitBtn = Button(
        addBuildingWindow,
        image=SubmitBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("SubmitBtn clicked"),
        relief="flat"
    )
    SubmitBtn.place(
        x=627.0,
        y=509.0,
        width=107.0,
        height=51.0
    )

    AddBuildingCanvas.create_text(
        130.0,
        352.0,
        anchor="nw",
        text="Location",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    location_entry_img = PhotoImage(
        file=relative_to_assets_addBuilding("entry_6.png"))
    AddBuildingCanvas.create_image(
        425.5,
        375.0,
        image=location_entry_img
    )
    location_entry = Entry(
        addBuildingWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    location_entry.place(
        x=264.0,
        y=359.0,
        width=323.0,
        height=30.0
    )
   
    addBuildingWindow.resizable(False, False)
    addBuildingWindow.mainloop()
