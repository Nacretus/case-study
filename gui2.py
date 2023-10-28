#from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import proto
import sys

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("dark-blue")

class secondGUI(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title("illness detection system")
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
        #reset button
        self.sidebar_Rst_button = ctk.CTkButton(self.logo_frame, text="Go Back", command=lambda: self.sidebar_button_event("Go Back"), font=ctk.CTkFont('Arial', size=12))
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

        #illness and symptoms
        self.symptom_label = ctk.CTkLabel(self.frame, text="Illness and Symptoms", font=ctk.CTkFont('Arial', size=15))
        self.symptom_label.configure(justify="left", anchor="w")
        self.symptom_label.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        #illness and symptoms
        self.symptom_textbox =ctk.CTkTextbox(self.frame, wrap="word")
        self.symptom_textbox.grid(row=1, column=1, padx=10, pady=(0, 10),sticky="nsew")
        self.frame.grid_rowconfigure(1, weight=1)

        #medication 
        self.medication_label = ctk.CTkLabel(self.frame, text="Medication", font=ctk.CTkFont('Arial', size=15))
        self.medication_label.configure(justify="left", anchor="w")
        self.medication_label.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        
        #medication
        self.medication_textbox =ctk.CTkTextbox(self.frame, wrap="word")
        self.medication_textbox.grid(row=3, column=1, padx=10, pady=(0, 10),sticky="nsew")
        self.frame.grid_rowconfigure(3, weight=1)



    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self,button_clicked):
        if button_clicked == "Go Back":
            confirm = messagebox.askyesno("Go Back Confirmation", "Do you wish to Go Back?\n Once you Go Back the information in here will change")
            if confirm:
                first_gui =proto.prototype()
                self.destroy()
                first_gui.mainloop()
            else:
                print("exit operation canceled")
        elif button_clicked == "exit":
            confirm = messagebox.askyesno("Exit Confirmation", "Do you wish to quit?")
            if confirm:
                self.quit()
                sys.exit()
            else:
                print("exit operation canceled")

    def display_symptom_text(self, text):
        self.symptom_textbox.configure(state="normal")
        self.symptom_textbox.delete("1.0", "end")
        self.symptom_textbox.insert("1.0", text)
            # Make the textbox read-only again
        self.symptom_textbox.configure(state="disabled")
    
if __name__ == "__main__":
    secondGUI = secondGUI()
    secondGUI.mainloop()
