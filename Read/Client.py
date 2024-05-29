from tkinter import *
from tkinter import ttk, messagebox
import Functionality.Read_client
import importlib

def LandingWindowModule():
    LandingModule = importlib.import_module("LandingWindow")
    LandingModule.landing_window()
def showLandingWindow(parent_window):
    parent_window.withdraw()
    LandingWindowModule()


def Client_window():
    window = Toplevel()
    frame = Frame(window)
    frame.pack()
    Client_Frame = LabelFrame(frame, text="All Clients")
    Client_Frame.pack(padx=20, pady=10)

    success, clients = Functionality.Read_client.read_clients()
    if success:
            tree = ttk.Treeview(Client_Frame, columns=("ID", "Name", "Contact"))
            tree.heading("#0", text="", anchor="center") 
            tree.heading("ID", text="ID", anchor="center")
            tree.heading("Name", text="Name", anchor="center")
            tree.heading("Contact", text="Contact", anchor="center")
            
            
            for client in clients:
                tree.insert("", "end", values=client)
            
            tree.pack()

    backButton = Button(frame, text="Back", command=lambda:showLandingWindow(window))
    backButton.pack(padx=10, pady=10)