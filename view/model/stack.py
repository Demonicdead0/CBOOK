class stack:
    def __init__(self):
        self.pila = []
    
    def add(self, elemento):
        self.pila.append(elemento)
    
    def get(self):
        if len(self.pila) > 0:
            return self.pila[-1]
        else:
            return 0101
    
    def pop(self):
        if len(self.pila) > 0:
            return self.pila.pop()
        else:
            return 0101
    
