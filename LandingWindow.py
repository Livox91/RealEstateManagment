import importlib
from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_LANDING = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame0")


def AddSocietyModule():
    SocietyModule = importlib.import_module("Society")
    SocietyModule.addSociety_window()
def AddClientModule():
    ClientModule = importlib.import_module("Client")
    ClientModule.addClient_window()
def AddAgentModule():
    AgentModule = importlib.import_module("Agent")
    AgentModule.addAgent_window()
def AddListingModule():
    ListingModule = importlib.import_module("Listing")
    ListingModule.addListing_window()
def AddAgencyModule():
    AgencyModule = importlib.import_module("Agency")
    AgencyModule.addAgency_window()

def showaddClientWindow(parent_window):
    parent_window.destroy()
    AddClientModule()
def showaddAgencyWindow(parent_window):
    parent_window.destroy()
    AddAgencyModule()
def showaddListingWindow(parent_window):
    parent_window.destroy()
    AddListingModule()
def showaddAgentWindow(parent_window):
    parent_window.destroy()
    AddAgentModule()
def showaddSocietyWindow(parent_window):
    parent_window.withdraw()
    AddSocietyModule()

def relative_to_assets_landing(path: str) -> Path:
    return ASSETS_PATH_LANDING / Path(path)
def landing_window():
    LandingWindow = Toplevel()
    LandingWindow.geometry("800x600")
    LandingWindow.configure(bg = "#FFFFFF")

    landingCanvas = Canvas(
        LandingWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    landingCanvas.pack()

    landingCanvas.place(x = 0, y = 0)
    real_estate_logo = PhotoImage(
        file=relative_to_assets_landing("image_1.png"))
    landingCanvas.create_image(
        400.0,
        155.0,
        image=real_estate_logo
    )
    landingCanvas.create_text(
        665.0,
        544.0,
        anchor="nw",
        text="231572 Zaki Haider\n231527 Minahil Ahmed\n231689 Ujaala Zaib",
        fill="#000000",
        font=("Lexend Regular", 12 * -1)
    )
    
    add_property_btn = PhotoImage(
        file=relative_to_assets_landing("button_1.png"))
    add_property_btn_ = Button(
        LandingWindow,
        image=add_property_btn,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: print("hello"),
        relief="flat"
    )
    add_property_btn_.place(
        x=583.0,
        y=481.0,
        width=75.0,
        height=25.0
    )

   
    add_client_btn = PhotoImage(
        file=relative_to_assets_landing("button_2.png"))
    add_client_btn_ = Button(
        LandingWindow,
        image=add_client_btn,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: showaddClientWindow(LandingWindow),
        relief="flat"
    )
    add_client_btn_.place(
        x=583.0,
        y=424.0,
        width=75.0,
        height=25.0
    )

   
    add_agent_btn = PhotoImage(
        file=relative_to_assets_landing("button_3.png"))
    add_agent_btn_ = Button(
        LandingWindow,
        image=add_agent_btn,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showaddAgentWindow(LandingWindow),
        relief="flat"
    )
    add_agent_btn_.place(
        x=583.0,
        y=367.0,
        width=75.0,
        height=25.0
    )
    
      
    add_society = PhotoImage(
    file=relative_to_assets_landing("button_4.png"))
    add_society_ = Button(
        LandingWindow,
        image=add_society,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showaddSocietyWindow(LandingWindow),
        relief="flat"
    )
    add_society_.place(
        x=459.0,
        y=367.0,
        width=75.0,
        height=25.0
    )

    add_agency = PhotoImage(
        file=relative_to_assets_landing("button_5.png"))
    add_agency_ = Button(
        LandingWindow,
        image=add_agency,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showaddListingWindow(LandingWindow),
        relief="flat"
    )
    add_agency_.place(
        x=459.0,
        y=424.0,
        width=75.0,
        height=25.0
    )

    add_listing = PhotoImage(
        file=relative_to_assets_landing("button_6.png"))
    add_listing_ = Button(
        LandingWindow,
        image=add_listing,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showaddListingWindow(LandingWindow),
        relief="flat"
    )
    add_listing_.place(
        x=459.0,
        y=481.0,
        width=75.0,
        height=25.0
    )
    
    LandingWindow.mainloop()
    #Landing Window END
