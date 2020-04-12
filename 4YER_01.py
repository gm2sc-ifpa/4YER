# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:47:27 2019

@authors Professors: 
        Dr. Denis C. L. Costa
        MSc. Lair A. de Meneses
        
@authors Students:
        Heictor Alves de Oliveira Costa
        Lucas Pompeu Neves
        Brennus Caio Carvalho da Cruz
        Júlio Leite Azancort Neto

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
       Análise de Sinais utilizando o Método de Fourier
       
Disponível em:
    
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-COMPUTATIONAL-ENVIRONMENT/blob/master/SENGI_2020/Fourier_01.py
    
"""
print('')
print('============= Início do Programa 4YER_01 ============')
print('')
# Importando Bibliotecas
# Biblioteca numpy: Matemática de alto Nível

# import numpy as np

# Biblioteca matplot: Plotagem em 2D
# import matplotlib.pyplot as plt

# Biblioteca sympy: Matemática Simbólica
import sympy as sy
import numpy as np

##########################################################
print('=====================================================')
# Variáveis de Controle

T0 = 0.0               # Instante Inicial

T1 = 10                # Instante Final

T = T1 - T0            # Período Fundamenta

w = 2*sy.pi/T          # Frequência Angular


t = np.linspace(T0,T1,100)

lista = []

n = int(input('>>> Entre com o número do harmônico n --> ')  ) 
# Número de Harmônicos
print('')
print('Número de Harmônicos >>>', n)
print('====================================================')
S0 = 0
for i in range(1, n + 1):
    
    n = i
    ##########################################################
    # Declarando a variável simbólica
    t = sy.symbols('t')

    # Declarando a Função - Sinal
    def f(t):
        return 10*t-t**2
      
    # Declarando a amplitude Real do Sinal
    def a0(t):
        return (2/T)*sy.integrate(f(t), (t, T0, T1))
    print('a0 =', a0(t))

    # Declarando a amplitude Real do Sinal
    def an(t):
        return (2/T)*sy.integrate(f(t) * sy.cos(n * w * t), (t, T0, T1))
    print('an =', an(t))

    # Declarando a amplitude Complexa do Sinal
    def bn(t):
        return (2/T)*sy.integrate(f(t) * sy.sin(n * w * t), (t, T0, T1))
    print('bn =', bn(t))
    #print('=================================================')

    ##########################################################
    # Compondo a Função Resposta do Sinal
    def Fn(t):
        return an(t) * sy.cos(n * w * t) + bn(t) * sy.sin(n * w * t)
    
    lista.append(Fn(t))
    
    print('Fn(t) é o Somatório no n-ésimo Harmônico')
    
    print("Função para {} harmônico(s):".format(i), Fn(t))
    
    S0 = S0 + Fn(t)

    print('F(n) é o Valor do Sinal no n-ésimo Harmômico')
    print('')
    print('F(n) = Σ[an.cos(nwt) + bn.sen(nwt)]')
    print('')
    print('==================================================')
    print('Para n = ', n, '--> F(n) =', Fn(t))
    print('')
print("S =", 0.5*a0(t) + S0)

##########################################################
print(' ')
print('============== Fim do Programa 4YER_01 =============')





