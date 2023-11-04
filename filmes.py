class Filmes:
    
    def __init__(self, nome, categoria, preco, disponibilidade):
        self.nome = nome;
        self.categoria = categoria;
        self.preco = preco;
        self.disponibilidade = disponibilidade;
    
    #Criação dos métodos da classe
    
    def filmesCaros(self):
        if (self.preco > 60):
            print("Este filme é muito caro");
        else: 
            print("O filme está em conta");
               
    
    def exibirFilmes(self):
        print(f"Nome: {self.nome}");
        print(f"Categoria: {self.categoria}");
        print(f"Nome: {self.preco}");
        
        
    def exibeDisponibilidadeDeFilmeParaAlugar(self):
        if (self.disponibilidade == 'S'):
            print("O filme está disponível");
        else:
            print("Desculpe. O filme não está disponível no momento. Deseja ver uma segunda opção?");
            
        
# Instâncias da classe Filmes:

ListaDeFilmes = [
Filmes('John Wick: De volta ao Jogo', 'Ação', 70, 'S'),
Filmes('John Wick: Um novo dia para matar', 'Ação', 90, 'S'),
Filmes('Piratas do Caribe: No fim do mundo', 'Aventura', 50, 'N')
];

for i in ListaDeFilmes:
    i.exibirFilmes()
    print("-=" * 30)



        
