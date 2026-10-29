from database import Base
from sqlalchemy import String, Integer, Column 

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key="true")
    name = Column(String, nullable="false")
    hair = Column(String, nullable="false")
    clothes = Column(String, nullable="false")
        
    def changeName(self, name):
        self.name = name
        
    def changeHair(self, hair):
        self.hair = hair
        
    def changeClothes(self, clothes):
        self.clothes = clothes
    
    def resetCharacter(self):
        self.name = ""
        self.hair = ""
        self.clothes = ""
        
    def __str__(self):
        return f"Name: {self.name} - Hair: {self.hair} - Clothes: {self.clothes}"
    