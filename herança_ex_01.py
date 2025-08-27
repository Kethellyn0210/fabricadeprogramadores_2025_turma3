class Personagens():
    def __init__(self,personagem, participa, idade, sexo):
     self.personagem = personagem
     self.participa = participa
     self.idade = idade
     self.sexo = sexo

    def participa_(self):
        return print(f"O personagem {self.personagem} participa de {self.participa}.")

    def apresentar(self):
        return print(f"Olá! Eu sou {self.personagem}, tenho {self.idade} anos e sou do sexo {self.sexo}.")

    def idade_(self):
        return print(f"{self.personagem} tem {self.idade} anos!")

    def descricao(self):
        return print(f"Personagem: {self.personagem}, Série/Anime: {self.participa}, Idade: {self.idade}, Sexo: {self.sexo}")