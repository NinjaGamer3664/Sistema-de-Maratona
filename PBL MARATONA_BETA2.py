# Autor: Cauan Dos Reis Almeida
# Componente Curricular: MI Algoritmos
# Concluído em: 14 de Setembro de 2024 
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

print(100*'-' + '\033[1m\033[48;5;93m' + f'\n{"RANKING MAKER":^100}\n' + f'{"JUNGUICUQUI APPS":^100}\n' + '\033[0m' + 100*'-')

valor1 = float(input('\033[38;5;82m' + 'Digite o valor das questões fáceis[decimal permitido, use ponto]:' + '\033[0m'))
valor2 = float(input('\033[38;5;82m' + 'Digite o valor das questões médias[decimal permitido, use ponto]:' + '\033[0m'))
valor3 = float(input('\033[38;5;82m' + 'Digite o valor das questões difíceis[decimal permitido, use ponto]:' + '\033[0m'))

print(f"{100*'-'}\n")

#Verifica e garante que as pontuações seguem um peso justo
if not valor1 < valor2 < valor3:
   print('\033[38;5;130m' + 'As difíceis devem ser maiores que as médias, que devem ser msiores que as fáceis!')
elif valor1 < valor2 < valor3:
    equipe1 = input('\033[38;5;33m' + 'Defina o nome da primeira equipe:\n' + '\033[0m')
    equipe2 = input('\033[38;5;33m' + 'Defina o nome da segunda equipe:\n' + '\033[0m')
    equipe3 = input('\033[38;5;33m' + 'Defina o nome da terceira equipe:\n' + '\033[0m')
    equipe4 = input('\033[38;5;33m' + 'Defina o nome da quarta equipe:\n' + '\033[0m')
    equipe5 = input('\033[38;5;33m' + 'Defina o nome da quinta equipe:\n' + '\033[0m')
    
    print(f"{100*'-'}\n")

    if str.upper(equipe1) == str.upper(equipe2) or str.upper(equipe1) == str.upper(equipe3) or str.upper(equipe1) == str.upper(equipe4) or str.upper(equipe1) == str.upper(equipe5):
        print('\033[38;5;130m' + 'Nome de equipes foram repetidos! Recomeçe o programa.')
    elif str.upper(equipe2) == str.upper(equipe3) or str.upper(equipe2) == str.upper(equipe4) or str.upper(equipe2) == str.upper(equipe5):
        print('\033[38;5;130m' + 'Nome de equipes foram repetidos! Recomeçe o programa.')
    elif str.upper(equipe3) == str.upper(equipe4) or str.upper(equipe3) == str.upper(equipe5):
        print('\033[38;5;130m' + 'Nomes de equipes foram repetidos! Recomeçe o programa.')
    elif str.upper(equipe4) == str.upper(equipe5):
        print('\033[38;5;130m' + 'Nomes de equipes foram repetidos! Recomeçe o programa.')
    else:
        #valores globais da equipa 1
        tempo_total_horas1 = 0
        tempo_total_minutos1 = 0
        tempo_total_segundos1 = 0
        pontuação1 = 0
        número_questões1 = 0
        medpon1 = 0
        qf1 = 0
        qm1 = 0
        qd1 = 0

        #valores globais equipe 2
        tempo_total_horas2 = 0
        tempo_total_minutos2 = 0
        tempo_total_segundos2 = 0
        pontuação2 = 0
        número_questões2 = 0
        medpon2 = 0
        qf2 = 0
        qm2 = 0
        qd2 = 0

        #valores globais equipe 3
        tempo_total_horas3 = 0
        tempo_total_minutos3 = 0
        tempo_total_segundos3 = 0
        pontuação3 = 0
        número_questões3 = 0
        medpon3 = 0
        qf3 = 0
        qm3 = 0
        qd3 = 0

        #valores globais equipe 4
        tempo_total_horas4 = 0
        tempo_total_minutos4 = 0
        tempo_total_segundos4 = 0
        pontuação4 = 0
        número_questões4 = 0
        medpon4 = 0
        qf4 = 0
        qm4 = 0
        qd4 = 0

        #valores globais equipe 5
        tempo_total_horas5 = 0
        tempo_total_minutos5 = 0
        tempo_total_segundos5 = 0
        pontuação5 = 0
        número_questões5 = 0
        medpon5 = 0
        qf5 = 0
        qm5 = 0
        qd5 = 0

        #variantes globais gerais
        alteração = ' '
        correta_errada = ' '
        finalizar = ' '
        maisd = 0


        #Todo o programa é lançado num laço de repetição que armazena os dados da competição
        while finalizar != 'sim':
            alteração = input('\033[38;5;208m' + 'Qual equipe deseja atualizar?[DIGITE O NOME DA EQUIPE]\n' + '\033[0m')
            print(f"{100*'-'}\n")
            if alteração == equipe1:
                correta_errada = str(input('\033[38;5;208m' + 'A equipe concluiu o desafio? [sim ou não]\n' + '\033[0m'))
                print(f"{100*'-'}\n")
                if correta_errada == 'não':
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n" + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    print(f"{100*'-'}\n")
                    #soma e guarda os valores de tempo
                    tempo_total_minutos1 += tempo_minuto
                    tempo_total_segundos1 += tempo_segundos

                    #Conversor de tempo 
                    if tempo_total_segundos1 > 59:
                        tempo_total_minutos1 += 1
                        tempo_total_segundos1 -= 60
                    if tempo_total_minutos1 > 59:
                        tempo_total_minutos1 -= 60
                        tempo_total_horas1 += 1


                elif correta_errada == 'sim':
                    #Calcula a pontuação da equipe
                    número_questões1 += 1
                    dificuldade = int(input('\033[38;5;208m' + 'Qual foi a dificuldade da questão?\n'
                                            '1 = Fácil, 2 = Média, 3 = Difícil\n' + '\033[0m'))

                    if dificuldade == 1:
                        pontuação1 += valor1
                        qf1 += 1
                    elif dificuldade == 2:
                        pontuação1 += valor2
                        qm1 += 1
                    elif dificuldade == 3:
                        pontuação1 += valor3
                        qd1 += 1
                    if pontuação1 > 0 and número_questões1 > 0:
                        medpon1 = pontuação1 / número_questões1

                    print(f"{100*'-'}\n")
                    #tempo da equipe
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n" + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quanto tempo a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    tempo_total_minutos1 += tempo_minuto
                    tempo_total_segundos1 += tempo_segundos
                    print(f"{100*'-'}\n")
                    if tempo_total_segundos1 > 59:
                        tempo_total_minutos1 += 1
                        tempo_total_segundos1 -= 60
                    if tempo_total_minutos1 > 59:
                        tempo_total_minutos1 -= 60
                        tempo_total_horas1 += 1

                else:
                    print('\033[38;5;130m' + 'Digite apenas sim ou não em MINÚSCULO!')

                
            elif alteração == equipe2:
                correta_errada = str(input('\033[38;5;208m' + 'A equipe concluiu o desafio? [sim ou não]\n' + '\033[0m'))
                print(f"{100*'-'}\n")
                if correta_errada == 'não':
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n" + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    print(f"{100*'-'}\n")
                    tempo_total_minutos2 += tempo_minuto
                    tempo_total_segundos2 += tempo_segundos
                    
                    #conversor de tempo
                    if tempo_total_segundos2 > 59:
                        tempo_total_minutos2 += 1
                        tempo_total_segundos2 -= 60
                    if tempo_total_minutos2 > 59:
                        tempo_total_minutos2 -= 60
                        tempo_total_horas2 += 1

                elif correta_errada == 'sim':
                    #Calcula a pontuação de pontos da equipe
                    número_questões2 += 1
                    dificuldade = int(input('\033[38;5;208m' + 'Qual foi a dificuldade da questão?\n'
                                            '1 = Fácil, 2 = Média, 3 = Difícil\n' + '\033[0m'))
                    print(f"{100*'-'}\n")

                    if dificuldade == 1:
                        pontuação2 += valor1
                        qf2 += 1
                    elif dificuldade == 2:
                        pontuação2 += valor2
                        qm2 += 1
                    elif dificuldade == 3:
                        pontuação2 += valor3
                        qd2 += 1
                    if pontuação2 > 0 and número_questões2 > 0:
                        medpon2 = pontuação2 / número_questões2

                    #conversor de tempo
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n" + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    print(f"{100*'-'}\n")
                    tempo_total_minutos2 += tempo_minuto
                    tempo_total_segundos2 += tempo_segundos
                    
                    if tempo_total_segundos2 > 59:
                        tempo_total_minutos2 += 1
                        tempo_total_segundos2 -= 60
                    if tempo_total_minutos2 > 59:
                        tempo_total_minutos2 -= 60
                        tempo_total_horas2 += 1

                else:
                    print('\033[38;5;130m' + 'Digite apenas sim ou não em MINÚSCULO!' + '\033[0m')
                    print(f"{100*'-'}\n")

            elif alteração == equipe3:
                correta_errada = str(input('\033[38;5;208m' + 'A equipe concluiu o desafio? [sim ou não]\n' + '\033[0m'))
                print(f"{100*'-'}\n")
                if correta_errada == 'não':
                    tempo_minuto = int(input('\033[38;5;208m' + 'Quantos minutos a equipe levou? [APENAS EM MINUTOS]!!!\n' + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    print(f"{100*'-'}\n")
                    tempo_total_minutos3 += tempo_minuto
                    tempo_total_segundos3 += tempo_segundos

                    #Conversor de tempo
                    if tempo_total_segundos3 > 59:
                        tempo_total_minutos3 += 1
                        tempo_total_segundos3 -= 60
                    if tempo_total_minutos3 > 59:
                        tempo_total_minutos3 -= 60
                        tempo_total_horas3 += 1

                elif correta_errada == 'sim':
                    #Calcula a pontuação da equipe
                    número_questões3 += 1
                    dificuldade = int(input('\033[38;5;208m' + 'Qual foi a dificuldade da questão?\n'
                                            '1 = Fácil, 2 = Média, 3' + '\033[0m'))
                    print(f"{100*'-'}\n")

                    if dificuldade == 1:
                        pontuação3 += valor1
                        qf3 += 1
                    elif dificuldade == 2:
                        pontuação3 += valor2
                        qm3 += 1
                    elif dificuldade == 3:
                        pontuação3 += valor3
                        qd3 += 1
                    if pontuação3 > 0 and número_questões3 > 0:
                        medpon3 = pontuação3 / número_questões3
                    
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n" + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    tempo_total_minutos3 += tempo_minuto
                    tempo_total_segundos3 += tempo_segundos
                    print(f"{100*'-'}\n")

                    if tempo_total_segundos3 > 59:
                        tempo_total_minutos3 += 1
                        tempo_total_segundos3 -= 60
                    if tempo_total_minutos3 > 59:
                        tempo_total_minutos3 -= 60
                        tempo_total_horas3 += 1

                else:
                    print('\033[38;5;130m' + 'Digite apenas sim ou não em MINÚSCULO!' + '\033[0m')
                    print(f"{100*'-'}\n")


            elif alteração == equipe4:
                correta_errada = str(input('\033[38;5;208m' + 'A equipe concluiu o desafio? [sim ou não]\n' + '\033[0m'))
                print(f"{100*'-'}\n")
                if correta_errada == 'não':
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n" + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    print(f"{100*'-'}\n")
                    tempo_total_minutos4 += tempo_minuto
                    tempo_total_segundos4 += tempo_segundos
                    
                    #Conversor de tempo
                    if tempo_total_segundos4 > 59:
                        tempo_total_minutos4 += 1
                        tempo_total_segundos4 -= 60
                    if tempo_total_minutos4 > 59:
                        tempo_total_minutos4 -= 60
                        tempo_total_horas4 += 1

                elif correta_errada == 'sim':
                    #Calcula a pontuação da equipe
                    número_questões4 += 1
                    dificuldade = int(input('\033[38;5;208m' + 'Qual foi a dificuldade da questão?\n'
                                            '1 = Fácil, 2 = Média, 3 = Difícil\n' + '\033[0m'))
                    print(f"{100*'-'}\n")

                    if dificuldade == 1:
                        pontuação4 += valor1
                        qf4 += 1
                    elif dificuldade == 2:
                        pontuação4 += valor2
                        qm4 += 1
                    elif dificuldade == 3:
                        pontuação4 += valor3
                        qd4 += 1
                    if pontuação4 > 0 and número_questões4 > 0:
                        medpon4 = pontuação4 / número_questões4
                    
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n" + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    print(f"{100*'-'}\n")
                    tempo_total_minutos4 += tempo_minuto
                    tempo_total_segundos4 += tempo_segundos

                    #conversor de tempo
                    if tempo_total_segundos4 > 59:
                        tempo_total_minutos4 += 1
                        tempo_total_segundos4 -= 60
                    if tempo_total_minutos4 > 59:
                        tempo_total_minutos4 -= 60
                        tempo_total_horas4 += 1

                else:
                    print('\033[38;5;130m' + 'Digite apenas sim ou não em minúsculo!' + '\033[0m')
                    print(f"{100*'-'}\n")

            elif alteração == equipe5:
                correta_errada = str(input('\033[38;5;208m' + 'A equipe concluiu o desafio? [sim ou não]\n' + '\033[0m'))
                print(f"{100*'-'}\n")
                if correta_errada == 'não':
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n" + '\033[0m'))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    print(f"{100*'-'}\n")
                    tempo_total_minutos5 += tempo_minuto
                    tempo_total_segundos5 += tempo_segundos
                    
                    #Conversor de tempo
                    if tempo_total_segundos5 > 59:
                        tempo_total_minutos5 += 1
                        tempo_total_segundos5 -= 60
                    if tempo_total_minutos5 > 59:
                        tempo_total_minutos5 -= 60
                        tempo_total_horas5 += 1

                elif correta_errada == 'sim':
                    #Calcula a pontuação da equipe
                    número_questões5 += 1
                    dificuldade = int(input('\033[38;5;208m' + 'Qual foi a dificuldade da questão?\n'
                                            '1 = Fácil, 2 = Média, 3 = Difícil\n' + '\033[0m'))
                    print(f"{100*'-'}\n")

                    if dificuldade == 1:
                        pontuação5 += valor1
                        qf5 += 1
                    elif dificuldade == 2:
                        pontuação5 += valor2
                        qm5 += 1
                    elif dificuldade == 3:
                        pontuação5 += valor3
                        qd5 += 1
                    if pontuação5 > 0 and número_questões5 > 0:
                        medpon5 = pontuação5 / número_questões5
                    
                    tempo_minuto = int(input('\033[38;5;208m' + "Quantos minutos a equipe levou? [APENAS EM MINUTOS!!!]\n"))
                    tempo_segundos = int(input('\033[38;5;208m' + 'Quantos segundos a equipe levou? [APENAS EM SEGUNDOS!!!]\n' + '\033[0m'))
                    print(f"{100*'-'}\n")
                    tempo_total_minutos5 += tempo_minuto
                    tempo_total_segundos5 += tempo_segundos

                    #conversor de tempo
                    if tempo_total_segundos5 > 59:
                        tempo_total_minutos5 += 1
                        tempo_total_segundos5 -= 60
                    if tempo_total_minutos5 > 59:
                        tempo_total_minutos5 -= 60
                        tempo_total_horas5 += 1

                else:
                    print('\033[38;5;130m' + 'Digite apenas sim ou não em MINÚSCULO!' + '\033[0m')
                    print(f"{100*'-'}\n")

            #variantes do ranking
            c1 = equipe1
            c2 = equipe2
            c3 = equipe3
            c4 = equipe4
            c5 = equipe5
            pc1 = pontuação1
            pc2 = pontuação2
            pc3 = pontuação3
            pc4 = pontuação4
            pc5 = pontuação5
            mpc1 = medpon1
            mpc2 = medpon2
            mpc3 = medpon3
            mpc4 = medpon4
            mpc5 = medpon5
            fc1 = qf1
            fc2 = qf2
            fc3 = qf3
            fc4 = qf4
            fc5 = qf5
            mc1 = qm1
            mc2 = qm2
            mc3 = qm3
            mc4 = qm4
            mc5 = qm5
            dc1 = qd1
            dc2 = qd2
            dc3 = qd3
            dc4 = qd4
            dc5 = qd5
            tc1 = ((tempo_total_horas1*60)+tempo_total_minutos1)*60+tempo_total_segundos1
            tc2 = ((tempo_total_horas2*60)+tempo_total_minutos2)*60+tempo_total_segundos2
            tc3 = ((tempo_total_horas3*60)+tempo_total_minutos3)*60+tempo_total_segundos3
            tc4 = ((tempo_total_horas4*60)+tempo_total_minutos4)*60+tempo_total_segundos4
            tc5 = ((tempo_total_horas5*60)+tempo_total_minutos5)*60+tempo_total_segundos5
            tr1 = f'{tempo_total_horas1:02}:{tempo_total_minutos1:02}:{tempo_total_segundos1:02}'
            tr2 = f'{tempo_total_horas2:02}:{tempo_total_minutos2:02}:{tempo_total_segundos2:02}'
            tr3 = f'{tempo_total_horas3:02}:{tempo_total_minutos3:02}:{tempo_total_segundos3:02}'
            tr4 = f'{tempo_total_horas4:02}:{tempo_total_minutos4:02}:{tempo_total_segundos4:02}'
            tr5 = f'{tempo_total_horas5:02}:{tempo_total_minutos5:02}:{tempo_total_segundos5:02}'
                
            for i in range(6):
                if pc1 < pc2 or (pc1 == pc2 and dc1 < dc2) or (pc1 == pc2 and dc1 == dc2 and tc1 > tc2):
                    c1, c2 = c2, c1
                    pc1, pc2 = pc2, pc1
                    fc1, fc2 = fc2, fc1
                    mc1, mc2 = mc2, mc1
                    dc1, dc2 = dc2, dc1
                    mpc1, mpc2 = mpc2, mpc1
                    tc1, tc2 = tc2, tc1
                    tr1, tr2 = tr2, tr1
                if pc2 < pc3 or (pc2 == pc3 and dc2 < dc3) or (pc2 == pc3 and dc2 == dc3 and tc2 > tc3):
                    c2, c3 = c3, c2
                    pc2, pc3 = pc3, pc2
                    fc2, fc3 = fc3, fc2
                    mc2, mc3 = mc3, mc2
                    dc2, dc3 = dc3, dc2
                    mpc2, mpc3 = mpc3, mpc2
                    tc2, tc3 = tc3, tc2
                    tr2, tr3 = tr3, tr2
                if pc3 < pc4 or (pc3 == pc4 and dc3 < dc4) or (pc3 == pc4 and dc3 == dc4 and tc3 > tc4):
                    c3, c4 = c4, c3
                    pc3, pc4 = pc4, pc3
                    fc3, fc4 = fc4, fc3
                    mc3, mc4 = mc4, mc3
                    dc3, dc4 = dc4, dc3
                    mpc3, mpc4 = mpc4, mpc3
                    tc3, tc4 = tc4, tc3
                    tr3, tr4 = tr4, tr3
                if pc4 < pc5 or (pc4 == pc5 and dc4 < dc5) or (pc4 == pc5 and dc4 == dc5 and tc4 > tc5):
                    c4, c5 = c5, c4
                    pc4, pc5 = pc5, pc4
                    fc4, fc5 = fc5, fc4
                    mc4, mc5 = mc5, mc4
                    dc4, dc5 = dc5, dc4
                    mpc4, mpc5 = mpc5, mpc4
                    tc4, tc5 = tc5, tc4
                    tr4, tr5 = tr5, tr4
            for i in range(6):
                if maisd < qd1:
                    maisd = qd1
                elif maisd < qd2:
                    maisd = qd2
                elif maisd < qd3:
                    maisd = qd3
                elif maisd < qd4:
                    maisd = qd4
                elif maisd < qd5:
                    maisd = qd5

            print('\033[38;5;94m' + f'{"EQUIPES":^10}' + f'{"PONTOS":^20}' + f'{"DIFÍCEIS"}' + f'{"TEMPO":^22}\n' + '\033[0m' +
                  '\033[38;5;205m' + f'1° {c1:15} {pc1:^1.1f} {dc1:13} {tr1:^25}\n' + '\033[0m' +
                  '\033[38;5;183m' + f'2° {c2:15} {pc2:^1.1f} {dc2:13} {tr2:^25}\n' + '\033[0m' +
                  '\033[0;34m' + f'3° {c3:15} {pc3:^1.1f} {dc3:13} {tr3:^25}\n' + '\033[0m' +
                  '\033[0;33m' + f'4° {c4:15} {pc4:^1.1f} {dc4:13} {tr4:^25}\n' + '\033[0m' +
                  '\033[0;36m' + f'5° {c5:15} {pc5:^1.1f} {dc5:13} {tr5:^25}\n' + '\033[0m')
            
            #finaliza o laço de repetição e imprime os valores obtidos na saída
            finalizar = input('\033[38;5;106m' + 'Deseja finalizar?[sim em minúsculo para encerrar programa]\n')
            if finalizar == 'sim':
                print(f"{100*'-'}\n")
                print('\033[0;31m\033[0;107m' + f'A equipe vencedora é {c1} com a pontuação {pc1} e tempo {tr1}' + '\033[0m')
                print(f"{100*'-'}\n")
                print('\033[38;5;94m' + f'{"EQUIPES":^10} {"PONTOS":^20} {"MÉD. DE PON.":^2} {"FÁCEIS":10} {"MÉDIAS":^10} {"DIFÍCEIS":^10} {"TEMPO":^15}\n' + '\033[0m' +
                      '\033[38;5;205m' + f'1° {c1:15} {pc1:1.1f} {mpc1:15.1f} {fc1:8} {mc1:13} {dc1:10} {tr1:^25}\n' + '\033[0m' +
                      '\033[38;5;183m' + f'2° {c2:15} {pc2:1.1f} {mpc2:15.1f} {fc2:8} {mc2:13} {dc2:10} {tr2:^25}\n' + '\033[0m' +
                      '\033[0;34m' + f'3° {c3:15} {pc3:1.1f} {mpc3:15.1f} {fc3:8} {mc3:13} {dc3:10} {tr3:^25}\n' + '\033[0m' +
                      '\033[0;33m' + f'4° {c4:15} {pc4:1.1f} {mpc4:15.1f} {fc4:8} {mc4:13} {dc4:10} {tr4:^25}\n' + '\033[0m' +
                      '\033[0;36m' + f'5° {c5:15} {pc5:1.1f} {mpc5:15.1f} {fc5:8} {mc5:13} {dc5:10} {tr5:^25}\n' + '\033[0m')
                print(f"{100*'-'}\n")
                if maisd == 0:
                    print('\033[0;105m\033[0;32m' + 'Nenhuma equipe acertou questões difíceis!' + '\033[0m')
                elif maisd == qd1:
                    print('\033[0;105m\033[0;32m' + f"A equipe que mais acertou problemas difíceis foi a {equipe1} com {maisd}" + '\033[0m')
                elif maisd == qd2:
                    print('\033[0;105m\033[0;32m' + f"A equipe que mais acertou problemas difíceis foi a {equipe2} {maisd}" + '\033[0m')
                elif maisd == qd3:
                    print('\033[0;105m\033[0;32m' + f"A equipe que mais acertou problemas difíceis foi a {equipe3} {maisd}" + '\033[0m')
                elif maisd == qd4:
                    print('\033[0;105m\033[0;32m' + f"A equipe que mais acertou problemas difíceis foi a {equipe4} {maisd}" + '\033[0m')
                elif maisd == qd5:
                    print('\033[0;105m\033[0;32m' + f"A equipe que mais acertou problemas difíceis foi a {equipe5} {maisd}" + '\033[0m')
print(100*'-' + '\033[1m\033[48;5;93m' + f'\n{"FIM DO PROGRAMA":^100}\n' + f'{"OBRIGADO POR JOGAR":^100}\n' + '\033[0m' + 100*'-')
