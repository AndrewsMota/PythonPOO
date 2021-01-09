import Pessoa as p
import os.path

class ParticipanteExterno(p.Pessoa):
    def __init__(self):
        super().__init__()
        self.empresa = ""

    def incluir(self):
        super().incluir()
        self.empresa = input("Entre com a empresa: ")

    def exibir(self):
        super().exibir()
        print(self.empresa)

    def salvar(self):
        try:
            arquivo_part = open('Participantes.txt', 'a')
            arquivo_part.write('\nParticipante externo\n')
            arquivo_part.close()
            super().salvar()
            arquivo_part = open('Participantes.txt', 'a')
            arquivo_part.write(self.empresa + '\n')
            arquivo_part.close()

        except Exception as erro:
            print(f"Erro: {erro.__class__}")
