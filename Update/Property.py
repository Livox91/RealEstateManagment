from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib
import Update.Update
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_HOUSE = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame7")
ASSETS_PATH_PLOT = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame9")
ASSETS_PATH_APARTMENT = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame11")
ASSETS_PATH_SHOP = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame10")

def PropertyWindowModule():
    PropertyModule = importlib.import_module("Add.Property")
    PropertyModule.Property_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()


def relative_to_assets_Shop(path: str) -> Path:
    return ASSETS_PATH_SHOP / Path(path)
def relative_to_assets_Apartment(path: str) -> Path:
    return ASSETS_PATH_APARTMENT / Path(path)
def relative_to_assets_House(path: str) -> Path:
    return ASSETS_PATH_HOUSE / Path(path)
def relative_to_assets_Plot(path: str) -> Path:
    return ASSETS_PATH_PLOT / Path(path)
def House_window():
    UpdateWindow = Update.Update.UpdateScreen()
    if House_id:
        HouseWindow = Toplevel()
        HouseWindow.geometry("800x600")
        HouseWindow.configure(bg = "#FFFFFF")


        HouseCanvas = Canvas(
            HouseWindow,
            bg = "#FFFFFF",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        HouseCanvas.place(x = 0, y = 0)
        HouseLogo = PhotoImage(
            file=relative_to_assets_House("image_1.png"))
        HouseCanvas.create_image(
            120.0,
            80.0,
            image=HouseLogo
        )

        HouseCanvas.create_text(
            295.0,
            51.0,
            anchor="nw",
            text=" House DATA",
            fill="#052561",
            font=("NirmalaUI Bold", 58 * -1)
        )

        HouseCanvas.create_text(
            144.0,
            229.0,
            anchor="nw",
            text="Title",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        HouseCanvas.create_text(
            422.0,
            189.0,
            anchor="nw",
            text="Area Size(sq.ft)",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        title_entry_img = PhotoImage(
            file=relative_to_assets_House("entry_1.png"))
        HouseCanvas.create_image(
            421.5,
            252.0,
            image=title_entry_img
        )
        title_entry = Entry(
            HouseWindow,
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

        HouseCanvas.create_text(
            126.0,
            279.0,
            anchor="nw",
            text="Location",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        location_entry_img = PhotoImage(
            file=relative_to_assets_House("entry_2.png"))
        HouseCanvas.create_image(
            421.5,
            302.0,
            image=location_entry_img
        )
        location_entry = Entry(
            HouseWindow,
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
            file=relative_to_assets_House("entry_3.png"))
        HouseCanvas.create_image(
            627.0,
            205.0,
            image=areaSize_entry_img
        )
        areaSize_entry = Entry(
            HouseWindow,
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

        HouseCanvas.create_text(
            109.0,
            336.0,
            anchor="nw",
            text="Society_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        societyId_entry_img = PhotoImage(
            file=relative_to_assets_House("entry_4.png"))
        HouseCanvas.create_image(
            294.0,
            352.0,
            image=societyId_entry_img
        )
        societyId_entry = Entry(
            HouseWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        societyId_entry.place(
            x=260.0,
            y=336.0,
            width=68.0,
            height=30.0
        )

        HouseCanvas.create_text(
            109.0,
            385.0,
            anchor="nw",
            text="House_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        houseId_entry_img = PhotoImage(
            file=relative_to_assets_House("entry_5.png"))
        HouseCanvas.create_image(
            294.0,
            408.0,
            image=houseId_entry_img
        )
        houseId_entry = Entry(
            HouseWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        houseId_entry.place(
            x=260.0,
            y=392.0,
            width=68.0,
            height=30.0
        )

        HouseCanvas.create_text(
            451.0,
            328.0,
            anchor="nw",
            text="No. of Beds",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        Beds_entry_img = PhotoImage(
            file=relative_to_assets_House("entry_6.png"))
        HouseCanvas.create_image(
            628.5,
            351.0,
            image=Beds_entry_img
        )
        Beds_entry = Entry(
            HouseWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        Beds_entry.place(
            x=593.0,
            y=335.0,
            width=71.0,
            height=30.0
        )

        HouseCanvas.create_text(
            444.0,
            385.0,
            anchor="nw",
            text="No. of Baths",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        baths_entry_img = PhotoImage(
            file=relative_to_assets_House("entry_7.png"))
        HouseCanvas.create_image(
            630.0,
            402.0,
            image=baths_entry_img
        )
        baths_entry = Entry(
            HouseWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        baths_entry.place(
            x=596.0,
            y=386.0,
            width=68.0,
            height=30.0
        )

        HouseCanvas.create_text(
            95.0,
            189.0,
            anchor="nw",
            text="Property_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        propertyid_entry_img = PhotoImage(
            file=relative_to_assets_House("entry_8.png"))
        HouseCanvas.create_image(
            294.0,
            205.0,
            image=propertyid_entry_img
        )
        propertyid_entry = Entry(
            HouseWindow,
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

        Backbtn_ = PhotoImage(
            file=relative_to_assets_House("button_1.png"))
        Backbtn = Button(
            HouseWindow,
            image=Backbtn_,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: showPropertyWindow(HouseWindow),
            relief="flat"
        )
        Backbtn.place(
            x=67.0,
            y=514.0,
            width=107.0,
            height=51.0
        )

        SubmitBtn_ = PhotoImage(
            file=relative_to_assets_House("button_2.png"))
        SubmitBtn = Button(
            HouseWindow,
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
        HouseWindow.resizable(False, False)
        HouseWindow.mainloop()
    if Plot_Id:
        PlotWindow = Toplevel()

        PlotWindow.geometry("800x600")
        PlotWindow.configure(bg = "#FFFFFF")


        PlotCanvas = Canvas(
            PlotWindow,
            bg = "#FFFFFF",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        PlotCanvas.place(x = 0, y = 0)
        PlotLogo = PhotoImage(
            file=relative_to_assets_Plot("image_1.png"))
        PlotCanvas.create_image(
            120.0,
            80.0,
            image=PlotLogo
        )

        PlotCanvas.create_text(
            324.0,
            51.0,
            anchor="nw",
            text=" Plot DATA",
            fill="#052561",
            font=("NirmalaUI Bold", 58 * -1)
        )
        PlotCanvas.create_text(
            144.0,
            229.0,
            anchor="nw",
            text="Title",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )
        PlotCanvas.create_text(
            422.0,
            189.0,
            anchor="nw",
            text="Area Size(sq.ft)",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        title_entry_img = PhotoImage(
            file=relative_to_assets_Plot("entry_1.png"))
        PlotCanvas.create_image(
            421.5,
            252.0,
            image=title_entry_img
        )
        title_entry = Entry(
            PlotWindow,
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

        PlotCanvas.create_text(
            126.0,
            279.0,
            anchor="nw",
            text="Location",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        location_entry_img = PhotoImage(
            file=relative_to_assets_Plot("entry_2.png"))
        PlotCanvas.create_image(
            421.5,
            302.0,
            image=location_entry_img
        )
        location_entry = Entry(
            PlotWindow,
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
            file=relative_to_assets_Plot("entry_3.png"))
        PlotCanvas.create_image(
            627.0,
            205.0,
            image=areaSize_entry_img
        )
        areaSize_entry = Entry(
            PlotWindow,
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

        PlotCanvas.create_text(
            109.0,
            336.0,
            anchor="nw",
            text="Society_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        societyID_entry_img = PhotoImage(
            file=relative_to_assets_Plot("entry_4.png"))
        PlotCanvas.create_image(
            294.0,
            352.0,
            image=societyID_entry_img
        )
        societyID_entry = Entry(
            PlotWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        societyID_entry.place(
            x=260.0,
            y=336.0,
            width=68.0,
            height=30.0
        )

        PlotCanvas.create_text(
            453.0,
            335.0,
            anchor="nw",
            text="Plot_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        plotId_entry_img = PhotoImage(
            file=relative_to_assets_Plot("entry_5.png"))
        PlotCanvas.create_image(
            625.0,
            351.0,
            image=plotId_entry_img
        )
        plotId_entry = Entry(
            PlotWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        plotId_entry.place(
            x=591.0,
            y=335.0,
            width=68.0,
            height=30.0
        )

        PlotCanvas.create_text(
            95.0,
            189.0,
            anchor="nw",
            text="Property_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        propertyid_entry_img = PhotoImage(
            file=relative_to_assets_Plot("entry_6.png"))
        PlotCanvas.create_image(
            294.0,
            205.0,
            image=propertyid_entry_img
        )
        propertyid_entry = Entry(
            PlotWindow,
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
            file=relative_to_assets_Plot("button_1.png"))
        BackBtn = Button(
            PlotWindow,
            image=BackBtn_,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: showPropertyWindow(PlotWindow),
            relief="flat"
        )
        BackBtn.place(
            x=67.0,
            y=514.0,
            width=107.0,
            height=51.0
        )

        SubmitBtn_ = PhotoImage(
            file=relative_to_assets_Plot("button_2.png"))
        SubmitBtn = Button(
            PlotWindow,
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

        PlotCanvas.create_text(
            93.0,
            396.0,
            anchor="nw",
            text="Lease Issue Date",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        leaseissue_entry_img = PhotoImage(
            file=relative_to_assets_Plot("entry_7.png"))
        PlotCanvas.create_image(
            294.0,
            412.0,
            image=leaseissue_entry_img
        )
        leaseissue_entry = Entry(
            PlotWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        leaseissue_entry.place(
            x=260.0,
            y=396.0,
            width=68.0,
            height=30.0
        )

        PlotCanvas.create_text(
            421.0,
            396.0,
            anchor="nw",
            text="Lease Expiry Date",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        leaseexpiry_entry_img = PhotoImage(
            file=relative_to_assets_Plot("entry_8.png"))
        PlotCanvas.create_image(
            627.0,
            412.0,
            image=leaseexpiry_entry_img
        )
        leaseexpiry_entry = Entry(
            PlotWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        leaseexpiry_entry.place(
            x=593.0,
            y=396.0,
            width=68.0,
            height=30.0
        )
        PlotWindow.resizable(False, False)
        PlotWindow.mainloop()
    if Apartment_ID:
        ApartmentWindow = Toplevel()
        ApartmentWindow.geometry("800x600")
        ApartmentWindow.configure(bg = "#FFFFFF")

        ApartmentCanvas = Canvas(
            ApartmentWindow,
            bg = "#FFFFFF",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        ApartmentCanvas.place(x = 0, y = 0)
        ApartmentLogo = PhotoImage(
            file=relative_to_assets_Apartment("image_1.png"))
        ApartmentCanvas.create_image(
            120.0,
            80.0,
            image=ApartmentLogo
        )

        ApartmentCanvas.create_text(
            240.0,
            51.0,
            anchor="nw",
            text=" Apartment DATA",
            fill="#052561",
            font=("NirmalaUI Bold", 56 * -1)
        )

        ApartmentCanvas.create_text(
            144.0,
            229.0,
            anchor="nw",
            text="Title",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        ApartmentCanvas.create_text(
            422.0,
            189.0,
            anchor="nw",
            text="Area Size(sq.ft)",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        title_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_1.png"))
        ApartmentCanvas.create_image(
            421.5,
            252.0,
            image=title_entry_img
        )
        title_entry = Entry(
            ApartmentWindow,
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

        ApartmentCanvas.create_text(
            126.0,
            279.0,
            anchor="nw",
            text="Location",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        location_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_2.png"))
        ApartmentCanvas.create_image(
            421.5,
            302.0,
            image=location_entry_img
        )
        location_entry = Entry(
            ApartmentWindow,
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
            file=relative_to_assets_Apartment("entry_3.png"))
        ApartmentCanvas.create_image(
            627.0,
            205.0,
            image=areaSize_entry_img
        )
        areaSize_entry = Entry(
            ApartmentWindow,
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

        ApartmentCanvas.create_text(
            109.0,
            336.0,
            anchor="nw",
            text="Society_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        societyID_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_4.png"))
        ApartmentCanvas.create_image(
            294.0,
            352.0,
            image=societyID_entry_img
        )
        societyID_entry = Entry(
            ApartmentWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        societyID_entry.place(
            x=260.0,
            y=336.0,
            width=68.0,
            height=30.0
        )

        ApartmentCanvas.create_text(
            425.0,
            335.0,
            anchor="nw",
            text="Apartment ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        apartmentid_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_5.png"))
        ApartmentCanvas.create_image(
            625.0,
            351.0,
            image=apartmentid_entry_img
        )
        apartmentid_entry = Entry(
            ApartmentWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        apartmentid_entry.place(
            x=591.0,
            y=335.0,
            width=68.0,
            height=30.0
        )

        ApartmentCanvas.create_text(
            104.0,
            392.0,
            anchor="nw",
            text="Building_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        buildingID_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_6.png"))
        ApartmentCanvas.create_image(
            294.0,
            408.0,
            image=buildingID_entry_img
        )
        buildingID_entry = Entry(
            ApartmentWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        buildingID_entry.place(
            x=260.0,
            y=392.0,
            width=68.0,
            height=30.0
        )

        ApartmentCanvas.create_text(
            452.0,
            391.0,
            anchor="nw",
            text="Unit_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        unitId_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_7.png"))
        ApartmentCanvas.create_image(
            625.0,
            407.0,
            image=unitId_entry_img
        )
        unitId_entry = Entry(
            ApartmentWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        unitId_entry.place(
            x=591.0,
            y=391.0,
            width=68.0,
            height=30.0
        )

        ApartmentCanvas.create_text(
            95.0,
            189.0,
            anchor="nw",
            text="Property_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        propertyid_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_8.png"))
        ApartmentCanvas.create_image(
            294.0,
            205.0,
            image=propertyid_entry_img
        )
        propertyid_entry = Entry(
            ApartmentWindow,
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
            file=relative_to_assets_Apartment("button_1.png"))
        BackBtn = Button(
            ApartmentWindow,
            image=BackBtn_,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: showPropertyWindow(ApartmentWindow),
            relief="flat"
        )
        BackBtn.place(
            x=67.0,
            y=514.0,
            width=107.0,
            height=51.0
        )

        SubmitBtn_ = PhotoImage(
            file=relative_to_assets_Apartment("button_2.png"))
        SubmitBtn = Button(
            ApartmentWindow,
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

        ApartmentCanvas.create_text(
            109.0,
            443.0,
            anchor="nw",
            text="Floor Level",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        floorlvl_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_9.png"))
        ApartmentCanvas.create_image(
            268.0,
            456.0,
            image=floorlvl_entry_img
        )
        floorlvl_entry = Entry(
            ApartmentWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        floorlvl_entry.place(
            x=234.0,
            y=440.0,
            width=68.0,
            height=30.0
        )

        ApartmentCanvas.create_text(
            332.0,
            443.0,
            anchor="nw",
            text="No.of Beds",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        NoBeds_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_10.png"))
        ApartmentCanvas.create_image(
            469.0,
            455.0,
            image=NoBeds_entry_img
        )
        NoBeds_entry = Entry(
            ApartmentWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        NoBeds_entry.place(
            x=435.0,
            y=439.0,
            width=68.0,
            height=30.0
        )

        ApartmentCanvas.create_text(
            528.0,
            443.0,
            anchor="nw",
            text="No.of Baths",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        NoBath_entry_img = PhotoImage(
            file=relative_to_assets_Apartment("entry_11.png"))
        ApartmentCanvas.create_image(
            672.0,
            456.0,
            image=NoBath_entry_img
        )
        NoBath_entry = Entry(
            ApartmentWindow,
            bd=0,
            bg="#F8F5F5",
            fg="#000716",
            highlightthickness=0
        )
        NoBath_entry.place(
            x=638.0,
            y=440.0,
            width=68.0,
            height=30.0
        )

        ApartmentWindow.resizable(False, False)
        ApartmentWindow.mainloop()
    if Shop_ID:
        ShopWindow = Toplevel()

        ShopWindow.geometry("800x600")
        ShopWindow.configure(bg = "#FFFFFF")


        ShopCanvas = Canvas(
            ShopWindow,
            bg = "#FFFFFF",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        ShopCanvas.place(x = 0, y = 0)
        ShopLogo = PhotoImage(
            file=relative_to_assets_Shop("image_1.png"))
        ShopCanvas.create_image(
            120.0,
            80.0,
            image=ShopLogo
        )

        ShopCanvas.create_text(
            310.0,
            51.0,
            anchor="nw",
            text=" Shop DATA",
            fill="#052561",
            font=("NirmalaUI Bold", 58 * -1)
        )

        ShopCanvas.create_text(
            144.0,
            229.0,
            anchor="nw",
            text="Title",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        ShopCanvas.create_text(
            422.0,
            189.0,
            anchor="nw",
            text="Area Size(sq.ft)",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        title_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_1.png"))
        ShopCanvas.create_image(
            421.5,
            252.0,
            image=title_entry_img
        )
        title_entry = Entry(
            ShopWindow,
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

        ShopCanvas.create_text(
            126.0,
            279.0,
            anchor="nw",
            text="Location",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        location_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_2.png"))
        ShopCanvas.create_image(
            421.5,
            302.0,
            image=location_entry_img
        )
        location_entry = Entry(
            ShopWindow,
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
            file=relative_to_assets_Shop("entry_3.png"))
        ShopCanvas.create_image(
            627.0,
            205.0,
            image=areaSize_entry_img
        )
        areaSize_entry = Entry(
            ShopWindow,
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

        ShopCanvas.create_text(
            109.0,
            336.0,
            anchor="nw",
            text="Society_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        societyid_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_4.png"))
        ShopCanvas.create_image(
            294.0,
            352.0,
            image=societyid_entry_img
        )
        societyid_entry = Entry(
            ShopWindow,
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

        ShopCanvas.create_text(
            448.0,
            335.0,
            anchor="nw",
            text="Shop_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        shopid_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_5.png"))
        ShopCanvas.create_image(
            625.0,
            351.0,
            image=shopid_entry_img
        )
        shopid_entry = Entry(
            ShopWindow,
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

        ShopCanvas.create_text(
            104.0,
            434.0,
            anchor="nw",
            text="Building_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        buildingid_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_6.png"))
        ShopCanvas.create_image(
            294.0,
            450.0,
            image=buildingid_entry_img
        )
        buildingid_entry = Entry(
            ShopWindow,
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

        ShopCanvas.create_text(
            452.0,
            433.0,
            anchor="nw",
            text="Unit_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        unitid_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_7.png"))
        ShopCanvas.create_image(
            625.0,
            449.0,
            image=unitid_entry_img
        )
        unitid_entry = Entry(
            ShopWindow,
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

        ShopCanvas.create_text(
            95.0,
            189.0,
            anchor="nw",
            text="Property_ID",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        propertyid_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_8.png"))
        ShopCanvas.create_image(
            294.0,
            205.0,
            image=propertyid_entry_img
        )
        propertyid_entry = Entry(
            ShopWindow,
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
            file=relative_to_assets_Shop("button_1.png"))
        BackBtn = Button(
            ShopWindow,
            image=BackBtn_,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: showPropertyWindow(ShopWindow),
            relief="flat"
        )
        BackBtn.place(
            x=67.0,
            y=514.0,
            width=107.0,
            height=51.0
        )

        SubmitBtn_ = PhotoImage(
            file=relative_to_assets_Shop("button_2.png"))
        SubmitBtn = Button(
            ShopWindow,
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

        ShopCanvas.create_text(
            93.0,
            388.0,
            anchor="nw",
            text="Lease Issue Date",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        leaseIssue_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_9.png"))
        ShopCanvas.create_image(
            294.0,
            401.0,
            image=leaseIssue_entry_img
        )
        leaseIssue_entry = Entry(
            ShopWindow,
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

        ShopCanvas.create_text(
            419.0,
            389.0,
            anchor="nw",
            text="Lease Expiry Date",
            fill="#000000",
            font=("NirmalaUI Bold", 20 * -1)
        )

        leaseExpiry_entry_img = PhotoImage(
            file=relative_to_assets_Shop("entry_10.png"))
        ShopCanvas.create_image(
            625.0,
            401.0,
            image=leaseExpiry_entry_img
        )
        leaseExpiry_entry = Entry(
            ShopWindow,
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
        ShopWindow.resizable(False, False)
        ShopWindow.mainloop()
    
