class Circulo:
    pi = 3.1415
    
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        return self.pi * (self.raio ** 2)

circ1 = Circulo(5)
print(circ1.area())