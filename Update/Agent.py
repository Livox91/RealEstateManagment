from tkinter import ttk, messagebox
from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib
import Functionality.UPDATE_client
import Functionality.readone
import Functionality.update_Agent
import Update.Update
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_AGENT = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame4")

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()

def relative_to_assets_Agent(path: str) -> Path:
    return ASSETS_PATH_AGENT / Path(path)
def Agent_window():
    UpdateWindow = Update.Update.UpdateScreen()
    id = UpdateWindow.get_id_entry_value()
    if id:
        success,data = Functionality.readone.read("agent",id)
        if(success):
            print(data)
            AgentWindow = Toplevel()
            AgentWindow.geometry("800x600")
            AgentWindow.configure(bg = "#FFFFFF")

            AgentCanvas = Canvas(
                AgentWindow,
                bg = "#FFFFFF",
                height = 600,
                width = 800,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            AgentCanvas.place(x = 0, y = 0)
            AgentLogo = PhotoImage(
                file=relative_to_assets_Agent("image_1.png"))
            AgentCanvas.create_image(
                120.0,
                80.0,
                image=AgentLogo
            )

            AgentCanvas.create_text(
                309.0,
                51.0,
                anchor="nw",
                text=" Agent Data",
                fill="#052561",
                font=("NirmalaUI Bold", 58 * -1)
            )


            AgentCanvas.create_text(
                77.0,
                357.0,
                anchor="nw",
                text="Agent Name:",
                fill="#000000",
                font=("NirmalaUI Bold", 20 * -1)
            )

            AgentCanvas.create_text(
                102.0,
                304.0,
                anchor="nw",
                text="Agency_Id",
                fill="#000000",
                font=("NirmalaUI Bold", 20 * -1)
            )

            AgentCanvas.create_text(
                106.0,
                250.0,
                anchor="nw",
                text="Agent_id:",
                fill="#000000",
                font=("NirmalaUI Bold", 20 * -1)
            )

            AgentIDEntry_img = PhotoImage(
                file=relative_to_assets_Agent("entry_1.png"))
            AgentCanvas.create_image(
                295.0,
                266.0,
                image=AgentIDEntry_img
            )
            AgentIDEntry = Entry(
                AgentWindow,
                bd=0,
                bg="#FFFFFF",
                fg="#000716",
                highlightthickness=0
            )
            AgentIDEntry.place(
                x=261.0,
                y=250.0,
                width=68.0,
                height=30.0
            )
            AgentIDEntry.insert(0,data[0])
            AgentIDEntry.config(state='disabled')

            AgentNameEntry_img = PhotoImage(
                file=relative_to_assets_Agent("entry_2.png"))
            AgentCanvas.create_image(
                295.0,
                320.0,
                image=AgentNameEntry_img
            )
            AgentNameEntry = Entry(
                AgentWindow,
                bd=0,
                bg="#FFFFFF",
                fg="#000716",
                highlightthickness=0
            )
            AgentNameEntry.place(
                x=261.0,
                y=304.0,
                width=68.0,
                height=30.0
            )
            AgentNameEntry.insert(0,data[1])

            AgentContactEntry_img = PhotoImage(
                file=relative_to_assets_Agent("entry_3.png"))
            AgentCanvas.create_image(
                626.0,
                266.0,
                image=AgentContactEntry_img
            )
            AgentContactEntry = Entry(
                AgentWindow,
                bd=0,
                bg="#FFFFFF",
                fg="#000716",
                highlightthickness=0
            )
            AgentContactEntry.place(
                x=592.0,
                y=250.0,
                width=68.0,
                height=30.0
            )
            AgentContactEntry.insert(0,data[2])

            AgentSocietyIdEntry_img = PhotoImage(
                file=relative_to_assets_Agent("entry_4.png"))
            AgentCanvas.create_image(
                419.5,
                373.0,
                image=AgentSocietyIdEntry_img
            )
            AgentSocietyIdEntry = Entry(
                AgentWindow,
                bd=0,
                bg="#F8F5F5",
                fg="#000716",
                highlightthickness=0
            )
            AgentSocietyIdEntry.place(
                x=258.0,
                y=357.0,
                width=323.0,
                height=30.0
            )
            AgentSocietyIdEntry.insert(0,data[4])
            AgentCanvas.create_text(
                119.0,
                415.0,
                anchor="nw",
                text="Contact:",
                fill="#000000",
                font=("NirmalaUI Bold", 20 * -1)
            )

            AgentCanvas.create_text(
                385.0,
                245.0,
                anchor="nw",
                text="Affliated Society_ID",
                fill="#000000",
                font=("NirmalaUI Bold", 20 * -1)
            )

            AgentAgencyIDEntry_img = PhotoImage(
                file=relative_to_assets_Agent("entry_5.png"))
            AgentCanvas.create_image(
                419.5,
                431.0,
                image=AgentAgencyIDEntry_img
            )
            AgentAgencyIDEntry = Entry(
                AgentWindow,
                bd=0,
                bg="#F8F5F5",
                fg="#000716",
                highlightthickness=0
            )
            AgentAgencyIDEntry.place(
                x=258.0,
                y=415.0,
                width=323.0,
                height=30.0
            )
            AgentAgencyIDEntry.insert(0,data[3])

            BackBtn_img = PhotoImage(
                file=relative_to_assets_Agent("button_1.png"))
            BackBtn = Button(
                AgentWindow,
                image=BackBtn_img,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: showLandingWindow(AgentWindow),
                relief="flat"
            )
            BackBtn.place(
                x=65.0,
                y=472.0,
                width=107.0,
                height=51.0
            )
            
            Submitbtn_img = PhotoImage(
                file=relative_to_assets_Agent("button_2.png"))
            Submitbtn = Button(
                AgentWindow,
                image=Submitbtn_img,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: update(),
                relief="flat"
            )
            Submitbtn.place(
                
                x=627.0,
                y=472.0,
                width=107.0,
                height=51.0
            )
            
            def update():
                agencyid = AgentAgencyIDEntry.get()
                contact = AgentContactEntry.get()
                name = AgentNameEntry.get()
                societyid = AgentSocietyIdEntry.get()
                
                Functionality.update_Agent.update_agent(agency_id=UpdateWindow.get_id_entry_value(),agent_name=name,contact=contact,society_id=societyid,agent_id=agencyid)
            
            AgentWindow.mainloop()
        else:
            messagebox.showerror("Error", "Agent not found.")
    else:
        messagebox.showerror("Error", "Agent ID is required.")