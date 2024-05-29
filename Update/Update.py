from pathlib import Path
from tkinter import Tk, Toplevel, Canvas, Entry, Button, PhotoImage
import importlib

class UpdateScreen:
    def __init__(self,):
        self.id = None
        self.window = Toplevel()
        self.setup_window()

    def LandingWindowModule(self):
        LandingModule = importlib.import_module("LandingWindow")
        LandingModule.landing_window()

    def showLandingWindow(self):
        self.window.withdraw()
        self.LandingWindowModule()

    def relative_to_assets_update(self, path: str) -> Path:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\HP\Documents\Projects\Database\Code\assets\frame14")
        return ASSETS_PATH / Path(path)

    def setup_window(self):
        self.window.geometry("800x600")
        self.window.configure(bg="#FFFFFF")

        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        self.Logo = PhotoImage(file=self.relative_to_assets_update("image_1.png"))
        canvas.create_image(400.0, 155.0, image=self.Logo)

        canvas.create_text(
            344.0,
            342.0,
            anchor="nw",
            text="Enter ID",
            fill="#000000",
            font=("Lexend Regular", 26 * -1)
        )

        id_entry_img = PhotoImage(file=self.relative_to_assets_update("entry_1.png"))
        canvas.create_image(407.0, 421.5, image=id_entry_img)        
        self.id_entry = Entry(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.id_entry.place(x=381.0, y=407.0, width=52.0, height=27.0)

        BackBtn_ = PhotoImage(file=self.relative_to_assets_update("button_1.png"))
        BackBtn = Button(
            self.window,
            image=BackBtn_,
            borderwidth=0,
            highlightthickness=0,
            command=self.showLandingWindow,
            relief="flat"
        )
        BackBtn.place(x=73.0, y=499.0, width=107.0, height=51.0)

        SubmitBtn_ = PhotoImage(file=self.relative_to_assets_update("button_2.png"))
        SubmitBtn = Button(
            self.window,
            image=SubmitBtn_,
            borderwidth=0,
            highlightthickness=0,
            command= self.updateAction,
            relief="flat"
        )
        SubmitBtn.place(x=633.0, y=494.0, width=107.0, height=51.0)

        self.window.mainloop()
    
    def updateAction(self):
        self.id = self.id_entry.get()
        print (self.id)
        self.window.destroy()
        
    def get_id_entry_value(self):
        return self.id


