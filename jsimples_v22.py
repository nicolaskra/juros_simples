# Importando os
import os    
import sys 
# Remodelando a calculadora de juros simples
def menu():
    while True:
        print('Escolha a opção de operação a realizar:')
        print('1. Calcular o valor do juros')
        print('2. Calcular o capital inicial')
        print('3. Calcular o período da operação')
        print('4. Sair do menu')

        escolha = input('Escolha a opção (1,2,3,4): ')
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha == 1:
                calc_juros()
            elif escolha == 2:
                calc_cinicial()
            elif escolha == 3:
                calc_periodo()
            elif escolha == 4:
                sair()
            else:
                print('Por favor, insira um número válido.')


def calc_juros(): 
        
                    # Inputs: Valor incial , período em meses , taxa em decimal 
                    inicial = float(input(f'Insira o valor inicial: '))
                    periodo = int(input(f'Insira o período em meses: '))
                    taxa = float(input(f'Insira o valor da taxa em decimal: '))
            
                    
                    # Aplicando os cálculos
                    taxa_mensal = taxa / 100
                    juros = (inicial*periodo*taxa_mensal)
                    montante = inicial+juros
                    parcela  = montante/periodo
                    taxa_total = taxa * periodo 
            
                    
                    print('-'* 45)
                    # Pritando a escolha
                    print(f'\nVamos calcular os juros!\n')
                    
                    
                    # Personalizando a saida
                    # Outputs: Valor total juros, montante, valor da parcela , percentual % da operação
                    print(f'\nO valor total de juros é de R${juros:.2f} ')
                    
                    print(f'\nO montante será de R${montante:.2f} ')
                    
                    print(f'\nO valor da parcela será de R${parcela:.2f} ')
                    

                    print(f'\nO percentual total será de {taxa_total:.2f}%\n ')
                
                    print('-'* 45)


def calc_cinicial():
            
                    # Inputs: Valor total do juros , período em meses e taxa em decimal
                    juros = float(input(f'Insira o valor do juros: '))
                    periodo = int(input(f'Insira o período em meses: '))
                    taxa = float(input(f'Insira o valor da taxa em decimal: '))

                   
                         
                    # Convertendo a taxa 
                    taxa_decimal = taxa / 100
            
                    # Efetuando os cálculos
                    capital_inicial = juros/periodo/taxa
                    taxa_total = taxa * periodo * 100
                    taxa_mensal = taxa_total / periodo
                    montante = capital_inicial + juros
                    parcela = montante / periodo
            


                    print('-'* 45)   
                    # Pritando a escolha
                    print(f'\nVamos calcular o valor inicial\n')  
                    
                    
                    #  Personalizando os resultados
                    #  Outputs: Capital inicial, montante , parcela e percentual total
                    print(f'\nO valor do capital inicial é de R${capital_inicial:.2f} ')
                    
                    print(f'\nO montante será de R${montante:.2f} ')
                    
                    print(f'\nO valor da parcela será de R${parcela:.2f} ')
                    
                    print(f'\nO percentual total será de {taxa_total:.2f}%\n ')

                    print('-'* 45)



def calc_periodo():
                    # Solicitando os inputs
                    # Capital inicial, Valor do Juros , Taxa de juros em Decimal
                    capital_inicial = float(input(f' Insira o valor do capital inicial: '))
                    juros = float(input(f' Insira o valor do juros: '))
                    taxa = float(input(f' Insira o valor da taxa em decimal: '))

                    
                    # Convertendo a taxa
                    taxa_decimal = taxa / 100
                    # Aplicando os cálculos   
                    montante = capital_inicial + juros
                    periodo = juros / (capital_inicial * taxa_decimal)
                    taxa_total = taxa * periodo
                    parcela = montante / periodo
                    
                   
                   
                    
                    print('-'* 45)                   
                    # Pritando a escolha
                    print(f'\nVamos calcular o período')     
                    # Outputs: Periodo, capital inicial , montante , parcela e percentual total
                    print(f'\nO periodo da operação será de {periodo:.0f} meses')
                    
                    print(f'\nO valor do capital inicial é de R${capital_inicial:.2f} ')
                    
                    print(f'\nO montante será de R${montante:.2f} ')
                   
                    print(f'\nO valor da parcela será de R${parcela:.2f} ')
                    
                    print(f'\nO percentual total será de {taxa_total:.2f}%\n ')  
            
                    print('-'* 45)



def sair():
    # Utilizando os para limpar o terminal  
    os.system('cls')
    
    print(f'\nSaindo do programa....')


menu() 




                