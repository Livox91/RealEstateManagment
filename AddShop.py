from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame10")

def relative_to_assets_addShop(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def PropertyWindowModule():
    PropertyModule = importlib.import_module("AddProperty")
    PropertyModule.addProperty_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()

def addShop_window():
    addShopWindow = Toplevel()

    addShopWindow.geometry("800x600")
    addShopWindow.configure(bg = "#FFFFFF")


    AddShopCanvas = Canvas(
        addShopWindow,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    AddShopCanvas.place(x = 0, y = 0)
    addShopLogo = PhotoImage(
        file=relative_to_assets_addShop("image_1.png"))
    AddShopCanvas.create_image(
        120.0,
        80.0,
        image=addShopLogo
    )

    AddShopCanvas.create_text(
        310.0,
        51.0,
        anchor="nw",
        text="ADD Shop DATA",
        fill="#052561",
        font=("NirmalaUI Bold", 58 * -1)
    )

    AddShopCanvas.create_text(
        144.0,
        229.0,
        anchor="nw",
        text="Title",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    AddShopCanvas.create_text(
        422.0,
        189.0,
        anchor="nw",
        text="Area Size(sq.ft)",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    title_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_1.png"))
    AddShopCanvas.create_image(
        421.5,
        252.0,
        image=title_entry_img
    )
    title_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    title_entry.place(
        x=260.0,
        y=236.0,
        width=323.0,
        height=30.0
    )

    AddShopCanvas.create_text(
        126.0,
        279.0,
        anchor="nw",
        text="Location",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    location_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_2.png"))
    AddShopCanvas.create_image(
        421.5,
        302.0,
        image=location_entry_img
    )
    location_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    location_entry.place(
        x=260.0,
        y=286.0,
        width=323.0,
        height=30.0
    )

    areaSize_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_3.png"))
    AddShopCanvas.create_image(
        627.0,
        205.0,
        image=areaSize_entry_img
    )
    areaSize_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    areaSize_entry.place(
        x=593.0,
        y=189.0,
        width=68.0,
        height=30.0
    )

    AddShopCanvas.create_text(
        109.0,
        336.0,
        anchor="nw",
        text="Society_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    societyid_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_4.png"))
    AddShopCanvas.create_image(
        294.0,
        352.0,
        image=societyid_entry_img
    )
    societyid_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    societyid_entry.place(
        x=260.0,
        y=336.0,
        width=68.0,
        height=30.0
    )

    AddShopCanvas.create_text(
        448.0,
        335.0,
        anchor="nw",
        text="Shop_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    shopid_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_5.png"))
    AddShopCanvas.create_image(
        625.0,
        351.0,
        image=shopid_entry_img
    )
    shopid_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    shopid_entry.place(
        x=591.0,
        y=335.0,
        width=68.0,
        height=30.0
    )

    AddShopCanvas.create_text(
        104.0,
        434.0,
        anchor="nw",
        text="Building_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    buildingid_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_6.png"))
    AddShopCanvas.create_image(
        294.0,
        450.0,
        image=buildingid_entry_img
    )
    buildingid_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    buildingid_entry.place(
        x=260.0,
        y=434.0,
        width=68.0,
        height=30.0
    )

    AddShopCanvas.create_text(
        452.0,
        433.0,
        anchor="nw",
        text="Unit_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    unitid_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_7.png"))
    AddShopCanvas.create_image(
        625.0,
        449.0,
        image=unitid_entry_img
    )
    unitid_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    unitid_entry.place(
        x=591.0,
        y=433.0,
        width=68.0,
        height=30.0
    )

    AddShopCanvas.create_text(
        95.0,
        189.0,
        anchor="nw",
        text="Property_ID",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    propertyid_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_8.png"))
    AddShopCanvas.create_image(
        294.0,
        205.0,
        image=propertyid_entry_img
    )
    propertyid_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    propertyid_entry.place(
        x=260.0,
        y=189.0,
        width=68.0,
        height=30.0
    )

    BackBtn_ = PhotoImage(
        file=relative_to_assets_addShop("button_1.png"))
    BackBtn = Button(
        addShopWindow,
        image=BackBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showPropertyWindow(addShopWindow),
        relief="flat"
    )
    BackBtn.place(
        x=67.0,
        y=514.0,
        width=107.0,
        height=51.0
    )

    SubmitBtn_ = PhotoImage(
        file=relative_to_assets_addShop("button_2.png"))
    SubmitBtn = Button(
        addShopWindow,
        image=SubmitBtn_,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("SubmitBtn clicked"),
        relief="flat"
    )
    SubmitBtn.place(
        x=627.0,
        y=509.0,
        width=107.0,
        height=51.0
    )

    AddShopCanvas.create_text(
        93.0,
        388.0,
        anchor="nw",
        text="Lease Issue Date",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    leaseIssue_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_9.png"))
    AddShopCanvas.create_image(
        294.0,
        401.0,
        image=leaseIssue_entry_img
    )
    leaseIssue_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    leaseIssue_entry.place(
        x=260.0,
        y=385.0,
        width=68.0,
        height=30.0
    )

    AddShopCanvas.create_text(
        419.0,
        389.0,
        anchor="nw",
        text="Lease Expiry Date",
        fill="#000000",
        font=("NirmalaUI Bold", 20 * -1)
    )

    leaseExpiry_entry_img = PhotoImage(
        file=relative_to_assets_addShop("entry_10.png"))
    AddShopCanvas.create_image(
        625.0,
        401.0,
        image=leaseExpiry_entry_img
    )
    leaseExpiry_entry = Entry(
        addShopWindow,
        bd=0,
        bg="#F8F5F5",
        fg="#000716",
        highlightthickness=0
    )
    leaseExpiry_entry.place(
        x=591.0,
        y=385.0,
        width=68.0,
        height=30.0
    )
    addShopWindow.resizable(False, False)
    addShopWindow.mainloop()
