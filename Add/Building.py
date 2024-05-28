from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame8")


def relative_to_assets_Building(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def PropertyWindowModule():
    PropertyModule = importlib.import_module("Add.Property")
    PropertyModule.Property_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()

def Building_window():
    BuildingWindow = Toplevel()

    BuildingWindow.geometry("800x600")
    BuildingWindow.configure(bg = "#FFFFFF")


    BuildingCanvas = Canvas(
        BuildingWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    BuildingCanvas.place(x = 0, y = 0)
    BuildingLogo = PhotoImage(
        file=relative_to_assets_Building("image_1.png"))
    BuildingCanvas.create_image(
        120.0,
        80.0,
        image=BuildingLogo
    )

    BuildingCanvas.create_text(
        272.0,
        51.0,
        anchor="nw",
        text=" Building DATA",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    BuildingCanvas.create_text(
        109.0,
        205.0,
        anchor="nw",
        text="Society_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    societyID_entry_img = PhotoImage(
        file=relative_to_assets_Building("entry_1.png"))
    BuildingCanvas.create_image(
        294.0,
        221.0,
        image=societyID_entry_img
    )
    societyID_entry = Entry(
        BuildingWindow,
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

    BuildingCanvas.create_text(
        101.0,
        254.0,
        anchor="nw",
        text="Building_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    buildingID_entry_img = PhotoImage(
        file=relative_to_assets_Building("entry_2.png"))
    BuildingCanvas.create_image(
        294.0,
        270.0,
        image=buildingID_entry_img
    )
    buildingID_entry = Entry(
        BuildingWindow,
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

    BuildingCanvas.create_text(
        87.0,
        302.0,
        anchor="nw",
        text="Building Name",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    buildingName_entry_img = PhotoImage(
        file=relative_to_assets_Building("entry_3.png"))
    BuildingCanvas.create_image(
        423.5,
        317.0,
        image=buildingName_entry_img
    )
    buildingName_entry = Entry(
        BuildingWindow,
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

    BuildingCanvas.create_text(
        440.0,
        196.0,
        anchor="nw",
        text="No. of Shops",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    Noshops_entry_img = PhotoImage(
        file=relative_to_assets_Building("entry_4.png"))
    BuildingCanvas.create_image(
        627.0,
        212.0,
        image=Noshops_entry_img
    )
    Noshops_entry = Entry(
        BuildingWindow,
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

    BuildingCanvas.create_text(
        399.0,
        254.0,
        anchor="nw",
        text="No. of Apartment",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    Noapartments_entry_img = PhotoImage(
        file=relative_to_assets_Building("entry_5.png"))
    BuildingCanvas.create_image(
        627.0,
        270.0,
        image=Noapartments_entry_img
    )
    Noapartments_entry = Entry(
        BuildingWindow,
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
        file=relative_to_assets_Building("button_1.png"))
    BackBtn = Button(
        BuildingWindow,
        image= BackBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showPropertyWindow(BuildingWindow),
        relief="flat"
    )
    BackBtn.place(
        x=67.0,
        y=514.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_Building("button_2.png"))
    SubmitBtn = Button(
        BuildingWindow,
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

    BuildingCanvas.create_text(
        130.0,
        352.0,
        anchor="nw",
        text="Location",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    location_entry_img = PhotoImage(
        file=relative_to_assets_Building("entry_6.png"))
    BuildingCanvas.create_image(
        425.5,
        375.0,
        image=location_entry_img
    )
    location_entry = Entry(
        BuildingWindow,
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
   
    BuildingWindow.resizable(False, False)
    BuildingWindow.mainloop()
