import tkinter as tk
import CreationFenetre as crt 
import MenuDeroulant as mdr

menue=mdr
fram =crt
fenetre =tk.Tk()
fenetre.geometry("900x650")
print(fenetre.winfo_screenwidth())
deroul=menue.SimpleDeroulanMenu(fenetre)
deroul.menu()
fenetre.mainloop()
