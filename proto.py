#from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from symptom_data import sorted_unique_symptoms
from gui2 import secondGUI
import sys

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("dark-blue")

class prototype(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("sajd")
        self.geometry('1100x600')

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        #sideframe 
        self.sidebar_frame = ctk.CTkFrame(self, width= 281, height=720, corner_radius= 0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="AUTOMATED ILLNESS\n DETECTION SYSTEM", font=ctk.CTkFont('Arial', size=15))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 0))

        #box that is used in the buttons inside the sideframe bar
        self.logo_frame = ctk.CTkFrame(self.sidebar_frame, width=200, height=400, corner_radius=10)
        self.logo_frame.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nsew")

        #buttons inside the side frames
        #showresult button
        self.sidebar_ShRst_button = ctk.CTkButton(self.logo_frame, text="Show Result", command=lambda: self.sidebar_button_event("show result"), font=ctk.CTkFont('Arial', size=12))
        self.sidebar_ShRst_button.grid(row=2, column=0, padx=20, pady=20)
        self.sidebar_ShRst_button.configure(text_color_disabled="black")

        #reset button
        self.sidebar_Rst_button = ctk.CTkButton(self.logo_frame, text="Reset", command=lambda: self.sidebar_button_event("Reset"), font=ctk.CTkFont('Arial', size=12))
        self.sidebar_Rst_button.grid(row=3, column=0, padx=20, pady=20)
        
        #exit button
        self.sidebar_Exit_button = ctk.CTkButton(self.logo_frame, text="Exit", command=lambda: self.sidebar_button_event("exit"), font=ctk.CTkFont('Arial', size=12))
        self.sidebar_Exit_button.grid(row=4, column=0, padx=20, pady=20)

        #ui scaling
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set("100%")

        #apperance mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["System","Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        #main Frame 
        self.frame = ctk.CTkFrame(self, width= 900, height= 480, corner_radius= 10)
        self.frame.grid(row=0, column=1, padx= 10, pady= 10, rowspan=4, sticky="nsew")
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        #the label inside the main frame label kasi walang text sa ctk
        self.symptom_label = ctk.CTkLabel(self.frame, text="SYMPTOMS", font=ctk.CTkFont('Arial', size=15))
        self.symptom_label.configure(justify="left", anchor="w")
        self.symptom_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        #textbox inside the main frame need ng functionality
        self.symptom_textbox =ctk.CTkTextbox(self.frame, wrap="word")
        self.symptom_textbox.grid(row=1, column=1, padx=10, pady=(0, 10),sticky="nsew")
        self.symptom_textbox.insert("1.0", "Enter your symptoms here")
        self.symptom_textbox.bind("<Button-1>", self.clear_placeholder)
        self.symptom_textbox.bind("<Key>", self.check_textbox_content)
        self.check_textbox_content(None)

        #tabview yung may palit palit eto yung frame lang 
        self.tabview = ctk.CTkTabview(self, width=250, corner_radius=10)
        self.tabview.grid(row=2, column=1, padx=(10, 10), pady=(200,0), sticky="nsew", )
        self.tabview.add("Instruction")
        self.tabview.add("Symptoms")
        self.tabview.add("About")
        self.tabview.tab("Instruction").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Symptoms").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About").grid_columnconfigure(0, weight=1)

        #eto yung frame sa instruction tab as well as contents
        self.instruction = ctk.CTkLabel(self.tabview.tab("Instruction"), text="How to use this system\n\nFIRST: Click the left button of your mouse to the symptoms text box\n\nSECOND: Type the symptoms you are experiencing or refer to the SYMPTOMS TAB for more options\n\nTHIRD: Click the SHOW RESULT button to see the predicted illness as well as their medications\n\nRESET: This button will remove all text inside the textbox.\n\nEXIT: This button i close the program ", font=ctk.CTkFont('Arial', size=20))
        self.instruction.configure(justify="left", anchor="w")
        self.instruction.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.instruction.bind("<Configure>", self.adjust_font_size_Intro)

        #scrollable frame lang to 
        self.list_symptoms = ctk.CTkScrollableFrame(self.tabview.tab("Symptoms"), height=120)
        self.list_symptoms.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.list_symptoms.grid_columnconfigure(0, weight=1)
        self.list_symptoms.grid_columnconfigure(1, weight=1)
        self.list_symptoms.grid_columnconfigure(2, weight=1)

        # Create buttons for displaying and selecting symptoms
        self.columns = 3  # Initial number of columns
        self.button_width = 20  # Initial button width

        # Create buttons for displaying and selecting symptoms
        for i, symptom in enumerate(sorted_unique_symptoms):
            self.create_symptom_button(symptom, i)

        #contents nung about tabview
        self.about = ctk.CTkLabel(self.tabview.tab("About"), text="The Illness Detection System primary goal is to help people that experience\n\n mild symptoms, to know what kind of illness they have or their symptoms \n\nmight be an underlying dieases, or people that just want\n\n to know what kind of illness might associate with their symptoms, \n\nand whether they need to seek to a medical professional to help them", font=ctk.CTkFont('Arial', size=20))
        self.about.configure(justify="left", anchor="w")
        self.about.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.about.bind("<Configure>", self.adjust_font_size_About)
 
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def sidebar_button_event(self,button_clicked):
        if button_clicked == "show result":
            input_text = self.symptom_textbox.get("1.0", "end-1c")
            self.destroy()
            second_gui = secondGUI()
            second_gui.display_symptom_text(input_text)
            second_gui.mainloop()
        elif button_clicked == "Reset":
            clear_text = self.symptom_textbox.delete("1.0", "end")
            print("text cleared")
            self.symptom_textbox.insert("1.0", "Enter your symptoms here")
            self.check_textbox_content(None)
        elif button_clicked == "exit":
            confirm = messagebox.askyesno("Exit Confirmation", "Do you wish to quit?")
            if confirm:
                self.quit()
                sys.exit()
            else:
                print("exit operation canceled")

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        self.button_width = int(20 * new_scaling_float)  # Adjust the base button width accordingly

    def clear_placeholder(self, event):
        if self.symptom_textbox.get("1.0", "1.0 lineend") == "Enter your symptoms here":
            self.symptom_textbox.delete("1.0", "1.0 lineend")

    def check_textbox_content(self, event):
        input_text = self.symptom_textbox.get("1.0", "end-1c")
        if input_text.strip() == "" or input_text == "Enter your symptoms here":
            self.sidebar_ShRst_button.configure(state=ctk.DISABLED)
        else:
            self.sidebar_ShRst_button.configure(state=ctk.NORMAL)

    def adjust_font_size_About(self, event):
        label_width = self.about.winfo_width()
        new_font_size = int(label_width / 65)
        self.about.configure(font=ctk.CTkFont('Arial', size=new_font_size))

    def adjust_font_size_Intro(self, event):
        label_width = self.instruction.winfo_width()
        new_font_size =int(label_width / 64)
        self.instruction.configure(font=ctk.CTkFont('Arial', size=new_font_size))
    
    def add_symptom_to_textbox(self, symptom):
        current_text = self.symptom_textbox.get("1.0", "end-1c")
        if current_text.strip() != "":
            current_text += ", "
        updated_text = current_text + symptom
        self.symptom_textbox.delete("1.0", "end")
        self.symptom_textbox.insert("1.0", updated_text)
    
    def calculate_button_width(self):
        scaling_factor = self.winfo_width()
        base_button_width = 20  # Adjust this to your base button width
        return int(base_button_width * scaling_factor)
    
    def create_symptom_button(self, symptom, i):
        column = i % self.columns
        row = i // self.columns
        if column == 5:  # Adjust the number of columns if it's a new row
            self.columns = min(self.columns, i + 1)
        
        def button_click_event():
            if self.symptom_textbox.get("1.0", "1.0 lineend") == "Enter your symptoms here":
                self.symptom_textbox.delete("1.0", "1.0 lineend")

            current_text = self.symptom_textbox.get("1.0", "end-1c")
            if current_text.strip() == "":
                updated_text = symptom
            else:
                updated_text = current_text + ", " + symptom

            self.symptom_textbox.delete("1.0", "end")
            self.symptom_textbox.insert("1.0", updated_text)

            self.check_textbox_content(None)

        button = ctk.CTkButton(self.list_symptoms, text=symptom, command=button_click_event, font=ctk.CTkFont('Arial', size=12))
        button.configure(width=self.button_width)
        button.grid(row=i // self.columns, column=column, padx=2, pady=2, sticky="w")

if __name__ == "__main__":
    first_gui = prototype()
    first_gui.mainloop()