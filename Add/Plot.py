from pathlib import Path
from tkinter import Tk,Toplevel, Canvas, Entry, Text, Button, PhotoImage
import importlib
import Functionality.add_property
import Functionality.add_plot


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame9")

def PropertyWindowModule():
    PropertyModule = importlib.import_module("Add.Property")
    PropertyModule.Property_window()
def showPropertyWindow(parent_window):
    parent_window.withdraw()
    PropertyWindowModule()
def relative_to_assets_Plot(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Plot_window():
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
        command=lambda: add(),
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
   
    def add():
        prop_id = propertyid_entry.get()
        area_size = areaSize_entry.get()
        title = title_entry.get()
        loc = location_entry.get()
        soc_id = societyID_entry.get()
        plot_id = plotId_entry.get()
        lease_iss = leaseissue_entry.get()
        lease_exp = leaseexpiry_entry.get()
        Functionality.add_plot.create("plot",Plot_ID = plot_id, Lease_issue = lease_iss, Lease_expiry = lease_exp)
        Functionality.add_property.add_property(area_size=area_size,location=loc,property_id=prop_id,property_type="plot",society_id=soc_id,specific_id=plot_id,title=title)
    PlotWindow.resizable(False, False)
    PlotWindow.mainloop()
