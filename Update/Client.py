from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib
from Update import Update
import Update.Update
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_CLIENT = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame1")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()

def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_Client(path: str) -> Path:
    return ASSETS_PATH_CLIENT / Path(path)
def Client_window():
    UpdateWindow = Update.Update.UpdateScreen()
    ClientWindow = Toplevel()
    ClientWindow.geometry("800x600")
    ClientWindow.configure(bg = "#FFFFFF")
    ClientCanvas = Canvas(
        ClientWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    ClientCanvas.pack()
    ClientCanvas.place(x = 0, y = 0)
    ClientLogo = PhotoImage(
        file=relative_to_assets_Client("image_1.png"))
    ClientCanvas.create_image(
        120.0,
        80.0,
        image=ClientLogo
    )
    ClientCanvas.create_text(
        285.0,
        51.0,
        anchor="nw",
        text=" Client Data",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    ClientCanvas.create_text(
        92.0,
        243.0,
        anchor="nw",
        text="Name:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    ClientCanvas.create_text(
        79.0,
        318.0,
        anchor="nw",
        text="Contact:",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    name_entry_image = PhotoImage(
        file=relative_to_assets_Client("entry_1.png"))
    ClientCanvas.create_image(
        422.5,
        266.0,
        image=name_entry_image
    )
    name_entry = Entry(
        ClientWindow,
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
        file=relative_to_assets_Client("entry_2.png"))
    ClientCanvas.create_image(
        422.5,
        341.0,
        image=contact_entry_image
    )
    contact_entry = Entry(
        ClientWindow,
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
        file=relative_to_assets_Client("button_1.png"))
    BackBtn = Button(
        ClientWindow,
        image=BackBtn_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showLandingWindow(ClientWindow),
        relief="flat"
    )
    BackBtn.place(
        x=65.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    Submitbtn_img = PhotoImage(
        file=relative_to_assets_Client("button_2.png"))
    Submitbtn = Button(
        ClientWindow,
        image=Submitbtn_img,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: print("hello"),
        relief="flat"
    )
    Submitbtn.place(
        
        x=627.0,
        y=472.0,
        width=107.0,
        height=51.0
    )

    
    ClientCanvas.create_text(
        109.0,
        189.0,
        anchor="nw",
        text="Client_Id",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    clientID_entry_img = PhotoImage(
        file=relative_to_assets_Client("entry_3.png"))
    ClientCanvas.create_image(
        294.0,
        205.0,
        image=clientID_entry_img
    )
    clientId_entry = Entry(
        ClientWindow,
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
    # Client End
    

    ClientWindow.mainloop()