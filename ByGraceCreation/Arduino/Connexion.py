import serial
import serial.tools.list_ports as lits_port
class ConnexionArduino :
    def __init__(self) -> None:
        self.rawdata =[] #Liste des valeurs que doit re tourner la fonction
        self.port =[] #La variable du port que nous allons utiliser 
        self.port_final=str()
        self.list_ports =lits_port.comports() # Extension de l'objet 
        self.a =0
        
        self.etat_connexion =False #Recuperer l'etat de l aconnexion
        self.arduino =serial
    
    def Connexion(self):
        """_summary_ Verification de la connexion et recherche du port à utiliser
        """
        ### Remplissage de tous les ports disponibles
        for i in (self.list_ports):
            self.port.append(i.device)
            
        
        for i in range (len(self.port)) : # Cone
            try :
                etat =self.arduino.Serial(self.port[i],timeout=1)
                self.port_final =self.port[i]
                self.etat_connexion =True
                break
            except :
                etat =None
                print("ERR001 : Erreur au niveau de la connexion pour le port : verifier les branchements de l'appareil")
        return etat
    
    def setPort(self)->str:
        """Renvois le port final retenu

        Returns:
            _type_: _description_
        """
        
        return self.port_final
    
    def setEtatConnection(self)->bool :
        """Retourne un boolen pour montrer l'etat d'une connexion 
        """
        return self.etat_connexion
