import datetime
import os.path

class Ata():
    def _init_(self):
        self.titulo = ""
        self.dataEmissao = 0
        self.inicio = 0
        self.termino = 0
        self.pauta = ""
        self.descricao = ""
        self.palavraChave = ""
        self.tipo = ""
        self.status = ""

    def emitir(self):
        self.titulo = input("Titulo: ")
        data_atual = datetime.datetime.today()
        self.dataEmissao = data_atual
        self.inicio = data_atual
        self.pauta = input("Pauta: ")
        self.descricao = input("Descrição: ")
        self.palavraChave = input("Palavra Chave: ")
        self.tipo = input("Tipo: ")
        self.status = input("Status: ")

    def exibir(self):
        try:
            file = open('atas.txt', 'r')
            atas = file.read()
            print(atas)
            file.close()
        except:
            print('Nenhuma ata foi salva!.')

    def concluir(self):
        data_atual = datetime.datetime.today()
        self.termino = data_atual
        file = open('atas.txt', 'w')
        file.write(f'\nTitulo: {self.titulo}')
        file.write(f'\nEmissao: {self.dataEmissao}')
        file.write(f'\nInicio: {self.inicio}')
        file.write(f'\nTermino: {self.termino}')
        file.write(f'\nPauta: {self.pauta}')
        file.write(f'\nDescricao: {self.descricao}')
        file.write(f'\nPalavra-chave: {self.palavraChave}')
        file.write(f'\nTipo: {self.tipo}')
        file.write(f'\nStatus: {self.status}')
        file.close

    def salvar(self):
        file = open('atas.txt', 'w')
        file.write(f'\nTitulo: {self.titulo}')
        file.write(f'\nEmissao: {self.dataEmissao}')
        file.write(f'\nInicio: {self.inicio}')
        file.write(f'\nPauta: {self.pauta}')
        file.write(f'\nDescricao: {self.descricao}')
        file.write(f'\nPalavra-chave: {self.palavraChave}')
        file.write(f'\nTipo: {self.tipo}')
        file.write(f'\nStatus: {self.status}')
        file.close

    def enviarRevisao(self):
        if os.path.exists('atas.txt') == True:
            file = open('atas.txt', 'r')
            self.lista = file.readlines()
            file.close()