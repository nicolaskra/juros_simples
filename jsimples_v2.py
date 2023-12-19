# Importando os
import os    


# Remodelando a calculadora de juros simples
def menu():
    while True:
                print(f'Escolha a opção de operação a relizar')
                print(f'1.Calcular o valor do juros')
                print(f'2.Calcular o capital inicial')
                print(f'3.Calcular o período da operação')
                print(f'4.Sair do menu')
                escolha = int(input('Escolha a opção 1,2,3,4 : '))
                # Determinando os parametros para aplicar a calculadora
                if escolha == 1:
                        calc_juros()
                elif escolha == 2:
                        calc_cinicial()    
                elif escolha == 3:
                        calc_periodo()
                elif escolha == 4:   
                        sair()
                        
                else:
                        print('Por favor insira um número válido')
                
                        print(escolha)
def calc_juros():
       
                # Inputs: Valor incial , período em meses , taxa em decimal 
                inicial = float(input(f'Insira o valor inicial: '))
                periodo = int(input(f'Insira o período em meses: '))
                taxa = float(input(f'Insira o valor da taxa em decimal: '))
        
                # Pritando a escolha
                print('escolha')
                # Aplicando os cálculos
                taxa_mensal = taxa / 100
                juros = (inicial*periodo*taxa_mensal)
                montante = inicial+juros
                parcela  = montante/periodo
                taxa_total = taxa * periodo 
        
                # Personalizando a saida
                # Outputs: Valor total juros, montante, valor da parcela , percentual % da operação
                print(f'O valor total de juros é de R${juros:.2f} ')
                print(f'O montante será de R${montante:.2f} ')
                print(f'O valor da parcela será de R${parcela:.2f} ')
                print(f'O percentual total será de {taxa_total:.2f}% ')
             

def calc_cinicial():
        
                # Inputs: Valor total do juros , período em meses e taxa em decimal
                juros = float(input(f'Insira o valor do juros: '))
                periodo = int(input(f'Insira o período em meses: '))
                taxa = float(input(f'Insira o valor da taxa em decimal: '))

                # Pritando a escolha
                print('escolha')        
                # Convertendo a taxa 
                taxa_decimal = taxa / 100
        
                # Efetuando os cálculos
                capital_inicial = juros/periodo/taxa
                taxa_total = taxa * periodo 
                taxa_mensal = taxa_total / periodo
                montante = capital_inicial + juros
                parcela = montante / periodo
        
                #  Personalizando os resultados
                print(f'O valor do capital inicial é de R${capital_inicial:.2f} ')
                print(f'O montante será de R${montante:.2f} ')
                print(f'O valor da parcela será de R${parcela:.2f} ')
                print(f'O percentual total será de {taxa_total:.2f}% ')

def calc_periodo():
                # Solicitando os inputs
                # Capital inicial, Valor do Juros , Taxa de juros em Decimal
                capital_inicial = float(input(f' Insira o valor do capital inicial: '))
                juros = float(input(f' Insira o valor do juros: '))
                taxa = float(input(f' Insira o valor da taxa em decimal: '))

                # Pritando a escolha
                print('escolha')  
                # Convertendo a taxa
                taxa_decimal = taxa / 100
                # Aplicando os cálculos   
                montante = capital_inicial + juros
                periodo = juros / (capital_inicial * taxa_decimal)
                taxa_total = taxa_decimal * periodo
                parcela = montante / periodo
                
                print(f'O periodo da operação será de {periodo:.2f} meses')
                print(f'O valor do capital inicial é de R${capital_inicial:.2f} ')
                print(f'O montante será de R${montante:.2f} ')
                print(f'O valor da parcela será de R${parcela:.2f} ')
                print(f'O percentual total será de {taxa_total:.2f}% ')  
        
 def sair():
        # Utilizando os para limpar o terminal  
                os.system('cls')
                print(f'Saindo do programa....')
        

menu()
