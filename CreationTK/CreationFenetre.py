#By Grace NN
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo 
class FrameWidget(object):
    def __init__(self,fenetre=tk.Tk,tailX=int(50),tailY=int(50),couleur=str("#282839")):
        """Création des frames pour lr base et support de la fenetre
        Args:
            fenetre (_type_, optional): _la fentre par defaut_. Defaults to tk.Tk.
            couleur (_type_, optional): _en #ccc exampke_. Defaults to str("#282839").
            tailX (_type_, optional): _ la taille en integer_. Defaults to int().
            tailY (_type_, optional): _la hauteur en integer_. Defaults to int().
        """
        super()
        self.couleur,self.tailX,self.tailY,self.fenetre =couleur,tailX,tailY,fenetre #Memorisation de paramètres    
        self.frame =tk.Frame(self.fenetre,bg=couleur,width=self.tailX,height=self.tailY)
        
    def position(self,x=int(),y=int(), position=str("None")):
        """ Fixe la position de chaque frame

        Args:
            position (String, optional): la position en pack left, top, button. Defaults to str().
            x (integer, optional): la position en place. Defaults to int(0).
            y (integer, optional): la position en place. Defaults to int(0).
        """
        if(position != "None"):
            self.frame.pack(side=position)
        else :
            self.frame.place(x=x,y=y)
    
    def frame_config(self) :
        """Elle permet juste de renvoyer l'objet important pour configurer
        """
        return self.frame

class Label(FrameWidget):
    # Varible de classe
    def __init__(self,frame,text=str(),variable_name=str("var"),style=str("Lucida Bright"),police=int(10),couleur_text=str("#fff"),bg=str("#282839")):
        """Creation of text of widget

        Args:
            frame (_type_): _description_
            text (_type_, optional): _description_. Defaults to str().
            variable_name (_type_, optional): _description_. Defaults to str("var").
            style (_type_, optional): _description_. Defaults to str("Lucida Bright").
            police (_type_, optional): _description_. Defaults to int(10).
            couleur_text (_type_, optional): _description_. Defaults to str("#fff").
            bg (_type_, optional): _description_. Defaults to str("#282839").
        """
        super()

        
        #Memorisation des parametres
        self.frame=frame
        self.text=text
        self.bg =bg
        self.police=police
        self.couleur_text=couleur_text
        ## Compteur de la variable de 
        variable_name =variable_name.casefold()
        variable_name =variable_name.lstrip()
        variable_name =variable_name.strip()
        self.variable_name =variable_name
        
        #création du bouton
        self.label=tk.Label(self.frame,text=self.text,font=(style, self.police), fg=self.couleur_text,bg=self.bg)
        
    def position(self, x=int(0), y=int(0),position=str("None")):
        """ Fixe la position de chaque frame

        Args:
            position (String, optional): la position en pack left, top, button. Defaults to str().
            x (integer, optional): la position en place. Defaults to int(0).
            y (integer, optional): la position en place. Defaults to int(0).
        """
        if(position != "None"):
            self.label.pack(side=position)
        else :
            self.label.place(x=x,y=y)
    
    def getVariable_name(self)->str :
        """Renvoi le nom de la varible de l'objet"""
        return self.variable_name    
    
    def TextConfig(self):
        return self.text

class Bouton (FrameWidget) :
    
    def CommandEssai() : #this fonction make first action wen you add button in your 
        showinfo("Programme d'essaie","La commende d'essai marche correctement de puis que vous avez installez le paquet Création des fenetres  \n  By Grace NN and Gaelle BMX")
        

    def __init__(self, frame,command=CommandEssai,text=str("Button"),couleur_text=str("#fff"),style=str("Lucida Bright"),police=int(10),couleur=str("#282838"), tailX=int(7), tailY=int(2),src_image=str("")):
        """Le boutton de commande de la chose

        Args:
            frame (_type_): _description_
            command (str, optional):Il prend en argument les fonction "rien".
            src_image (_type_, optional):Chemin d'acces au image str("").
            text (_type_, optional): ce qui s'affiche sur le button str("Button").
            couleur_text (_type_, optional): _description_. Defaults to str("#fff").
            style (_type_, optional): _description_. Defaults to str("Lucida Bright").
            police (_type_, optional): _description_. Defaults to int(15).
            couleur (_type_, optional): _description_. Defaults to str("#5656ec").
            tailX (_type_, optional): _description_. Defaults to int(50).
            tailY (_type_, optional): _description_. Defaults to int(25).
        """
    
        self.frame, self.command,self.src,self.text,self.couleur_text,self.style,self.police,self.couleur =frame,command,src_image,text,couleur_text,style,police,couleur
        super()
        self.image=None
        #Verification des images entrant
        if (src_image !=""):
            self.image =tk.PhotoImage(file=src_image)
            
        
        self.bouton =tk.Button(self.frame,text=self.text,width=tailX,
                               height=tailY,
                               fg=couleur_text,
                               bg=couleur,
                               image=self.image,
                               font=(self.style,self.police),
                               border=(0),
                               command=self.command,
                               highlightbackground=self.couleur_text,
                               highlightcolor=self.couleur_text,
                               padx=1,
                               pady=0.5,
                               activebackground="dark green",
                               activeforeground="#ccc",
                               relief='raised',
                               
                            )

            
    
    def position(self, x=int(0), y=int(0), position=str("None")):
        """ Fixe la position de chaque frame

        Args:
            position (String, optional): la position en pack left, top, button. Defaults to str().
            x (integer, optional): la position en place. Defaults to int(0).
            y (integer, optional): la position en place. Defaults to int(0).
        """
        if(position != "None"):
            self.bouton.pack(side=position)
        else :
            self.bouton.place(x=x,y=y)
        
   
        
    def TextConfig(self):
        return self.bouton

class CanvasFrame(FrameWidget):
    def __init__(self, frame, tailX=int(50), tailY=int(50), couleur=str("#282839")):
        self.frame=frame
        
class Image(FrameWidget) :
    def __init__(self,fenetre,src=str(""),tail_x=int(7),tail_y=(5)):
        super()
class ChampTexte(FrameWidget) :
    pass
class MessageDialogueBox(FrameWidget) :
    def __init__(self,title="message info",message="GNN corporation vous salut",type=int(0)):
        self.type=type
        self.title=title
        self.message = message
        pass
    
    def message_info(self):
        match self.type:
            case 0: #message simple comme vous pouver le voir    
                messagebox.showinfo(self.title,self.message)
                pass
            case 1: #message warning
                messagebox.showwarning(self.title,self.message)
                pass
            case 2:
                messagebox.showerror(self.title,self.message)
                pass
            case 3: # question 
                messagebox.askquestion(self.title,self.message)
        
        if self.type =="warnirg":
            pass
        elif self.type =="info":
            pass
        elif self.type =="error":
            pass
            