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
        120.0,
        80.0,
        image=addListingLogo
    )

    addListingCanvas.create_text(
        304.0,
        51.0,
        anchor="nw",
        text="ADD Listing Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    addListingCanvas.create_text(
        132.0,
        258.0,
        anchor="nw",
        text="Listing_Id",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addListingCanvas.create_text(
        114.0,
        330.0,
        anchor="nw",
        text="Property_Id ",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addListingCanvas.create_text(
        112.0,
        404.0,
        anchor="nw",
        text="Listing Date",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addListingID_img = PhotoImage(
        file=relative_to_assets_addListing("entry_1.png"))
    addListingCanvas.create_image(
        361.0,
        272.5,
        image=addListingID_img
    )
    addListingID_entry = Entry(
        addListingWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addListingID_entry.place(
        x=335.0,
        y=258.0,
        width=52.0,
        height=27.0
    )

    addListingPropertyID_img = PhotoImage(
        file=relative_to_assets_addListing("entry_2.png"))
    addListingCanvas.create_image(
        361.0,
        344.5,
        image=addListingPropertyID_img
    )
    addListingPropertyID_entry = Entry(
        addListingWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    addListingPropertyID_entry.place(
        x=335.0,
        y=330.0,
        width=52.0,
        height=27.0
    )

    ListingDateEntry_img = PhotoImage(
        file=relative_to_assets_addListing("entry_3.png"))
    addListingCanvas.create_image(
        400.5,
        419.0,
        image=ListingDateEntry_img
    )
    addListingDate_entry = Entry(
        addListingWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    addListingDate_entry.place(
        x=335.0,
        y=401.0,
        width=131.0,
        height=34.0
    )
    BackBtn_img = PhotoImage(
        file=relative_to_assets_addListing("button_1.png"))
    BackBtn = Button(
        addListingWindow,
        image=BackBtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(addListingWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    Submitbtn_img = PhotoImage(
        file=relative_to_assets_addListing("button_2.png"))
    Submitbtn = Button(
        addListingWindow,
        image=Submitbtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Submitbtn clicked"),
        relief="flat"
    )
    Submitbtn.place(
        
        x=627.0,
        y=472.0,
        width=107.0,
        height=51.0
    )
    addListingWindow.mainloop()

