from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_ADDLISTING = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame3")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()
def RentalWindowModule():
    RentalModule = importlib.import_module("AddRental")
    RentalModule.addRental_window()
def showaddRentalWindow(parent_window):
    parent_window.withdraw()
    RentalWindowModule()
def SaleWindowModule():
    SaleModule = importlib.import_module("AddSale")
    SaleModule.addSale_window()
def showaddSaleWindow(parent_window):
    parent_window.withdraw()
    SaleWindowModule()


def relative_to_assets_addListing(path: str) -> Path:
    return ASSETS_PATH_ADDLISTING / Path(path)
def addListing_window():
    addListingWindow = Toplevel()

    addListingWindow.geometry("800x600")
    addListingWindow.configure(bg = "#FFFFFF")


    addListingCanvas = Canvas(
        addListingWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    addListingCanvas.place(x = 0, y = 0)
    addListingLogo = PhotoImage(
        file=relative_to_assets_addListing("image_1.png"))
    addListingCanvas.create_image(
        400.0,
        155.0,
        image=addListingLogo
    )

    add_sale_listing = PhotoImage(
        file=relative_to_assets_addListing("button_1.png"))
    add_sale_listing_ = Button(
        addListingWindow,
        image=add_sale_listing,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showaddSaleWindow(addListingWindow),
        relief="flat"
    )
    add_sale_listing_.place(
        x=262.0,
        y=415.0,
        width=75.0,
        height=25.0
    )

    add_rental_listing = PhotoImage(
        file=relative_to_assets_addListing("button_2.png"))
    add_rental_listing_ = Button(
        addListingWindow,
        image=add_rental_listing,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showaddRentalWindow(addListingWindow),
        relief="flat"
    )
    add_rental_listing_.place(
        x=483.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    addListingCanvas.create_text(
        337.0,
        347.0,
        anchor="nw",
        text="Add Listing",
        fill="#000000",
        font=("Lexend Regular", 26 * -1)
    )

    BackBtn = PhotoImage(
        file=relative_to_assets_addListing("button_3.png"))
    BackBtn_ = Button(
        addListingWindow,
        image=BackBtn,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(addListingWindow),
        relief="flat"
    )
    BackBtn_.place(
        x=84.0,
        y=500.0,
        width=107.0,
        height=51.0
    )

    addListingWindow.resizable(False, False)
    addListingWindow.mainloop()
