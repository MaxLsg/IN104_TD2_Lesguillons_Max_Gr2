#Create Classes#
#TD2#




class Animal:
    def __init__(self,age,weight,country):
        self.age=age
        self.weight=weight
        self.country=country
    def getweight(self):
        return self.weight
    def eat(self,kgm)
        self.weight+=kgm
        print("New weight after eating is : %f "%(self.weight))
class Bird(Animal):
    def __init__(self,span_wings,reynolds):
        self.span_wings=span_wings
        self.reynolds=reynolds
    def flight_velocity(self,c):
        velocity=span_wings*c
        return velocity
        
    def turbulent_flight(self):
        if self.reynolds > 2000:
            print("Turbulent flight")
    
class Fish(Animal):
    def _init_(self,ocean,depth):
        self.ocean=ocean
        self.depth=depth
    def pressure(self,volumic_mass):
        return (9.81*volumic_mass*self.depth + 100000)
    def migration_to(self,new_ocean):
        self.ocean=new_ocean
        return None
    
        
        
        
                
   
                
      
    
    
    

        