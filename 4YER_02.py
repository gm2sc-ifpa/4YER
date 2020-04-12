# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:16:47 2019

@authors Professors: 
        Dr. Denis Carlos Lima Costa
        MSc. Lair Aguiar de Meneses
        
@authors Students:
        Heictor Alves de Oliveira Costa
        Lucas Pompeu Neves
        Brennus Caio Carvalho da Cruz
        Júlio Leite Azancort Neto

Grupo de Pesquisa: 
                 Gradiente de Modelagem Matemática e
                 Simulação Computacional - GM²SC
Assunto:
    
        Representação Gráfica de Sinais utilizando o Método de Fourier
        
Disponível em:
             
    https://github.com/GM2SC/DEVELOPMENT-OF-MATHEMATICAL-METHODS-IN-COMPUTATIONAL-ENVIRONMENT/blob/master/SENGI_2020/Fourier_02.py
    
"""
print('')
print('============== Início do Programa 4YER_02 ============')
print('')
# Importando Bibliotecas
# Biblioteca numpy: Matemática de alto Nível
import numpy as np 

from numpy import *


# Biblioteca matplot: Gráficos
import matplotlib.pyplot as plt

##########################################################
# Variáveis de Controle

T0 = 0.0                      # Instante Inicial

T1 = 10                       # Instante Final

t = np.linspace(T0,T1,100)    # Intervalo de análise

# Declarando a Função - Sinal
def f(t):
    return 10*t-t**2

# Representação Algébrica do Sinal
print('S(n) = a0/2 + F(n)')
print('')
print('S(n) = a0/2 + Σ[an.cos(nwt) + bn.sen(nwt)]')
print('')

a0 = 10

# Função Ruído 

limiteinferior = 0.0
limitesuperior = 30*10**(-1)
numeropontos = 100
 
ruido = random.uniform(low=limiteinferior, high=limitesuperior, size=numeropontos)
       
# Função Sinal sem Rúido: S(t)
# Função Sinal com Rúido: S(t) + ruido

# Copiar a Série de Fourier implementada no sript --> Fourier_01

S = (-1.85185185185185*cos(6.0*pi)/pi**3 - 5.55555555555556*sin(pi/1125899906842624)/pi**2 +\
     1.85185185185185/pi**3)*sin(0.6*pi*t) - 100.0*cos(0.2*pi*t)/pi**2 - 25.0*cos(0.4*pi*t)/pi**2 +\
    (-5.55555555555556/pi**2 - 5.55555555555556*cos(6.0*pi)/pi**2 +\
     1.85185185185185*sin(pi/1125899906842624)/pi**3)*cos(0.6*pi*t) + 16.6666666666667 + ruido

print('S(n) é a representação do Spectro do Sinal no n-ésimo Harmômico')
print('')
print('Figuras 01 e 02 --> Representação Gráfica do Sinal')
print('')

# Representação Gráfica do Sinal

plt.plot(t, S, '-b', label='Série de Fourier + Ruído', linewidth = 2.0)
plt.plot(t, f(t), '-r', label='Função Geradora', linewidth = 2.0)
plt.xlabel('Tempo')
plt.ylabel('Espectro do Sinal')
plt.title('Representação da Série de Fourier')
plt.legend(loc=4) 
plt.grid(True)
plt.show() 

##########################################################

# Representação Gráfica do Sinal Colorido
import matplotlib.cm as cm


# The colormap
cmap = cm.jet

# Create figure and axes
fig = plt.figure()
fig.clf()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(t, S, c = S,s = 10, label ='Série de Fourier + Rúido', cmap=cmap, linewidth = 2.0)
plt.plot(t, f(t), '-k', label='Função Geradora', linewidth = 2.0)
plt.xlabel('Tempo')
plt.ylabel('Espectro do Sinal')
plt.legend(loc=4) 
plt.grid(True)
# plt.savefig("Series_Fourier_Color{}.png".format(n), dpi=200 )
plt.show()

##########################################################


print(' ')
print('=============== Fim do Programa 4YER_02 =============')