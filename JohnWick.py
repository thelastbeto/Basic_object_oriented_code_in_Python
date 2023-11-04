from typing import Any
from filmes import Filmes;

class JohnWick(Filmes):
    
    # Construição de classe filha com novo atributo;
    def __init__(self, nome, categoria, preco, disponibilidade, johnwick):
        super().__init__(nome, categoria, preco, disponibilidade)
        self.johnwick = johnwick;
        
    # Iremos mostrar, com um novo método, se pertence a franquia de JohnWick
    def pertenceAFranquiaJohnWick(self):
        if(self.johnwick == 'S'):
            print("Este filme pertence a franquia de JohnWick")
        else:
            print("Este filme não pertence a franquia de John Wick")
            
filme1 = JohnWick('John Wick: Parabellum', 'Ação', 100, 'S', 'S')
filme1.pertenceAFranquiaJohnWick()
        
        
        
    
    
        