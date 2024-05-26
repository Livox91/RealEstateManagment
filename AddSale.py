from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame13")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()

def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_addSale(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def addSale_window():
    addSaleWindow = Toplevel()

    addSaleWindow.geometry("800x600")
    addSaleWindow.configure(bg = "#FFFFFF")


    AddSaleCanvas = Canvas(
        addSaleWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    AddSaleCanvas.place(x = 0, y = 0)
    addSaleLogo = PhotoImage(
        file=relative_to_assets_addSale("image_1.png"))
    AddSaleCanvas.create_image(
        120.0,
        80.0,
        image=addSaleLogo
    )

    AddSaleCanvas.create_text(
        304.0,
        51.0,
        anchor="nw",
        text="ADD Listing Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )
    AddSaleCanvas.create_text(
        132.0,
        234.0,
        anchor="nw",
        text="Listing_Id",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )
    AddSaleCanvas.create_text(
        114.0,
        286.0,
        anchor="nw",
        text="Property_Id ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )
    AddSaleCanvas.create_text(
        114.0,
        340.0,
        anchor="nw",
        text="Listing Date",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    listingId_entry_img = PhotoImage(
        file=relative_to_assets_addSale("entry_1.png"))
    AddSaleCanvas.create_image(
        304.0,
        248.5,
        image=listingId_entry_img
    )
    listingId_entry = Entry(
        addSaleWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    listingId_entry.place(
        x=278.0,
        y=234.0,
        width=52.0,
        height=27.0
    )

    AddSaleCanvas.create_text(
        484.0,
        234.0,
        anchor="nw",
        text="Sale ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    saleId_entry_img = PhotoImage(
        file=relative_to_assets_addSale("entry_2.png"))
    AddSaleCanvas.create_image(
        626.0,
        248.5,
        image=saleId_entry_img
    )
    saleId_entry = Entry(
        addSaleWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    saleId_entry.place(
        x=600.0,
        y=234.0,
        width=52.0,
        height=27.0
    )

    AddSaleCanvas.create_text(
        477.0,
        286.0,
        anchor="nw",
        text="Client ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    clientId_entry_img = PhotoImage(
        file=relative_to_assets_addSale("entry_3.png"))
    AddSaleCanvas.create_image(
        626.0,
        300.5,
        image=clientId_entry_img
    )
    clientId_entry = Entry(
        addSaleWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    clientId_entry.place(
        x=600.0,
        y=286.0,
        width=52.0,
        height=27.0
    )

    AddSaleCanvas.create_text(
        492.0,
        338.0,
        anchor="nw",
        text="Price",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    price_entry_img = PhotoImage(
        file=relative_to_assets_addSale("entry_4.png"))
    AddSaleCanvas.create_image(
        626.0,
        352.5,
        image=price_entry_img
    )
    price_entry = Entry(
        addSaleWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    price_entry.place(
        x=600.0,
        y=338.0,
        width=52.0,
        height=27.0
    )

    AddSaleCanvas.create_text(
        125.0,
        397.0,
        anchor="nw",
        text="Sale Date",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    saleDate_entry_img = PhotoImage(
        file=relative_to_assets_addSale("entry_5.png"))
    AddSaleCanvas.create_image(
        342.0,
        411.5,
        image=saleDate_entry_img
    )
    saleDate_entry = Entry(
        addSaleWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    saleDate_entry.place(
        x=276.0,
        y=397.0,
        width=132.0,
        height=27.0
    )

    propertyId_entry_img = PhotoImage(
        file=relative_to_assets_addSale("entry_6.png"))
    AddSaleCanvas.create_image(
        304.0,
        300.5,
        image=propertyId_entry_img
    )
    propertyId_entry = Entry(
        addSaleWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    propertyId_entry.place(
        x=278.0,
        y=286.0,
        width=52.0,
        height=27.0
    )

    listingDate_entry_img = PhotoImage(
        file=relative_to_assets_addSale("entry_7.png"))
    AddSaleCanvas.create_image(
        342.0,
        355.0,
        image=listingDate_entry_img
    )
    listingDate_entry = Entry(
        addSaleWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    listingDate_entry.place(
        x=276.0,
        y=338.0,
        width=132.0,
        height=32.0
    )

    BackBtn_ = PhotoImage(
        file=relative_to_assets_addSale("button_1.png"))
    BackBtn = Button(
        addSaleWindow,
        image=BackBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(addSaleWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=480.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_addSale("button_2.png"))
    SubmitBtn = Button(
        addSaleWindow,
        image=SubmitBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("SubmitBtn clicked"),
        relief="flat"
    )
    SubmitBtn.place(
        x=627.0,
        y=480.0,
        width=107.0,
        height=51.0
    )
    addSaleWindow.resizable(False, False)
    addSaleWindow.mainloop()
