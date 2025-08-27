from herança_ex_01 import Personagens

class Participa():
    def faz(self):
        return print(f"O {self.personagem} e de {self.participa}")

personagen = Personagens('Tsukishima', 'Haikyuu' ,'Não sei', 'Masculino')
personagen.faz()