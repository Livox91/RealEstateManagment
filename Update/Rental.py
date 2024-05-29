from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib
import Update.Update
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame12")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()

def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()


def relative_to_assets_Rental(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Rental_window():
    UpdateWindow = Update.Update.UpdateScreen()
    RentalWindow = Toplevel()
    RentalWindow.geometry("800x600")
    RentalWindow.configure(bg = "#FFFFFF")

    RentalCanvas = Canvas(
        RentalWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    RentalCanvas.place(x = 0, y = 0)
    RentalLogo = PhotoImage(
        file=relative_to_assets_Rental("image_1.png"))
    RentalCanvas.create_image(
        120.0,
        80.0,
        image=RentalLogo
    )

    RentalCanvas.create_text(
        304.0,
        51.0,
        anchor="nw",
        text=" Listing Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    RentalCanvas.create_text(
        132.0,
        234.0,
        anchor="nw",
        text="Listing_Id",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    RentalCanvas.create_text(
        114.0,
        286.0,
        anchor="nw",
        text="Property_Id ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    RentalCanvas.create_text(
        114.0,
        340.0,
        anchor="nw",
        text="Listing Date",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    listingId_entry_img = PhotoImage(
        file=relative_to_assets_Rental("entry_1.png"))
    RentalCanvas.create_image(
        304.0,
        248.5,
        image=listingId_entry_img
    )
    listingId_entry = Entry(
        RentalWindow,
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

    RentalCanvas.create_text(
        475.0,
        234.0,
        anchor="nw",
        text="Rental ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    rentalId_entry_img = PhotoImage(
        file=relative_to_assets_Rental("entry_2.png"))
    RentalCanvas.create_image(
        626.0,
        248.5,
        image=rentalId_entry_img
    )
    rentalId_entry = Entry(
        RentalWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    rentalId_entry.place(
        x=600.0,
        y=234.0,
        width=52.0,
        height=27.0
    )

    RentalCanvas.create_text(
        477.0,
        286.0,
        anchor="nw",
        text="Client ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    clientId_entry_img = PhotoImage(
        file=relative_to_assets_Rental("entry_3.png"))
    RentalCanvas.create_image(
        626.0,
        300.5,
        image=clientId_entry_img
    )
    clientId_entry = Entry(
        RentalWindow,
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

    RentalCanvas.create_text(
        493.0,
        338.0,
        anchor="nw",
        text="Rent",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    rent_entry_img = PhotoImage(
        file=relative_to_assets_Rental("entry_4.png"))
    RentalCanvas.create_image(
        626.0,
        352.5,
        image=rent_entry_img
    )
    rent_entry = Entry(
        RentalWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    rent_entry.place(
        x=600.0,
        y=338.0,
        width=52.0,
        height=27.0
    )

    RentalCanvas.create_text(
        115.0,
        397.0,
        anchor="nw",
        text="Rental Date",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    rentalDate_entry_img = PhotoImage(
        file=relative_to_assets_Rental("entry_5.png"))
    RentalCanvas.create_image(
        342.0,
        411.5,
        image=rentalDate_entry_img
    )
    rentalDate_entry = Entry(
        RentalWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    rentalDate_entry.place(
        x=276.0,
        y=397.0,
        width=132.0,
        height=27.0
    )

    RentalCanvas.create_text(
        477.0,
        397.0,
        anchor="nw",
        text="Duration",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    duration_entry_img = PhotoImage(
        file=relative_to_assets_Rental("entry_6.png"))
    RentalCanvas.create_image(
        668.0,
        411.5,
        image=duration_entry_img
    )
    duration_entry = Entry(
        RentalWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    duration_entry.place(
        x=602.0,
        y=397.0,
        width=132.0,
        height=27.0
    )

    propertyId_entry_img = PhotoImage(
        file=relative_to_assets_Rental("entry_7.png"))
    RentalCanvas.create_image(
        304.0,
        300.5,
        image=propertyId_entry_img
    )
    propertyId_entry = Entry(
        RentalWindow,
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
        file=relative_to_assets_Rental("entry_8.png"))
    RentalCanvas.create_image(
        342.0,
        355.0,
        image=listingDate_entry_img
    )
    listingDate_entry = Entry(
        RentalWindow,
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
        file=relative_to_assets_Rental("button_1.png"))
    BackBtn = Button(
        RentalWindow,
        image=BackBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(RentalWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=480.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_Rental("button_2.png"))
    SubmitBtn = Button(
        RentalWindow,
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
    RentalWindow.resizable(False, False)
    RentalWindow.mainloop()