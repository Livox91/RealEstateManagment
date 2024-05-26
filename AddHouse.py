from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame7")

def PropertyWindowModule():
    PropertyModule = importlib.import_module("AddProperty")
    PropertyModule.addProperty_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()
def relative_to_assets_addHouse(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def addHouse_window():
    addHouseWindow = Toplevel()

    addHouseWindow.geometry("800x600")
    addHouseWindow.configure(bg = "#FFFFFF")


    AddHouseCanvas = Canvas(
        addHouseWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    AddHouseCanvas.place(x = 0, y = 0)
    addHouseLogo = PhotoImage(
        file=relative_to_assets_addHouse("image_1.png"))
    AddHouseCanvas.create_image(
        120.0,
        80.0,
        image=addHouseLogo
    )

    AddHouseCanvas.create_text(
        295.0,
        51.0,
        anchor="nw",
        text="ADD House DATA",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    AddHouseCanvas.create_text(
        144.0,
        229.0,
        anchor="nw",
        text="Title",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    AddHouseCanvas.create_text(
        422.0,
        189.0,
        anchor="nw",
        text="Area Size(sq.ft)",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    title_entry_img = PhotoImage(
        file=relative_to_assets_addHouse("entry_1.png"))
    AddHouseCanvas.create_image(
        421.5,
        252.0,
        image=title_entry_img
    )
    title_entry = Entry(
        addHouseWindow,
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

    AddHouseCanvas.create_text(
        126.0,
        279.0,
        anchor="nw",
        text="Location",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    location_entry_img = PhotoImage(
        file=relative_to_assets_addHouse("entry_2.png"))
    AddHouseCanvas.create_image(
        421.5,
        302.0,
        image=location_entry_img
    )
    location_entry = Entry(
        addHouseWindow,
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
        file=relative_to_assets_addHouse("entry_3.png"))
    AddHouseCanvas.create_image(
        627.0,
        205.0,
        image=areaSize_entry_img
    )
    areaSize_entry = Entry(
        addHouseWindow,
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

    AddHouseCanvas.create_text(
        109.0,
        336.0,
        anchor="nw",
        text="Society_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    societyId_entry_img = PhotoImage(
        file=relative_to_assets_addHouse("entry_4.png"))
    AddHouseCanvas.create_image(
        294.0,
        352.0,
        image=societyId_entry_img
    )
    societyId_entry = Entry(
        addHouseWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    societyId_entry.place(
        x=260.0,
        y=336.0,
        width=68.0,
        height=30.0
    )

    AddHouseCanvas.create_text(
        109.0,
        385.0,
        anchor="nw",
        text="House_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    houseId_entry_img = PhotoImage(
        file=relative_to_assets_addHouse("entry_5.png"))
    AddHouseCanvas.create_image(
        294.0,
        408.0,
        image=houseId_entry_img
    )
    houseId_entry = Entry(
        addHouseWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    houseId_entry.place(
        x=260.0,
        y=392.0,
        width=68.0,
        height=30.0
    )

    AddHouseCanvas.create_text(
        451.0,
        328.0,
        anchor="nw",
        text="No. of Beds",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    Beds_entry_img = PhotoImage(
        file=relative_to_assets_addHouse("entry_6.png"))
    AddHouseCanvas.create_image(
        628.5,
        351.0,
        image=Beds_entry_img
    )
    Beds_entry = Entry(
        addHouseWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    Beds_entry.place(
        x=593.0,
        y=335.0,
        width=71.0,
        height=30.0
    )

    AddHouseCanvas.create_text(
        444.0,
        385.0,
        anchor="nw",
        text="No. of Baths",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    baths_entry_img = PhotoImage(
        file=relative_to_assets_addHouse("entry_7.png"))
    AddHouseCanvas.create_image(
        630.0,
        402.0,
        image=baths_entry_img
    )
    baths_entry = Entry(
        addHouseWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    baths_entry.place(
        x=596.0,
        y=386.0,
        width=68.0,
        height=30.0
    )

    AddHouseCanvas.create_text(
        95.0,
        189.0,
        anchor="nw",
        text="Property_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    propertyid_entry_img = PhotoImage(
        file=relative_to_assets_addHouse("entry_8.png"))
    AddHouseCanvas.create_image(
        294.0,
        205.0,
        image=propertyid_entry_img
    )
    propertyid_entry = Entry(
        addHouseWindow,
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

    Backbtn_ = PhotoImage(
        file=relative_to_assets_addHouse("button_1.png"))
    Backbtn = Button(
        addHouseWindow,
        image=Backbtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showPropertyWindow(addHouseWindow),
        relief="flat"
    )
    Backbtn.place(
        x=67.0,
        y=514.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_addHouse("button_2.png"))
    SubmitBtn = Button(
        addHouseWindow,
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
    addHouseWindow.resizable(False, False)
    addHouseWindow.mainloop()
