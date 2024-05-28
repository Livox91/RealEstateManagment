import importlib
from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_LANDING = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame0")


def AddSocietyModule():
    SocietyModule = importlib.import_module("Add.Society")
    SocietyModule.Society_window()
def AddClientModule():
    ClientModule = importlib.import_module("Add.Client")
    ClientModule.Client_window()
def AddAgentModule():
    AgentModule = importlib.import_module("Add.Agent")
    AgentModule.Agent_window()
def AddListingModule():
    ListingModule = importlib.import_module("Add.Listing")
    ListingModule.Listing_window()
def AddAgencyModule():
    AgencyModule = importlib.import_module("Add.Agency")
    AgencyModule.Agency_window()
def AddPropertyModule():
    PropertyModule = importlib.import_module("Add.Property")
    PropertyModule.Property_window()
def UpdateClientModule():
     ClientModule = importlib.import_module("Update.Client")
     ClientModule.Client_window()

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
def showaddPropertyWindow(parent_window):
    parent_window.destroy()
    AddPropertyModule()
def showUpdateClientWindow(parent_window):
    parent_window.destroy()
    UpdateClientModule()


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
    landingCanvas.create_text(
        32.0,
        323.0,
        anchor="nw",
        text="Read Data",
        fill="#000000",
        font=("Lexend Regular", 21 * -1)
    )
    landingCanvas.create_text(
        604.0,
        323.0,
        anchor="nw",
        text="Add Data",
        fill="#000000",
        font=("Lexend Regular", 21 * -1)
    )
    landingCanvas.create_text(
        283.0,
        323.0,
        anchor="nw",
        text="Update & Delete Data",
        fill="#000000",
        font=("Lexend Regular", 21 * -1)
    )
    
    add_property_btn = PhotoImage(
        file=relative_to_assets_landing("button_1.png"))
    add_property_btn_ = Button(
        LandingWindow,
        image=add_property_btn,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: showaddPropertyWindow(LandingWindow),
        relief="flat"
    )
    add_property_btn_.place(
        x=713.0,
        y=469.0,
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
        x=713.0,
        y=418.0,
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
        x=713.0,
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
        x=604.0,
        y=367.0,
        width=75.0,
        height=25.0
    )

    read_property_bySociety = PhotoImage(
        file=relative_to_assets_landing("button_5.png"))
    read_property_bySociety_ = Button(
        LandingWindow,
        image=read_property_bySociety,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showaddAgencyWindow(LandingWindow),
        relief="flat"
    )
    read_property_bySociety_.place(
        x=32.0,
        y=365.0,
        width=113.0,
        height=25.0
    )

    update_property = PhotoImage(
        file=relative_to_assets_landing("button_6.png"))
    update_property_ = Button(
        LandingWindow,
        image=update_property,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showaddListingWindow(LandingWindow),
        relief="flat"
    )
    update_property_.place(
        x=263.0,
        y=364.0,
        width=113.0,
        height=25.0
    )
   
    update_client = PhotoImage(
        file=relative_to_assets_landing("button_7.png"))
    update_client_ = Button(
        LandingWindow,
        image=update_client,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showUpdateClientWindow(LandingWindow),
        relief="flat"
    )
    update_client_.place(
        x=263.0,
        y=403.0,
        width=113.0,
        height=25.0
    )
    
    update_agent = PhotoImage(
        file=relative_to_assets_landing("button_8.png"))
    update_agent_ = Button(
        LandingWindow,
        image=update_agent,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    update_agent_.place(
        x=263.0,
        y=442.0,
        width=113.0,
        height=25.0
    )
   
    update_rental = PhotoImage(
        file=relative_to_assets_landing("button_9.png"))
    update_rental_ = Button(
        LandingWindow,
        image=update_rental,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("update_rental_ clicked"),
        relief="flat"
    )
    update_rental_.place(
        x=263.0,
        y=480.0,
        width=113.0,
        height=25.0
    )

    
    update_sale = PhotoImage(
        file=relative_to_assets_landing("button_10.png"))
    update_sale_ = Button(
        LandingWindow,
        image=update_sale,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("update_sale_ clicked"),
        relief="flat"
    )
    update_sale_.place(
        x=263.0,
        y=516.0,
        width=113.0,
        height=25.0
    )
    
    delete_property = PhotoImage(
        file=relative_to_assets_landing("button_11.png"))
    delete_property_ = Button(
        LandingWindow,
        image=delete_property,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("delete_property_ clicked"),
        relief="flat"
    )
    delete_property_.place(
        x=401.0,
        y=363.0,
        width=113.0,
        height=25.0
    )

    delete_client = PhotoImage(
        file=relative_to_assets_landing("button_12.png"))
    delete_client_ = Button(
        LandingWindow,
        image=delete_client,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("delete_client_ clicked"),
        relief="flat"
    )
    delete_client_.place(
        x=401.0,
        y=402.0,
        width=113.0,
        height=25.0
    )

    delete_agency = PhotoImage(
        file=relative_to_assets_landing("button_13.png"))
    delete_agency_ = Button(
        LandingWindow,
        image=delete_agency,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("delete_agency_ clicked"),
        relief="flat"
    )
    delete_agency_.place(
        x=401.0,
        y=515.0,
        width=113.0,
        height=25.0
    )

    delete_listing = PhotoImage(
        file=relative_to_assets_landing("button_14.png"))
    delete_listing_ = Button(
        LandingWindow,
        image=delete_listing,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("delete_listing_ clicked"),
        relief="flat"
    )
    delete_listing_.place(
        x=401.0,
        y=480.0,
        width=113.0,
        height=25.0
    )

    delete_agent = PhotoImage(
        file=relative_to_assets_landing("button_15.png"))
    delete_agent_ = Button(
        LandingWindow,
        image=delete_agent,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("delete_agent_ clicked"),
        relief="flat"
    )
    delete_agent_.place(
        x=401.0,
        y=441.0,
        width=113.0,
        height=25.0
    )

    read_property_byType = PhotoImage(
        file=relative_to_assets_landing("button_16.png"))
    read_property_byType_ = Button(
        LandingWindow,
        image=read_property_byType,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("read_property_byType_ clicked"),
        relief="flat"
    )
    read_property_byType_.place(
        x=32.0,
        y=404.0,
        width=113.0,
        height=25.0
    )

    read_clients = PhotoImage(
        file=relative_to_assets_landing("button_17.png"))
    read_clients_ = Button(
        LandingWindow,
        image=read_clients,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("read_clients_ clicked"),
        relief="flat"
    )
    read_clients_.place(
        x=32.0,
        y=518.0,
        width=113.0,
        height=25.0
    )

    read_agents = PhotoImage(
        file=relative_to_assets_landing("button_18.png"))
    read_agents_ = Button(
        LandingWindow,
        image=read_agents,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("read_agents_ clicked"),
        relief="flat"
    )
    read_agents_.place(
        x=32.0,
        y=480.0,
        width=113.0,
        height=25.0
    )

    read_property_byListing = PhotoImage(
        file=relative_to_assets_landing("button_19.png"))
    read_property_byListing_ = Button(
        LandingWindow,
        image=read_property_byListing,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("read_property_byListing_ clicked"),
        relief="flat"
    )
    read_property_byListing_.place(
        x=32.0,
        y=442.0,
        width=113.0,
        height=25.0
    )
    
    add_agency = PhotoImage(
        file=relative_to_assets_landing("button_20.png"))
    add_agency_ = Button(
        LandingWindow,
        image=add_agency,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showaddAgencyWindow(LandingWindow),
        relief="flat"
    )
    add_agency_.place(
        x=605.0,
        y=416.0,
        width=75.0,
        height=25.0
    )

    add_listing = PhotoImage(
        file=relative_to_assets_landing("button_21.png"))
    add_listing_ = Button(
        LandingWindow,
        image=add_listing,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:showaddListingWindow(LandingWindow),
        relief="flat"
    )
    add_listing_.place(
        x=604.0,
        y=469.0,
        width=75.0,
        height=25.0
    )

    LandingWindow.mainloop()
    #Landing Window END
