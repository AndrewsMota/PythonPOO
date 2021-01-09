import ParticipanteExterno as pe
import ParticipanteInterno as pi
import os.path


class ParticipanteReuniao():
    def __init__(self):
        self.Externo = pe.ParticipanteExterno()
        self.Interno = pi.ParticipanteInterno()

    def CadastroPE(self):
        while True:
            print("\n Participante externo")
            self.Externo.incluir()
            print("\nConfira os dados")
            self.Externo.exibir()
            print("\n Os dados estão corretos? ")
            menu = str(input("S/N\n"))
            if menu == 'S' or menu == 's':
                self.Externo.salvar()
                break
            elif menu == 'N' or menu == 'n':
                print('\n Deseja reinserir?')
                menu = str(input("S/N\n"))
                if menu == 'N' or menu == 'n':
                    break

    def CadastroPI(self):
        while True:
            print("\nParticipante interno")
            self.Interno.incluir()
            print("\nConfira os dados ")
            self.Interno.exibir()
            print("\n Os dados estão corretos?")
            menu = str(input("S/N\n"))
            if menu == 'S' or menu == 's':
                if os.path.exists('Participante.txt'):
                    self.Interno.verificar_emissor()
                if self.Interno.cont == 0:
                    print("\n O participante é o emissor?")
                    a = str(input("S/N\n"))
                    if a == 'S' or a == 's':
                        self.Interno.emissor = ''
                self.Interno.salvar()
                break
            elif menu == 'N' or menu == 'n':
                print('\n Deseja inserir os dados novamente?')
                menu = str(input("S/N\n"))
                if menu == 'N' or menu == 'n':
                    break

    def Apagar(self):
        print("\n Tem certeza? ")
        menu = str(input("S/N\n"))
        if menu == 'S' or menu == 's':
            try:
                if os.path.exists('Participantes.txt'):
                    arquivo_part = open('Participantes.txt', 'w')
                    arquivo_part.close()

            except Exception as erro:
                print(f"O problema encontrado foi {erro.__class__}")

    def ExibirPI(self):
        print('\n')
        # Imprime todos os participantes internos
        cont = 10
        arquivo_part = open('Participantes.txt', 'r')
        for linha0 in arquivo_part:
            linha = linha0.strip()
            if linha == ' Participante interno':
                cont = 0
            if cont < 9:
                print(linha)
                cont = cont + 1
        arquivo_part.close()

    def ExibirPE(self):
        # Imprime todos os participantes externos
        cont = 10
        arquivo_part = open('Participantes.txt', 'r')
        for linha0 in arquivo_part:
            linha = linha0.strip()
            if linha == ' Participante externo':
                cont = 0
            if cont < 5:
                print(linha)
                cont = cont + 1
        arquivo_part.close()
        print('\n')