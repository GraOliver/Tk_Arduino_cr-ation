#By Grace NN dans cette partie nous allons proposer une certaine 
#menu deroulan
import CreationFenetre as crfnt
class SimpleDeroulanMenu(object):
    # constantes de la programmation
    HEIGTH_MIN_NAVE=30
    POSITION_Y_LABEL_NAVE =15
    def __init__(self,fenetre,dimension=str("900x300")) -> None:
        self.fentre =fenetre
        self.dimension =dimension.split('x')
        self.ruban =crfnt.FrameWidget(self.fentre,tailX=self.fentre.winfo_screenwidth(),tailY=50).position()
        
        self.focus = self.fentre.bind("<Motion>",SimpleDeroulanMenu.one_focus)
        # self.on_click=self.fentre.bind('<>')
    def menu(self,rubrique=['Hom','Setting','A bout']):
        k=0
        for i in rubrique :
            label =crfnt.Label(self.ruban,text=i).position(x=100+k,y=self.POSITION_Y_LABEL_NAVE)
            k+=100
    
    def submenu(self,event): 
        print(event)
        
    def one_click(event):
        print(event)
    def one_focus(event):
        if event.y>0 and event.y<30:
            if  event.x >100 and event.x <120 :
                print(event.x)
                