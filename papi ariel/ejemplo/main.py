import tkinter as tk
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Mrs. Freddy Shopping")

class Scrollbar:
    def __init__(self):
        root = customtkinter.CTk()
        h = Scrollbar(root, orient = "horizontal")
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(root)
        v.pack(side = RIGHT, fill = Y)

        def main():
            print("Hello World!")
            tkinter.messagebox.showerror(title="Fatal error ocurred!", message="No enough memory to show the error!")

        def main2():
            msj = textbox.get("1.0",'end-1c')
            tkinter.messagebox.showinfo(title="Data Information", message=msj)

        label = customtkinter.CTkLabel(root, text="Mrs. Freddy's Shop", font=("Roboto", 18))
        label.pack(padx=60, pady=40, fill="both")

       
       
       
       
       
       
       
       
        """

        buttom = customtkinter.CTkButton(root, text="Send", font=("Arial", 16), command=main2, fg_color="orange")
        buttom.pack(padx=20, pady=40)

        buttom2 = customtkinter.CTkButton(root, text="Send'nt", font=("Arial", 16), command=main)
        buttom2.pack(padx=0, pady=0 )
        """
    
        root.mainloop()

s = Scrollbar()