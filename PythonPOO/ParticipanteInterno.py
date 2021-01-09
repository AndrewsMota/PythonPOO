import Pessoa as p

class ParticipanteInterno(p.Pessoa):
    def __init__(self):
        super().__init__()
        self.matricula = 0
        self.sexo = ""
        self.nascimento = ""
        self.telefone = ""
        self.setor = ""
        self.emissor = "não "
        self.cont = 0

    def incluir(self):
        super().incluir()
        self.matricula = int(input("Entre com a matrícula: "))
        self.sexo = input("Entre com o sexo: ")
        self.nascimento = input("Entre com a data de nascimento: ")
        self.telefone = input("Entre com o telefone: ")
        self.setor = input("Entre com o setor: ")


    def exibir(self):
        super().exibir()
        print(self.matricula)
        print(self.sexo)
        print(self.nascimento)
        print(self.telefone)
        print(self.setor)

    def salvar(self):
        try:
            arquivo_part = open('Participantes.txt', 'a')
            arquivo_part.write('\nParticipante interno\n')
            arquivo_part.write(self.emissor + 'é o emissor.\n')
            arquivo_part.close()
            super().salvar()
            arquivo_part = open('Participantes.txt', 'a')
            arquivo_part.write(str(self.matricula) + '\n')
            arquivo_part.write(self.sexo + '\n')
            arquivo_part.write(self.nascimento + '\n')
            arquivo_part.write(self.telefone + '\n')
            arquivo_part.write(self.setor + '\n')
            arquivo_part.close()

        except Exception as erro:
            print(f"O problema encontrado foi {erro.__class__}")

    def verificar_emissor(self):
        try:
            arquivo_part = open('Participantes.txt', 'r')
            for linha0 in arquivo_part:
                linha = linha0.strip()
                if linha == 'é o emissor.':
                    self.cont = 1
            arquivo_part.close()
        except FileNotFoundError:
            print('Arquivo não existe !')
