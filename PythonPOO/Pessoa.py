class Pessoa():
    def __init__(self):
        self.nome = ""
        self.email = ""
        self.celular = ""

    def incluir(self):
        self.nome = input("Entre com o nome: ")
        self.email = input("Entre com o email: ")
        self.celular = input("Entre com o celular: ")

    def exibir(self):
        print(self.nome)
        print(self.email)
        print(self.celular)

    def salvar(self):
        try:
            arquivo_part = open('Participantes.txt', 'a')
            arquivo_part.write(self.nome + '\n')
            arquivo_part.write(self.email + '\n')
            arquivo_part.write(self.celular + '\n')
            arquivo_part.close()

        except Exception as erro:
            print(f"O problema encontrado foi {erro.__class__}")