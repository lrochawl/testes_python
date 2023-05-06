hora_ini, minuto_ini, hora_final, minuto_final = (int (x) for x in input().split() )

hora_ini = int(hora_ini) * 60 + minuto_ini
hora_final = int(hora_final) * 60 + minuto_final

duracao_jogo = hora_final - hora_ini

if(duracao_jogo <= 0):
    duracao_jogo = 24 * 60 - duracao_jogo

minutos = duracao_jogo % 60
horas = duracao_jogo // 60

print("O JOGO DUROU "+str(horas)+" HORA(S) E "+str(minutos)+" MINUTO(S)")