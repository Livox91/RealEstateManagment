from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame11")


def relative_to_assets_addApartment(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def PropertyWindowModule():
    PropertyModule = importlib.import_module("AddProperty")
    PropertyModule.addProperty_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()

def addApartment_window():
    addApartmentWindow = Toplevel()
    addApartmentWindow.geometry("800x600")
    addApartmentWindow.configure(bg = "#FFFFFF")

    AddApartmentCanvas = Canvas(
        addApartmentWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    AddApartmentCanvas.place(x = 0, y = 0)
    addApartmentLogo = PhotoImage(
        file=relative_to_assets_addApartment("image_1.png"))
    AddApartmentCanvas.create_image(
        120.0,
        80.0,
        image=addApartmentLogo
    )

    AddApartmentCanvas.create_text(
        240.0,
        51.0,
        anchor="nw",
        text="ADD Apartment DATA",
        fill="#052561",
        font=("NirmalaUI Bold", 56 * -1)
    )

    AddApartmentCanvas.create_text(
        144.0,
        229.0,
        anchor="nw",
        text="Title",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    AddApartmentCanvas.create_text(
        422.0,
        189.0,
        anchor="nw",
        text="Area Size(sq.ft)",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    title_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_1.png"))
    AddApartmentCanvas.create_image(
        421.5,
        252.0,
        image=title_entry_img
    )
    title_entry = Entry(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        126.0,
        279.0,
        anchor="nw",
        text="Location",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    location_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_2.png"))
    AddApartmentCanvas.create_image(
        421.5,
        302.0,
        image=location_entry_img
    )
    location_entry = Entry(
        addApartmentWindow,
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
        file=relative_to_assets_addApartment("entry_3.png"))
    AddApartmentCanvas.create_image(
        627.0,
        205.0,
        image=areaSize_entry_img
    )
    areaSize_entry = Entry(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        109.0,
        336.0,
        anchor="nw",
        text="Society_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    societyID_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_4.png"))
    AddApartmentCanvas.create_image(
        294.0,
        352.0,
        image=societyID_entry_img
    )
    societyID_entry = Entry(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        425.0,
        335.0,
        anchor="nw",
        text="Apartment ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    apartmentid_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_5.png"))
    AddApartmentCanvas.create_image(
        625.0,
        351.0,
        image=apartmentid_entry_img
    )
    apartmentid_entry = Entry(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        104.0,
        392.0,
        anchor="nw",
        text="Building_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    buildingID_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_6.png"))
    AddApartmentCanvas.create_image(
        294.0,
        408.0,
        image=buildingID_entry_img
    )
    buildingID_entry = Entry(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        452.0,
        391.0,
        anchor="nw",
        text="Unit_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    unitId_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_7.png"))
    AddApartmentCanvas.create_image(
        625.0,
        407.0,
        image=unitId_entry_img
    )
    unitId_entry = Entry(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        95.0,
        189.0,
        anchor="nw",
        text="Property_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    propertyid_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_8.png"))
    AddApartmentCanvas.create_image(
        294.0,
        205.0,
        image=propertyid_entry_img
    )
    propertyid_entry = Entry(
        addApartmentWindow,
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
        file=relative_to_assets_addApartment("button_1.png"))
    BackBtn = Button(
        addApartmentWindow,
        image=BackBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showPropertyWindow(addApartmentWindow),
        relief="flat"
    )
    BackBtn.place(
        x=67.0,
        y=514.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_addApartment("button_2.png"))
    SubmitBtn = Button(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        109.0,
        443.0,
        anchor="nw",
        text="Floor Level",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    floorlvl_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_9.png"))
    AddApartmentCanvas.create_image(
        268.0,
        456.0,
        image=floorlvl_entry_img
    )
    floorlvl_entry = Entry(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        332.0,
        443.0,
        anchor="nw",
        text="No.of Beds",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    NoBeds_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_10.png"))
    AddApartmentCanvas.create_image(
        469.0,
        455.0,
        image=NoBeds_entry_img
    )
    NoBeds_entry = Entry(
        addApartmentWindow,
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

    AddApartmentCanvas.create_text(
        528.0,
        443.0,
        anchor="nw",
        text="No.of Baths",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    NoBath_entry_img = PhotoImage(
        file=relative_to_assets_addApartment("entry_11.png"))
    AddApartmentCanvas.create_image(
        672.0,
        456.0,
        image=NoBath_entry_img
    )
    NoBath_entry = Entry(
        addApartmentWindow,
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

    addApartmentWindow.resizable(False, False)
    addApartmentWindow.mainloop()
