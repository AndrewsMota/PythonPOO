import ParticipanteReuniao as p
import ParticipanteInterno as pi
import Ata as a
import os.path
import Pessoa as pe

a = a.Ata()
reuniao = p.ParticipanteReuniao()
interno = pi.ParticipanteInterno()

loop = 0


while loop == 0:
    try:
        while True:
            menu = int(input(
                            f"\n[1] Menu ATA\n"
                            f"[2] Menu Participante\n"
                            f"[3] Sair\n"))

            if menu == 1:
                menu = int(input(
                                f"\n[1] Emitir ata\n"
                                f"[2] Exibir ata.txt\n"
                                f"[3] Sugestão\n"
                                f"[4] Salvar\n"
                                f"[5] Concluir a ata\n"
                                f"[6] Voltar\n"))

                if menu == 1:
                    interno.verificar_emissor()
                    if interno.cont == 1:
                        a.emitir()
                    else:
                        print("\nNão há um emissor .")

                elif menu == 2:
                    a.exibir()

                elif menu == 3:
                    interno.verificar_emissor()
                    if interno.cont == 1:
                        print("\nO emissor concordou ?")
                        a = str(input("S/N\n"))
                        if a == 'S' or a == 's':
                            a.emitir()
                    else:
                        print("\nNão há um emissor cadastrado.")

                elif menu == 4:
                    try:
                        a.salvar()
                        os.system('cls' if os.name == 'nt' else 'clear')
                    except AttributeError:
                        print('\nNão existe Ata para ser salva !')    
                        

                elif menu == 5:
                    try:
                        a.concluir()
                    except AttributeError:
                        ('\nNão existe Ata para ser concluida !')

                elif menu >= 6:                    
                    os.system('cls' if os.name == 'nt' else 'clear')    

            elif menu == 2:
                menu = int(input(
                                f"\n[1] Cadastrar participante interno\n"
                                f"[2] Cadastrar participante externo\n"
                                f"[3] Apagar Participantes\n"
                                f"[4] Exibir Participantes\n"
                                f"[5] Voltar\n"))
                if menu == 1:
                    reuniao.CadastroPI()
                elif menu == 2:
                    reuniao.CadastroPE()
                elif menu == 3:
                    reuniao.Apagar()
                elif menu == 4:
                    try:    
                        reuniao.ExibirPI()
                        reuniao.ExibirPE()
                    except FileNotFoundError:
                        print('Não existem participantes cadastrados !')

            elif menu == 3:
                loop = loop+1
                break

    except ValueError:
        print('\nOpção incorreta !!')