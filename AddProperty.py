import importlib
from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame6")
def AddHouseWindowModule():
    AddHouseModule = importlib.import_module("AddHouse")
    AddHouseModule.addHouse_window()
def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def AddBuildingWindowModule():
    AddBuildingModule = importlib.import_module("AddBuilding")
    AddBuildingModule.addBuilding_window()
def AddPlotWindowModule():
    AddPlotModule = importlib.import_module("AddPlot")
    AddPlotModule.addPlot_window()
def AddShopWindowModule():
    AddShopModule = importlib.import_module("AddShop")
    AddShopModule.addShop_window()
def AddApartmentWindowModule():
    AddApartmentModule = importlib.import_module("AddApartment")
    AddApartmentModule.addApartment_window()


def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()
def showAddHouseWindow(parent_window):
    parent_window.withdraw()
    AddHouseWindowModule()
def showAddBuildingWindow(parent_window):
    parent_window.withdraw()
    AddBuildingWindowModule()
def showAddPlotWindow(parent_window):
    parent_window.withdraw()
    AddPlotWindowModule()
def showAddShopWindow(parent_window):
    parent_window.withdraw()
    AddShopWindowModule()
def showAddApartmentWindow(parent_window):
    parent_window.withdraw()
    AddApartmentWindowModule()

def relative_to_assets_addProperty(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def addProperty_window():
    addPropertyWindow = Toplevel()
    addPropertyWindow.geometry("800x600")
    addPropertyWindow.configure(bg = "#FFFFFF")


    addPropertyCanvas = Canvas(
        addPropertyWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    addPropertyCanvas.place(x = 0, y = 0)
    addPropertyLogo = PhotoImage(
        file=relative_to_assets_addProperty("image_1.png"))
    addPropertyCanvas.create_image(
        400.0,
        155.0,
        image=addPropertyLogo
    )

    addApartment = PhotoImage(
        file=relative_to_assets_addProperty("button_1.png"))
    addApartment_ = Button(
        addPropertyWindow,
        image=addApartment,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showAddApartmentWindow(addPropertyWindow),
        relief="flat"
    )
    addApartment_.place(
        x=485.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    addBuilding = PhotoImage(
        file=relative_to_assets_addProperty("button_2.png"))
    addBuilding_ = Button(
        addPropertyWindow,
        image=addBuilding,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showAddBuildingWindow(addPropertyWindow),
        relief="flat"
    )
    addBuilding_.place(
        x=372.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    addHouse = PhotoImage(
        file=relative_to_assets_addProperty("button_3.png"))
    addHouse_ = Button(
        addPropertyWindow,
        image=addHouse,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showAddHouseWindow(addPropertyWindow),
        relief="flat"
    )
    addHouse_.place(
        x=146.0,
        y=415.0,
        width=75.0,
        height=25.0
    )

    addPlot = PhotoImage(
        file=relative_to_assets_addProperty("button_4.png"))
    addPlot_ = Button(
        addPropertyWindow,
        image=addPlot,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showAddPlotWindow(addPropertyWindow),
        relief="flat"
    )
    addPlot_.place(
        x=259.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    addShop = PhotoImage(
        file=relative_to_assets_addProperty("button_5.png"))
    addShop_ = Button(
        addPropertyWindow,
        image=addShop,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showAddShopWindow(addPropertyWindow),
        relief="flat"
    )
    addShop_.place(
        x=598.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    addPropertyCanvas.create_text(
        326.0,
        344.0,
        anchor="nw",
        text="Add Property",
        fill="#000000",
        font=("Lexend Regular", 26 * -1)
    )

    backBtn = PhotoImage(
        file=relative_to_assets_addProperty("button_6.png"))
    backBtn_ = Button(
        addPropertyWindow,
        image=backBtn,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(addPropertyWindow),
        relief="flat"
    )
    backBtn_.place(
        x=77.0,
        y=509.0,
        width=107.0,
        height=51.0
    )

    addPropertyWindow.resizable(False, False)
    addPropertyWindow.mainloop()
