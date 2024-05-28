from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame7")

def PropertyWindowModule():
    PropertyModule = importlib.import_module("Add.Property")
    PropertyModule.Property_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()
def relative_to_assets_House(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def House_window():
    HouseWindow = Toplevel()

    HouseWindow.geometry("800x600")
    HouseWindow.configure(bg = "#FFFFFF")


    HouseCanvas = Canvas(
        HouseWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    HouseCanvas.place(x = 0, y = 0)
    HouseLogo = PhotoImage(
        file=relative_to_assets_House("image_1.png"))
    HouseCanvas.create_image(
        120.0,
        80.0,
        image=HouseLogo
    )

    HouseCanvas.create_text(
        295.0,
        51.0,
        anchor="nw",
        text=" House DATA",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    HouseCanvas.create_text(
        144.0,
        229.0,
        anchor="nw",
        text="Title",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    HouseCanvas.create_text(
        422.0,
        189.0,
        anchor="nw",
        text="Area Size(sq.ft)",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    title_entry_img = PhotoImage(
        file=relative_to_assets_House("entry_1.png"))
    HouseCanvas.create_image(
        421.5,
        252.0,
        image=title_entry_img
    )
    title_entry = Entry(
        HouseWindow,
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

    HouseCanvas.create_text(
        126.0,
        279.0,
        anchor="nw",
        text="Location",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    location_entry_img = PhotoImage(
        file=relative_to_assets_House("entry_2.png"))
    HouseCanvas.create_image(
        421.5,
        302.0,
        image=location_entry_img
    )
    location_entry = Entry(
        HouseWindow,
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
        file=relative_to_assets_House("entry_3.png"))
    HouseCanvas.create_image(
        627.0,
        205.0,
        image=areaSize_entry_img
    )
    areaSize_entry = Entry(
        HouseWindow,
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

    HouseCanvas.create_text(
        109.0,
        336.0,
        anchor="nw",
        text="Society_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    societyId_entry_img = PhotoImage(
        file=relative_to_assets_House("entry_4.png"))
    HouseCanvas.create_image(
        294.0,
        352.0,
        image=societyId_entry_img
    )
    societyId_entry = Entry(
        HouseWindow,
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

    HouseCanvas.create_text(
        109.0,
        385.0,
        anchor="nw",
        text="House_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    houseId_entry_img = PhotoImage(
        file=relative_to_assets_House("entry_5.png"))
    HouseCanvas.create_image(
        294.0,
        408.0,
        image=houseId_entry_img
    )
    houseId_entry = Entry(
        HouseWindow,
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

    HouseCanvas.create_text(
        451.0,
        328.0,
        anchor="nw",
        text="No. of Beds",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    Beds_entry_img = PhotoImage(
        file=relative_to_assets_House("entry_6.png"))
    HouseCanvas.create_image(
        628.5,
        351.0,
        image=Beds_entry_img
    )
    Beds_entry = Entry(
        HouseWindow,
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

    HouseCanvas.create_text(
        444.0,
        385.0,
        anchor="nw",
        text="No. of Baths",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    baths_entry_img = PhotoImage(
        file=relative_to_assets_House("entry_7.png"))
    HouseCanvas.create_image(
        630.0,
        402.0,
        image=baths_entry_img
    )
    baths_entry = Entry(
        HouseWindow,
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

    HouseCanvas.create_text(
        95.0,
        189.0,
        anchor="nw",
        text="Property_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    propertyid_entry_img = PhotoImage(
        file=relative_to_assets_House("entry_8.png"))
    HouseCanvas.create_image(
        294.0,
        205.0,
        image=propertyid_entry_img
    )
    propertyid_entry = Entry(
        HouseWindow,
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
        file=relative_to_assets_House("button_1.png"))
    Backbtn = Button(
        HouseWindow,
        image=Backbtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showPropertyWindow(HouseWindow),
        relief="flat"
    )
    Backbtn.place(
        x=67.0,
        y=514.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_House("button_2.png"))
    SubmitBtn = Button(
        HouseWindow,
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
    HouseWindow.resizable(False, False)
    HouseWindow.mainloop()
