import gestion
import zooAnimales

class Animal():
    _totalAnimales=0
    _zona= None
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre=nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self,edad):
        self._edad=edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self,habitat):
        self._habitat=habitat
    
    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero=genero
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def setTotalAnimales(cls,totalAnimales):
        cls._totalAnimales=totalAnimales
    
    @classmethod
    def getZona(cls):
        return cls._zona
    @classmethod
    def setZona(cls,zona):
        cls._zona=zona

        
    