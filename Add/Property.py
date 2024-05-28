import importlib
from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame6")
def HouseWindowModule():
    HouseModule = importlib.import_module("Add.House")
    HouseModule.House_window()
def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def BuildingWindowModule():
    BuildingModule = importlib.import_module("Add.Building")
    BuildingModule.Building_window()
def PlotWindowModule():
    PlotModule = importlib.import_module("Add.Plot")
    PlotModule.Plot_window()
def ShopWindowModule():
    ShopModule = importlib.import_module("Add.Shop")
    ShopModule.Shop_window()
def ApartmentWindowModule():
    ApartmentModule = importlib.import_module("Add.Apartment")
    ApartmentModule.Apartment_window()


def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()
def showHouseWindow(parent_window):
    parent_window.withdraw()
    HouseWindowModule()
def showBuildingWindow(parent_window):
    parent_window.withdraw()
    BuildingWindowModule()
def showPlotWindow(parent_window):
    parent_window.withdraw()
    PlotWindowModule()
def showShopWindow(parent_window):
    parent_window.withdraw()
    ShopWindowModule()
def showApartmentWindow(parent_window):
    parent_window.withdraw()
    ApartmentWindowModule()

def relative_to_assets_Property(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Property_window():
    PropertyWindow = Toplevel()
    PropertyWindow.geometry("800x600")
    PropertyWindow.configure(bg = "#FFFFFF")


    PropertyCanvas = Canvas(
        PropertyWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    PropertyCanvas.place(x = 0, y = 0)
    PropertyLogo = PhotoImage(
        file=relative_to_assets_Property("image_1.png"))
    PropertyCanvas.create_image(
        400.0,
        155.0,
        image=PropertyLogo
    )

    Apartment = PhotoImage(
        file=relative_to_assets_Property("button_1.png"))
    Apartment_ = Button(
        PropertyWindow,
        image=Apartment,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showApartmentWindow(PropertyWindow),
        relief="flat"
    )
    Apartment_.place(
        x=485.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    Building = PhotoImage(
        file=relative_to_assets_Property("button_2.png"))
    Building_ = Button(
        PropertyWindow,
        image=Building,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showBuildingWindow(PropertyWindow),
        relief="flat"
    )
    Building_.place(
        x=372.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    House = PhotoImage(
        file=relative_to_assets_Property("button_3.png"))
    House_ = Button(
        PropertyWindow,
        image=House,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showHouseWindow(PropertyWindow),
        relief="flat"
    )
    House_.place(
        x=146.0,
        y=415.0,
        width=75.0,
        height=25.0
    )

    Plot = PhotoImage(
        file=relative_to_assets_Property("button_4.png"))
    Plot_ = Button(
        PropertyWindow,
        image=Plot,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showPlotWindow(PropertyWindow),
        relief="flat"
    )
    Plot_.place(
        x=259.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    Shop = PhotoImage(
        file=relative_to_assets_Property("button_5.png"))
    Shop_ = Button(
        PropertyWindow,
        image=Shop,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showShopWindow(PropertyWindow),
        relief="flat"
    )
    Shop_.place(
        x=598.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    PropertyCanvas.create_text(
        326.0,
        344.0,
        anchor="nw",
        text=" Property",
        fill="#000000",
        font=("Lexend Regular", 26 * -1)
    )

    backBtn = PhotoImage(
        file=relative_to_assets_Property("button_6.png"))
    backBtn_ = Button(
        PropertyWindow,
        image=backBtn,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(PropertyWindow),
        relief="flat"
    )
    backBtn_.place(
        x=77.0,
        y=509.0,
        width=107.0,
        height=51.0
    )

    PropertyWindow.resizable(False, False)
    PropertyWindow.mainloop()
