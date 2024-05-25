from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib
import Connection


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_ADDCLIENT = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame1")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()

def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_AddClient(path: str) -> Path:
    return ASSETS_PATH_ADDCLIENT / Path(path)
def addClient_window():
    AddClientWindow = Toplevel()
    AddClientWindow.geometry("800x600")
    AddClientWindow.configure(bg = "#FFFFFF")
    addClientCanvas = Canvas(
        AddClientWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    addClientCanvas.pack()
    addClientCanvas.place(x = 0, y = 0)
    addClientLogo = PhotoImage(
        file=relative_to_assets_AddClient("image_1.png"))
    addClientCanvas.create_image(
        120.0,
        80.0,
        image=addClientLogo
    )
    addClientCanvas.create_text(
        285.0,
        51.0,
        anchor="nw",
        text="ADD Client Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    addClientCanvas.create_text(
        92.0,
        243.0,
        anchor="nw",
        text="Name:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    addClientCanvas.create_text(
        79.0,
        318.0,
        anchor="nw",
        text="Contact:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    name_entry_image = PhotoImage(
        file=relative_to_assets_AddClient("entry_1.png"))
    addClientCanvas.create_image(
        422.5,
        266.0,
        image=name_entry_image
    )
    name_entry = Entry(
        AddClientWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    name_entry.place(
        x=261.0,
        y=250.0,
        width=323.0,
        height=30.0
    )

    contact_entry_image = PhotoImage(
        file=relative_to_assets_AddClient("entry_2.png"))
    addClientCanvas.create_image(
        422.5,
        341.0,
        image=contact_entry_image
    )
    contact_entry = Entry(
        AddClientWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    contact_entry.place(
        x=261.0,
        y=325.0,
        width=323.0,
        height=30.0
    )

    BackBtn_img = PhotoImage(
        file=relative_to_assets_AddClient("button_1.png"))
    BackBtn = Button(
        AddClientWindow,
        image=BackBtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(AddClientWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    Submitbtn_img = PhotoImage(
        file=relative_to_assets_AddClient("button_2.png"))
    Submitbtn = Button(
        AddClientWindow,
        image=Submitbtn_img,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: getValue(),
        relief="flat"
    )
    Submitbtn.place(
        
        x=627.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    
    addClientCanvas.create_text(
        109.0,
        189.0,
        anchor="nw",
        text="Client_Id",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    clientID_entry_img = PhotoImage(
        file=relative_to_assets_AddClient("entry_3.png"))
    addClientCanvas.create_image(
        294.0,
        205.0,
        image=clientID_entry_img
    )
    clientId_entry = Entry(
        AddClientWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    clientId_entry.place(
        x=260.0,
        y=189.0,
        width=68.0,
        height=30.0
    )
    #Add Client End
    def getValue():
        name = name_entry.get()
        contact = contact_entry.get()
        client_id = clientId_entry.get()
        if name and contact and client_id :
            success,message =Connection.addRecordtoTable("client",Client_Id = client_id, Client_name = name , Contact = contact)
            if success:
                print("done")
            else:
                print(message)
        
    AddClientWindow.mainloop()