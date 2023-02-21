from tkinter import *
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("light")  
root = customtkinter.CTk()
root.geometry("500x530")
root.title("My first GUI")

customtkinter.CTkButton: {
    
}

empanada_normal = customtkinter.CTkImage(Image.open("empN.jpg"), size=(100, 100))
empanada_arreglada = customtkinter.CTkImage(Image.open("empA.jpeg"), size=(100, 100))
empanada_pobre = customtkinter.CTkImage(Image.open("pobre.jpeg"), size=(100, 100))

frame = customtkinter.CTkFrame(master=root, corner_radius= 20, fg_color="#bd1f26")
frame.pack(pady=20, padx=20, fill="both", expand=True)

titulo = customtkinter.CTkLabel(master=frame, corner_radius=2, text="Welcome to the shopping menu!",
                                font=("Roboto Black 900", 24, "bold"),
                                text_color=("#ecd778"))
titulo.pack(pady=15, padx=15)



def change_frame():
    frame2 = customtkinter.CTkFrame(master=root, corner_radius= 20, fg_color="#bd1f26")
    frame2.pack(pady=20, padx=20, fill="both", expand=1)
    frame.forget()

    title2 = customtkinter.CTkLabel(master=frame2, corner_radius=2, text="Let's choose what do you want!",
                                font=("Roboto Black 900", 24, "bold"),
                                text_color=("#ecd778"))
    title2.pack(pady=15, padx=15)

    cb1 = customtkinter.CTkCheckBox(master=frame2, text="Small",
                                    font=("Roboto Black900",12,"bold"),
                                    corner_radius=6,
                                    border_width=3,
                                    border_color="#260028",
                                    fg_color="#260028",
                                    hover_color="#eed77a",
                                    checkmark_color="#eed77a",
                                    text_color="#e8ca78",
                                    text_color_disabled=("gray60", "gray45"),
    )
    cb1.pack(ipadx= 300, ipady=500)

    


buttom_1 = customtkinter.CTkButton(master=frame,
                                   image=empanada_normal,
                                   fg_color=("#ecd778"),
                                   text="Freddy's Empanadita",
                                   text_color="#870937",
                                   corner_radius=8,
                                   width=200,
                                   height=110,
                                   font=("Roboto Black 900",30, "bold"),
                                   border_spacing=10,
                                   command=change_frame)
buttom_1.pack(padx = 10)

buttom_2 = customtkinter.CTkButton(master=frame,
                                   image=empanada_arreglada,
                                   fg_color=("#ecd778"),
                                   text="        The Arreglada    ",
                                   text_color="#870937",
                                   corner_radius=8,
                                   width=200,
                                   height=110,
                                   font=("Roboto Black 900",30, "bold"),
                                   border_spacing=10,
                                   command=change_frame)
buttom_2.pack(pady = 10)

buttom_3 = customtkinter.CTkButton(master=frame,
                                   image=empanada_pobre,
                                   fg_color=("#ecd778"),
                                   text="     Empanada Pobre  ",
                                   text_color="#870937",
                                   corner_radius=8,
                                   width=200,
                                   height=110,
                                   font=("Roboto Black 900",30, "bold"),
                                   border_spacing=10, 
                                   command=change_frame)
buttom_3.pack(pady = 2)
    


root.mainloop()