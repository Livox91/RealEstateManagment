from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame11")


def relative_to_assets_Apartment(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def PropertyWindowModule():
    PropertyModule = importlib.import_module("Add.Property")
    PropertyModule.Property_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()

def Apartment_window():
    ApartmentWindow = Toplevel()
    ApartmentWindow.geometry("800x600")
    ApartmentWindow.configure(bg = "#FFFFFF")

    ApartmentCanvas = Canvas(
        ApartmentWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    ApartmentCanvas.place(x = 0, y = 0)
    ApartmentLogo = PhotoImage(
        file=relative_to_assets_Apartment("image_1.png"))
    ApartmentCanvas.create_image(
        120.0,
        80.0,
        image=ApartmentLogo
    )

    ApartmentCanvas.create_text(
        240.0,
        51.0,
        anchor="nw",
        text=" Apartment DATA",
        fill="#052561",
        font=("NirmalaUI Bold", 56 * -1)
    )

    ApartmentCanvas.create_text(
        144.0,
        229.0,
        anchor="nw",
        text="Title",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    ApartmentCanvas.create_text(
        422.0,
        189.0,
        anchor="nw",
        text="Area Size(sq.ft)",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    title_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_1.png"))
    ApartmentCanvas.create_image(
        421.5,
        252.0,
        image=title_entry_img
    )
    title_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    title_entry.place(
        x=260.0,
        y=236.0,
        width=323.0,
        height=30.0
    )

    ApartmentCanvas.create_text(
        126.0,
        279.0,
        anchor="nw",
        text="Location",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    location_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_2.png"))
    ApartmentCanvas.create_image(
        421.5,
        302.0,
        image=location_entry_img
    )
    location_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    location_entry.place(
        x=260.0,
        y=286.0,
        width=323.0,
        height=30.0
    )

    areaSize_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_3.png"))
    ApartmentCanvas.create_image(
        627.0,
        205.0,
        image=areaSize_entry_img
    )
    areaSize_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    areaSize_entry.place(
        x=593.0,
        y=189.0,
        width=68.0,
        height=30.0
    )

    ApartmentCanvas.create_text(
        109.0,
        336.0,
        anchor="nw",
        text="Society_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    societyID_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_4.png"))
    ApartmentCanvas.create_image(
        294.0,
        352.0,
        image=societyID_entry_img
    )
    societyID_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    societyID_entry.place(
        x=260.0,
        y=336.0,
        width=68.0,
        height=30.0
    )

    ApartmentCanvas.create_text(
        425.0,
        335.0,
        anchor="nw",
        text="Apartment ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    apartmentid_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_5.png"))
    ApartmentCanvas.create_image(
        625.0,
        351.0,
        image=apartmentid_entry_img
    )
    apartmentid_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    apartmentid_entry.place(
        x=591.0,
        y=335.0,
        width=68.0,
        height=30.0
    )

    ApartmentCanvas.create_text(
        104.0,
        392.0,
        anchor="nw",
        text="Building_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    buildingID_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_6.png"))
    ApartmentCanvas.create_image(
        294.0,
        408.0,
        image=buildingID_entry_img
    )
    buildingID_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    buildingID_entry.place(
        x=260.0,
        y=392.0,
        width=68.0,
        height=30.0
    )

    ApartmentCanvas.create_text(
        452.0,
        391.0,
        anchor="nw",
        text="Unit_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    unitId_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_7.png"))
    ApartmentCanvas.create_image(
        625.0,
        407.0,
        image=unitId_entry_img
    )
    unitId_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    unitId_entry.place(
        x=591.0,
        y=391.0,
        width=68.0,
        height=30.0
    )

    ApartmentCanvas.create_text(
        95.0,
        189.0,
        anchor="nw",
        text="Property_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    propertyid_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_8.png"))
    ApartmentCanvas.create_image(
        294.0,
        205.0,
        image=propertyid_entry_img
    )
    propertyid_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    propertyid_entry.place(
        x=260.0,
        y=189.0,
        width=68.0,
        height=30.0
    )

    BackBtn_ = PhotoImage(
        file=relative_to_assets_Apartment("button_1.png"))
    BackBtn = Button(
        ApartmentWindow,
        image=BackBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showPropertyWindow(ApartmentWindow),
        relief="flat"
    )
    BackBtn.place(
        x=67.0,
        y=514.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_Apartment("button_2.png"))
    SubmitBtn = Button(
        ApartmentWindow,
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

    ApartmentCanvas.create_text(
        109.0,
        443.0,
        anchor="nw",
        text="Floor Level",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    floorlvl_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_9.png"))
    ApartmentCanvas.create_image(
        268.0,
        456.0,
        image=floorlvl_entry_img
    )
    floorlvl_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    floorlvl_entry.place(
        x=234.0,
        y=440.0,
        width=68.0,
        height=30.0
    )

    ApartmentCanvas.create_text(
        332.0,
        443.0,
        anchor="nw",
        text="No.of Beds",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    NoBeds_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_10.png"))
    ApartmentCanvas.create_image(
        469.0,
        455.0,
        image=NoBeds_entry_img
    )
    NoBeds_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    NoBeds_entry.place(
        x=435.0,
        y=439.0,
        width=68.0,
        height=30.0
    )

    ApartmentCanvas.create_text(
        528.0,
        443.0,
        anchor="nw",
        text="No.of Baths",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    NoBath_entry_img = PhotoImage(
        file=relative_to_assets_Apartment("entry_11.png"))
    ApartmentCanvas.create_image(
        672.0,
        456.0,
        image=NoBath_entry_img
    )
    NoBath_entry = Entry(
        ApartmentWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    NoBath_entry.place(
        x=638.0,
        y=440.0,
        width=68.0,
        height=30.0
    )

    ApartmentWindow.resizable(False, False)
    ApartmentWindow.mainloop()
