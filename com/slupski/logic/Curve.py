class Curve:
    A = 0
    B = 0
    modulo = 13
    
    def __init__(self, A, B, modulo):
        self.A = A
        self.B = B
        self.modulo = modulo
    
    def __isCorrect__(self):
        delta = (4*(self.A^3)) + (27*(self.B^2)) 
        if delta % self.modulo == 0:
            return False
        return True