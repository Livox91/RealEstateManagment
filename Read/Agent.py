from tkinter import *
from tkinter import ttk, messagebox
import Functionality.Read_agent
import importlib

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()


def Agent_window():
    window = Toplevel()
    frame = Frame(window)
    frame.pack()
    Agent_Frame = LabelFrame(frame, text="All Agents")
    Agent_Frame.pack(padx=20, pady=10)

    success, agents = Functionality.Read_agent.read_agents()
    if success:
            tree = ttk.Treeview(Agent_Frame, columns=("ID", "Name", "Contact", "Agency_ID", "Society_ID"))
            tree.heading("#0", text="", anchor="center") 
            tree.heading("ID", text="ID", anchor="center")
            tree.heading("Name", text="Name", anchor="center")
            tree.heading("Contact", text="Contact", anchor="center")
            tree.heading("Agency_ID", text="Agency_ID", anchor="center")
            tree.heading("Society_ID", text="Society_ID", anchor="center")
            
            for agent in agents:
                tree.insert("", "end", values=agent)
            
            tree.pack()

    backButton = Button(frame, text="Back", command=lambda:showLandingWindow(window))
    backButton.pack(padx=10, pady=10)