import numpy as np
import pandas as pd
from getRegVector import getRegVector

data = pd.read_csv('dados_1.csv')
data = data.to_numpy()
y = data[:, 0]  # Dados de entrada do sistema.
u = data[:, 1]
N = len(y)
Ordem = 3  # int(input('Ordem do sistema: '))
P = 1000 * np.identity(Ordem * 2)
teta = np.zeros([Ordem*2, 1], dtype=int)
erro = 0
l = 0.97  # Fator de esquecimento constante (entre 0.9 e 1).


for t in range(Ordem, N):
    fi = getRegVector(Ordem, y, u, True, 0, t)
    fi_t = fi.transpose()
    erro = (y[t] - np.dot(fi_t, teta))  # Erro de estimação
    K = (np.dot(P, fi) / (l + np.dot(np.dot(fi_t, P), fi)))  #Ganho do estimador
    teta = teta + (K * erro)  # Vetor de parâmetros
    P = ((1 / l) * (P - np.dot(K, (np.dot(P, fi)).transpose())))  # Matriz de covariância
print(teta)
