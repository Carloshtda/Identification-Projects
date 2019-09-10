%Estimador dos minimos quadrados recursivo com Fator de Esquecimento
%Derivado do mmq recursivo do livro Identificação de Sistemas Dinâmicos
%Lineares - Antônio Coelho e Leandro Coelho
clear; clc; close all;
%%
data = load('dados_1.txt');
u = data(:,2); %Dados de entrada do sistema
y = data(:,1);
N = length(y);
Ordem = input('Ordem do sistema? ');
P = 1000*eye(Ordem*2); teta = zeros(1, Ordem*2)';
%tetas = [teta];
erro = zeros(1, N);
lambda = 0.97; %Fator de esquecimento cte(entre 0.9 e 1).
%%
for t=Ordem+1:N
    fi = getRegVector(Ordem, y, u, true, 0, t);
    erro(t) = y(t) - (fi'*teta);    %Erro de estimação
    K = P*fi/(lambda + fi'*P*fi);        %Ganho do estimador
    teta = teta + K*erro(t);        %Vetor de parâmetros
    P =  (1/lambda)*(P - K*(P*fi)');           % Matriz de covariância
end
disp(teta);