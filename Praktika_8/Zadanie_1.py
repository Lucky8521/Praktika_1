class animals():
    def __init__(self, tip,  activ, nutrition):
        self.tip = tip
        self.activ = activ
        self.nutrition = nutrition
    def __str__(self):
        return f'What type of animal? {self.tip}, your animal is active and what it eats {self.activ}, eats {self.nutrition}'

class mamals(animals):
    def __init__(self, tip, activ, nutrition, wool, name):
        super().__init__(tip, activ, nutrition)
        self.wool  = wool 
        self.name = name
    def say(self, txt):
        print(f'Wool y {self.name} {txt}')

class human(mamals):
    def __init__(self, tip,activ, nutrition, wool , name,  individual, personality):
        super().__init__(tip, activ, nutrition, wool , name)
        self.individual = individual
        self.personality = personality
    
    def __add__(self, Mamals):
        print(f'{self.name} and {Mamals.name}')

class cat(mamals):
    
    def __init__(self, tip, activ, nutrition, wool , name, cute, claws, home):
        super().__init__(tip,  activ, nutrition,wool , name)
        self.cute = cute
        self.claws = claws
        self.home =home

class dog(mamals):
    def __init__(self, tip,  activ, nutrition, wool , name, home, friend, affectionate):
        super().__init__(tip,  activ, nutrition, wool , name)
        self.home = home
        self.friend = friend
        self.affectionate = affectionate

    def __str__(self) -> str:
        return f'Is your dog a pet? {self.home}'

animal = animals('mamals', 'active', 'fish ')
print(animal)
print("----------------------------------")
an = mamals(None,None,None,None,"Wolf")
an.say("very curvy")
print("----------------------------------")
hum = human(None,None, None,None,"Bear", None,None)
hum_1 = human(None,None, None,None, "Polar bear", None ,None)
hum + hum_1
print("----------------------------------")
dog = dog(None,None,None,None,None, "Yes",None,None)
print(dog)