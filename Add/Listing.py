from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_LISTING = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame3")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()
def RentalWindowModule():
    RentalModule = importlib.import_module("Add.Rental")
    RentalModule.Rental_window()
def showRentalWindow(parent_window):
    parent_window.withdraw()
    RentalWindowModule()
def SaleWindowModule():
    SaleModule = importlib.import_module("Add.Sale")
    SaleModule.Sale_window()
def showSaleWindow(parent_window):
    parent_window.withdraw()
    SaleWindowModule()


def relative_to_assets_Listing(path: str) -> Path:
    return ASSETS_PATH_LISTING / Path(path)
def Listing_window():
    ListingWindow = Toplevel()

    ListingWindow.geometry("800x600")
    ListingWindow.configure(bg = "#FFFFFF")


    ListingCanvas = Canvas(
        ListingWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    ListingCanvas.place(x = 0, y = 0)
    ListingLogo = PhotoImage(
        file=relative_to_assets_Listing("image_1.png"))
    ListingCanvas.create_image(
        400.0,
        155.0,
        image=ListingLogo
    )

    _sale_listing = PhotoImage(
        file=relative_to_assets_Listing("button_1.png"))
    _sale_listing_ = Button(
        ListingWindow,
        image=_sale_listing,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showSaleWindow(ListingWindow),
        relief="flat"
    )
    _sale_listing_.place(
        x=262.0,
        y=415.0,
        width=75.0,
        height=25.0
    )

    _rental_listing = PhotoImage(
        file=relative_to_assets_Listing("button_2.png"))
    _rental_listing_ = Button(
        ListingWindow,
        image=_rental_listing,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showRentalWindow(ListingWindow),
        relief="flat"
    )
    _rental_listing_.place(
        x=483.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    ListingCanvas.create_text(
        337.0,
        347.0,
        anchor="nw",
        text=" Listing",
        fill="#000000",
        font=("Lexend Regular", 26 * -1)
    )

    BackBtn = PhotoImage(
        file=relative_to_assets_Listing("button_3.png"))
    BackBtn_ = Button(
        ListingWindow,
        image=BackBtn,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(ListingWindow),
        relief="flat"
    )
    BackBtn_.place(
        x=84.0,
        y=500.0,
        width=107.0,
        height=51.0
    )

    ListingWindow.resizable(False, False)
    ListingWindow.mainloop()
