# Fases:
# 1 -> Fase de grupos
# 2 -> Oitavas de final
# 3 -> Quartas de final
# 4 -> Semifinal
# 5 -> 3 lugar
# 6 -> Final

fase_de_grupos = 1
oitavas = 2
quartas = 3
semifinais = 4
terceiro_lugar = 5
final = 6

empate = None

primeiro = 0
segundo = 1


def merge_lists(list_of_lists):
  merge = []
  for list in list_of_lists:
    merge += list

  return merge

def unique_teams(list_of_plays):
  teams = set(merge_lists(list_of_plays))
  return teams

def validate_teams(list_of_plays):
  result = True if len(unique_teams(list_of_plays)) == 32 else False
  return result

#copa 2010
plays_2010 = [
    ['AFS', 'MEX']
    ,['URU', 'FRA']
    ,['AFS', 'URU']
    ,['FRA', 'MEX']
    ,['MEX', 'URU']
    ,['FRA', 'AFS']# grupo A
    ,['COR', 'GRE']
    ,['ARG', 'NIG']
    ,['ARG', 'COR']
    ,['GRE', 'NIG']
    ,['NIG', 'COR']
    ,['GRE', 'ARG']# grupo B
    ,['ING', 'EUA']
    ,['AGL', 'ESL']
    ,['ESL', 'EUA']
    ,['ING', 'AGL']
    ,['ESL', 'ING']
    ,['EUA', 'AGL']# grupo C
    ,['SER', 'GAN']
    ,['ALE', 'AUS']
    ,['ALE', 'SER']
    ,['GAN', 'AUS']
    ,['GAN', 'ALE']
    ,['AUS', 'SER']# grupo D
    ,['HOL', 'DIN']
    ,['JAP', 'CAM']
    ,['HOL', 'JAP']
    ,['CAM', 'DIN']
    ,['DIN', 'JAP']
    ,['CAM', 'HOL']# grupo E
    ,['ITA', 'PAR']
    ,['NZE', 'EVQ']
    ,['EVQ', 'PAR']
    ,['ITA', 'NZE']
    ,['EVQ', 'ITA']
    ,['PAR', 'NZE']# grupo F
    ,['CDM', 'POR']
    ,['BRA', 'CNO']
    ,['BRA', 'CDM']
    ,['POR', 'CNO']
    ,['POR', 'BRA']
    ,['CNO', 'CDM']# grupo G
    ,['HON', 'CHI']
    ,['ESP', 'SUI']
    ,['CHI', 'SUI']
    ,['ESP', 'HON']
    ,['CHI', 'ESP']
    ,['SUI', 'HON']# grupo H
    ,['URU', 'COR']
    ,['EUA', 'GAN']
    ,['HOL', 'EVQ']
    ,['BRA', 'CHI']
    ,['ARG', 'MEX']
    ,['ALE', 'ING']
    ,['PAR', 'JAP']
    ,['ESP', 'POR']# oitavas
    ,['URU', 'GAN']
    ,['HOL', 'BRA']
    ,['ARG', 'ALE']
    ,['PAR', 'ESP']#quartas
    ,['URU', 'HOL']
    ,['ALE', 'ESP']#semifinais
    ,['URU', 'ALE']#terceiro_lugar
    ,['HOL', 'ESP']#final
]

results_2010 = [
    [1, 1, empate, fase_de_grupos]  # [jogo[gols_t1, gols_t2, vencedor, fase]
    ,[0, 0, empate, fase_de_grupos]
    ,[0, 3, segundo, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]# grupo A
    ,[2, 0, primeiro, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[4, 1, primeiro, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[2, 2, empate, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]# grupo B
    ,[1, 1, empate, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[2, 2, empate, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]# grupo C
    ,[0, 1, segundo, fase_de_grupos]
    ,[4, 0, primeiro, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]# grupo D
    ,[2, 0, primeiro, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]
    ,[1, 3, segundo, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]# grupo E
    ,[1, 1, empate, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[3, 2, primeiro, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]# grupo F
    ,[0, 0, empate, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[3, 1, primeiro, fase_de_grupos]
    ,[7, 0, primeiro, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[0, 3, segundo, fase_de_grupos]# grupo G
    ,[0, 1, segundo, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]# grupo H
    ,[2, 1, primeiro, oitavas]
    ,[1, 2, segundo, oitavas]
    ,[2, 1, primeiro, oitavas]
    ,[3, 0, primeiro, oitavas]
    ,[3, 1, primeiro, oitavas]
    ,[4, 1, primeiro, oitavas]
    ,[0, 0, primeiro, oitavas]
    ,[1, 0, primeiro, oitavas]#oitavas
    ,[1, 1, primeiro, quartas]
    ,[2, 1, primeiro, quartas]
    ,[0, 4, segundo, quartas]
    ,[0, 1, segundo, quartas]#quartas
    ,[2, 3, segundo, semifinais]
    ,[0, 1, segundo, semifinais]#semifinais
    ,[2, 3, segundo, terceiro_lugar]#terceiro_lugar
    ,[0, 1, segundo, final]#final
]

#Copa 2014  
plays_2014 = [
     ['BRA', 'CRO']
    ,['MEX', 'CMR']
    ,['BRA', 'MEX']
    ,['CMR', 'CRO']
    ,['CMR', 'BRA']
    ,['CRO', 'MEX']#GRUPO A
    ,['ESP', 'HOL']
    ,['CHI', 'AUS']
    ,['AUS', 'HOL']
    ,['ESP', 'CHI']
    ,['AUS', 'ESP']
    ,['HOL', 'CHI']#grupo B
    ,['COL', 'GRE']
    ,['CDM', 'JAP']
    ,['COL', 'CDM']
    ,['JAP', 'GRE']
    ,['GRE', 'CDM']
    ,['JAP', 'COL']#grupo C
    ,['URU', 'CRC']
    ,['ING', 'ITA']
    ,['URU', 'ING']
    ,['ITA', 'CRC']
    ,['CRC', 'ING']
    ,['ITA', 'URU']#grupo D
    ,['SUI', 'EQU']
    ,['FRA', 'HON']
    ,['SUI', 'FRA']
    ,['HON', 'EQU']
    ,['EQU', 'FRA']
    ,['HON', 'SUI']#grupo E
    ,['ARG', 'BOS']
    ,['IRA', 'NIG']
    ,['ARG', 'IRA']
    ,['NIG', 'BOS']
    ,['BOS', 'IRA']
    ,['NIG', 'ARG']#grupo F
    ,['ALE', 'POR']
    ,['GAN', 'EUA']
    ,['ALE', 'GAN']
    ,['EUA', 'POR']
    ,['POR', 'GAN']
    ,['EUA', 'ALE']#grupo G
    ,['BEL', 'AGL']
    ,['RUS', 'COR']
    ,['BEL', 'RUS']
    ,['COR', 'AGL']
    ,['AGL', 'RUS']
    ,['COR', 'BEL']#grupo H
    ,['BRA', 'CHI']
    ,['COL', 'URU']
    ,['FRA', 'NIG']
    ,['ALE', 'AGL']
    ,['HOL', 'MEX']
    ,['CRC', 'GRE']
    ,['ARG', 'SUI']
    ,['BEL', 'EUA']# oitavas
    ,['BRA', 'COL']
    ,['FRA', 'ALE']
    ,['HOL', 'CRC']
    ,['ARG', 'BEL']#quartas
    ,['BRA', 'ALE']
    ,['HOL', 'ARG']#semifinais
    ,['BRA', 'HOL']#terceiro_lugar
    ,['ALE', 'ARG']#final
]

results_2014 = [
    [3, 1, primeiro, fase_de_grupos]  # [jogo[gols_t1, gols_t2, vencedor, fase]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[0, 4, segundo, fase_de_grupos]
    ,[1, 4, segundo, fase_de_grupos]
    ,[1, 3, segundo, fase_de_grupos]#grupo A
    ,[1, 5, segundo, fase_de_grupos]
    ,[3, 1, primeiro, fase_de_grupos]
    ,[2, 3, segundo, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]
    ,[0, 3, segundo, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]#grupo B
    ,[3, 0, primeiro, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[1, 4, segundo, fase_de_grupos]#grupo C
    ,[1, 3, segundo, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]#grupo D
    ,[2, 1, primeiro, fase_de_grupos]
    ,[3, 0, primeiro, fase_de_grupos]
    ,[2, 5, segundo, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[0, 3, segundo, fase_de_grupos]#grupo E
    ,[2, 1, primeiro, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[3, 1, primeiro, fase_de_grupos]
    ,[2, 3, segundo, fase_de_grupos]#grupo F
    ,[4, 0, primeiro, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]
    ,[2, 2, empate, fase_de_grupos]
    ,[2, 2, empate, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]#grupo G
    ,[2, 1, primeiro, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[2, 4, segundo, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]#grupo H
    ,[1, 1, primeiro, oitavas]
    ,[2, 0, primeiro, oitavas]
    ,[2, 0, primeiro, oitavas]
    ,[2, 1, primeiro, oitavas]
    ,[2, 1, primeiro, oitavas]
    ,[1, 1, primeiro, oitavas]
    ,[1, 0, primeiro, oitavas]
    ,[2, 1, primeiro, oitavas]#oitavas
    ,[2, 1, primeiro, quartas]
    ,[0, 1, segundo, quartas]
    ,[0, 0, primeiro, quartas]
    ,[1, 0, primeiro, quartas]#quartas
    ,[1, 7, segundo, semifinais]
    ,[0, 0, segundo, semifinais]#semifinais
    ,[0, 3, segundo, terceiro_lugar]#terceiro_lugar
    ,[1, 0, primeiro, final]#final
]

#copa 2018
plays_2018 = [
     ['RUS', 'ARS']
    ,['EGI', 'URU']
    ,['RUS', 'EGI']
    ,['URU', 'ARS']
    ,['URU', 'RUS']
    ,['ARS', 'EGI']#GRUPO A
    ,['MAR', 'IRA']
    ,['POR', 'ESP']
    ,['POR', 'MAR']
    ,['IRA', 'ESP']
    ,['IRA', 'POR']
    ,['ESP', 'MAR']#GRUPO B
    ,['FRA', 'AUS']
    ,['PER', 'DIN']
    ,['DIN', 'AUS']
    ,['FRA', 'PER']
    ,['DIN', 'FRA']
    ,['AUS', 'PER']#GRUPO C
    ,['ARG', 'ISL']
    ,['CRO', 'NIG']
    ,['ARG', 'CRO']
    ,['NIG', 'ISL']
    ,['NIG', 'ARG']
    ,['ISL', 'CRO']#GRUPO D
    ,['CRC', 'SER']
    ,['BRA', 'SUI']
    ,['BRA', 'CRC']
    ,['SER', 'SUI']
    ,['SER', 'BRA']
    ,['SUI', 'CRC']#GRUPO E
    ,['ALE', 'MEX']
    ,['SUE', 'COR']
    ,['COR', 'MEX']
    ,['ALE', 'SUE']
    ,['COR', 'ALE']
    ,['MEX', 'SUE']#GRUPO F
    ,['BEL', 'PAN']
    ,['TUN', 'ING']
    ,['BEL', 'TUN']
    ,['ING', 'PAN']
    ,['ING', 'BEL']
    ,['PAN', 'TUN']#GRUPO G
    ,['COL', 'JAP']
    ,['POL', 'SEN']
    ,['JAP', 'SEN']
    ,['POL', 'COL']
    ,['JAP', 'POL']
    ,['SEN', 'COL']#GRUPO H
    ,['URU', 'POL']
    ,['FRA', 'ARG']
    ,['BRA', 'MEX']
    ,['BEL', 'JAP']
    ,['ESP', 'RUS']
    ,['CRO', 'DIN']
    ,['SUE', 'SUI']
    ,['COL', 'ING']# oitavas
    ,['URU', 'FRA']
    ,['BRA', 'BEL']
    ,['RUS', 'CRO']
    ,['SUE', 'ING']#quartas
    ,['FRA', 'BEL']
    ,['CRO', 'ING']#semifinais
    ,['BEL', 'ING']#terceiro_lugar
    ,['FRA', 'CRO']#final
]

results_2018 = [
     [5, 0, primeiro, fase_de_grupos]  # [jogo[gols_t1, gols_t2, vencedor, fase]
    ,[0, 1, segundo, fase_de_grupos]
    ,[3, 1, primeiro, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[3, 0, primeiro, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]#grupo A
    ,[0, 1, segundo, fase_de_grupos]  
    ,[3, 3, empate, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[2, 2, empate, fase_de_grupos]#grupo B
    ,[2, 1, primeiro, fase_de_grupos]  
    ,[0, 1, segundo, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]#grupo C
    ,[1, 1, empate, fase_de_grupos]  
    ,[2, 0, primeiro, fase_de_grupos]
    ,[0, 3, segundo, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]#grupo D
    ,[0, 1, segundo, fase_de_grupos]  
    ,[1, 1, empate, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]
    ,[2, 2, empate, fase_de_grupos] #grupo E
    ,[0, 1, segundo, fase_de_grupos]  
    ,[1, 0, primeiro, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]
    ,[0, 3, segundo, fase_de_grupos]#grupo F
    ,[3, 0, primeiro, fase_de_grupos]  
    ,[1, 2, segundo, fase_de_grupos]
    ,[5, 2, primeiro, fase_de_grupos]
    ,[6, 1, primeiro, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]#grupo G
    ,[1, 2, segundo, fase_de_grupos]  
    ,[1, 2, segundo, fase_de_grupos]
    ,[2, 2, empate, fase_de_grupos]
    ,[0, 3, segundo, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]#grupo H
    ,[2, 1, primeiro, oitavas]
    ,[4, 3, primeiro, oitavas]
    ,[2, 0, primeiro, oitavas]
    ,[3, 2, primeiro, oitavas]
    ,[1, 1, segundo, oitavas]
    ,[1, 1, primeiro, oitavas]
    ,[1, 0, primeiro, oitavas]
    ,[1, 1, segundo, oitavas]#oitavas
    ,[0, 2, segundo, quartas]
    ,[1, 2, segundo, quartas]
    ,[2, 2, segundo, quartas]
    ,[0, 2, segundo, quartas]#quartas
    ,[1, 0, primeiro, semifinais]
    ,[2, 1, segundo, semifinais]#semifinais
    ,[2, 0, primeiro, terceiro_lugar]#terceiro_lugar
    ,[4, 2, primeiro, final]#final
]
    
#copa 2022
plays_2022 = [
     ['CAT', 'EQU']
    ,['SEN', 'HOL']
    ,['CAT', 'SEN']
    ,['HOL', 'EQU']
    ,['HOL', 'CAT']
    ,['EQU', 'SEN']#GRUPO A
    ,['ING', 'IRA']
    ,['EUA', 'GAL']
    ,['GAL', 'IRA']
    ,['ING', 'EUA']
    ,['IRA', 'EUA']
    ,['GAL', 'ING']#GRUPO B
    ,['ARG', 'ARS']
    ,['MEX', 'POL']
    ,['POL', 'ARS']
    ,['ARG', 'MEX']
    ,['POL', 'ARG']
    ,['ARS', 'MEX']#GRUPO C
    ,['DIN', 'TUN']
    ,['FRA', 'AUS']
    ,['TUN', 'AUS']
    ,['FRA', 'DIN']
    ,['TUN', 'FRA']
    ,['AUS', 'DIN']#GRUPO D
    ,['ALE', 'JAP']
    ,['ESP', 'CRC']
    ,['JAP', 'CRC']
    ,['ESP', 'ALE']
    ,['JAP', 'ESP']
    ,['CRC', 'ALE']#GRUPO E
    ,['MAR', 'CRO']
    ,['BEL', 'CAN']
    ,['BEL', 'MAR']
    ,['CRO', 'CAN']
    ,['CRO', 'BEL']
    ,['CAN', 'MAR']#GRUPO F
    ,['SUI', 'CAM']
    ,['BRA', 'SER']
    ,['CAM', 'SER']
    ,['BRA', 'SUI']
    ,['CAM', 'BRA']
    ,['SER', 'SUI']#GRUPO G
    ,['URU', 'COR']
    ,['POR', 'GAN']
    ,['COR', 'GAN']
    ,['POR', 'URU']
    ,['COR', 'POR']
    ,['GAN', 'URU']#GRUPO H
    ,['HOL', 'EUA']
    ,['ARG', 'AUS']
    ,['JAP', 'CRO']
    ,['BRA', 'COR']
    ,['ING', 'SEN']
    ,['FRA', 'POL']
    ,['MAR', 'ESP']
    ,['POR', 'SUI']# oitavas
    ,['HOL', 'ARG']
    ,['CRO', 'BRA']
    ,['ING', 'FRA']
    ,['MAR', 'POR']#quartas
    ,['ARG', 'CRO']
    ,['FRA', 'MAR']#semifinais
    ,['CRO', 'MAR']#terceiro_lugar
    ,['ARG', 'FRA']#final
]

results_2022 = [
     [0, 2, segundo, fase_de_grupos]  # [jogo[gols_t1, gols_t2, vencedor, fase]
    ,[0, 2, segundo, fase_de_grupos]
    ,[1, 3, segundo, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]
    ,[1, 2, segundo, fase_de_grupos]#grupo A
    ,[6, 2, primeiro, fase_de_grupos]  
    ,[1, 1, empate, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[0, 3, segundo, fase_de_grupos] #grupo B
    ,[1, 2, segundo, fase_de_grupos]  
    ,[0, 0, empate, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]  
    ,[1, 2, segundo, fase_de_grupos]#grupo C
    ,[0, 0, empate, fase_de_grupos]  
    ,[4, 1, primeiro, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]  
    ,[1, 0, primeiro, fase_de_grupos]#grupo D
    ,[1, 2, segundo, fase_de_grupos]  
    ,[7, 0, primeiro, fase_de_grupos]
    ,[0, 1, segundo, fase_de_grupos]
    ,[1, 1, empate, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]  
    ,[2, 4, segundo, fase_de_grupos]#grupo E
    ,[0, 0, empate, fase_de_grupos]  
    ,[1, 0, primeiro, fase_de_grupos]
    ,[0, 2, segundo, fase_de_grupos]
    ,[4, 1, primeiro, fase_de_grupos]
    ,[0, 0, empate, fase_de_grupos]  
    ,[1, 2, segundo, fase_de_grupos]#grupo F
    ,[1, 0, primeiro, fase_de_grupos]  
    ,[2, 0, primeiro, fase_de_grupos]
    ,[3, 3, empate, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]
    ,[1, 0, primeiro, fase_de_grupos]  
    ,[2, 3, segundo, fase_de_grupos]#grupo G
    ,[0, 0, empate, fase_de_grupos]  
    ,[3, 2, primeiro, fase_de_grupos]
    ,[2, 3, segundo, fase_de_grupos]
    ,[2, 0, primeiro, fase_de_grupos]
    ,[2, 1, primeiro, fase_de_grupos]  
    ,[0, 2, segundo, fase_de_grupos]#grupo H
    ,[3, 1, primeiro, oitavas]
    ,[2, 1, primeiro, oitavas]
    ,[1, 1, segundo, oitavas]
    ,[4, 1, primeiro, oitavas]
    ,[3, 0, primeiro, oitavas]
    ,[3, 1, primeiro, oitavas]
    ,[0, 0, primeiro, oitavas]
    ,[6, 1, primeiro, oitavas]#oitavas
    ,[2, 2, segundo, quartas]
    ,[1, 1, primeiro, quartas]
    ,[1, 2, segundo, quartas]
    ,[1, 0, primeiro, quartas]#quartas
    ,[3, 0, primeiro, semifinais]
    ,[2, 0, primeiro, semifinais]#semifinais
    ,[2, 1, primeiro, terceiro_lugar]#terceiro_lugar
    ,[3, 3, primeiro, final]#final
]

teams_2010 = unique_teams(plays_2010)
teams_2014 = unique_teams(plays_2014)
teams_2018 = unique_teams(plays_2018)
teams_2022 = unique_teams(plays_2022)

all_teams = teams_2010.union(teams_2014, teams_2018, teams_2022)
all_plays = plays_2010 + plays_2014 + plays_2018 + plays_2022
all_results = results_2010 + results_2014 + results_2018 + results_2022


def generate_teams_ref():
    teams_dictionary = {}
    count = 0
    for team in all_teams:
        teams_dictionary[team] = count
        count += 1

    return teams_dictionary

if __name__ == "__main__":
    print(generate_teams_ref())



