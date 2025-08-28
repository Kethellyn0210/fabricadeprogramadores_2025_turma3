class Pessoa():

    def __init__(self, altura: float, idade: int, sexo: str, endereco: int, telefone: int, nome_mae: str, nome_pai: str, cpf: int, nascimento: int, nome: str  ):

        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.nome_pai = nome_pai
        self.nome_mae = nome_mae
        self.telefone = telefone
        self.endereco = endereco
        self.sexo = sexo
        self.idade = idade
        self.altura = altura


        @property
        def idade(self):
            return self