import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model as sk
import pandas as pd
from _aux import Graphs as gr
from _aux import Cols as C
arq = "gaming_mental_health_10M_40features.csv"

'''
investigar as seguintes relações (exemplos, mas sinta-se livre para explorar outras):

DAILY_GAMING_HOURS ↔ DEPRESSION_SCORE (relação principal do projeto)
DAILY_GAMING_HOURS ↔ ANXIETY_SCORE
ADDICTION_LEVEL ↔ DEPRESSION_SCORE
SLEEP_HOURS ↔ DEPRESSION_SCORE (sono afeta saúde mental)

TOXIC_EXPOSURE ↔ AGGRESSION_SCORE
VIOLENT_GAMES_RATIO ↔ AGGRESSION_SCORE
NIGHT_GAMING_RATIO ↔ SLEEP_HOURS (jogo à noite = menos sono?)
MULTIPLAYER_RATIO ↔ SOCIAL_INTERACTION_SCORE

EXERCISE_HOURS ↔ DEPRESSION_SCORE (exercício melhora saúde mental?)
STRESS_LEVEL ↔ SLEEP_HOURS
LONELINESS_SCORE ↔ FRIENDS_GAMING_COUNT
SCREEN_TIME_TOTAL ↔ EYE_STRAIN_SCORE, BACK_PAIN_SCORE
'''
def main():
    plt_list = []
    data = import_data()
    data = limpar_data(data)

    #estatistica completa do dataset, para ter uma visão geral de tudo 
    # (média, mediana, moda, desvio padrão, etc.)
    print(calcular_estatisticas_completas(data))


    #divide a coluna de depressão em 20 faixas (bins) de 500 mil para facilitar a visualização e análise
    data['depression_score_binned'] = pd.cut(data['depression_score'], bins=20, labels=False)

    # 2. Agrupamento unificado (Média é o melhor para a linha de tendência)
    resumo = data.groupby('depression_score_binned').agg({
        C.SLEEP_HOURS: 'mean',
        C.DAILY_GAMING_HOURS: 'mean'
    }).reset_index()

    # 3. Preparação da lista para o super_show
    plt_list = []


    # passar a função desejada de gr e depois um dicionário com os parâmetros 
    # necessários para cada gráfico, como colunas, título, etc.

    # Gráfico 1: Sono   
    plt_list.append((gr.scatter_with_trend, {
        'x': 'depression_score_binned',
        'y': C.SLEEP_HOURS,
        'title': 'Média de Sono por Faixa de Depressão'
    }))

    # Gráfico 2: Jogo
    plt_list.append((gr.scatter_with_trend, {
        'x': 'depression_score_binned',
        'y': C.DAILY_GAMING_HOURS,
        'title': 'Média de Jogo por Faixa de Depressão'
    }))

    # 4. Exibição unificada
    #passar a base de dados tratada e a lista de gráficos 
    # para o super_show, que vai organizar tudo bonitinho
    gr.super_show(resumo, plt_list)
def group_by(df, column,numeric=True):
    df = df.groupby(column).mean(numeric_only=numeric).reset_index()
    return df
def limpar_data(df):
    # Remove as duplicatas e atualiza o DataFrame
    df = df.drop_duplicates()
    return df
def calcular_estatisticas_completas(df):
    # Selecionamos apenas as colunas numéricas para não dar erro em cálculos
    df_numerico = df.select_dtypes(include=['number'])
    
    # 1. Pegamos a base principal (média, std, min, quartis, max)
    # O .T transpõe a tabela para ficar mais fácil de ler (colunas viram linhas)
    stats = df_numerico.describe().T
    
    # 2. Adicionamos a Mediana (que é o quartil de 50%)
    # Já está no describe, mas vamos garantir que apareça com esse nome se preferir
    stats['mediana'] = df_numerico.median()
    
    # 3. Adicionamos a Moda
    # A moda pode retornar mais de um valor (empate), então pegamos o primeiro [.iloc[0]]
    stats['moda'] = df_numerico.apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    
    # 4. Adicionamos a Amplitude (Máximo - Mínimo)
    stats['amplitude'] = stats['max'] - stats['min']
    
    # 5. Adicionamos a Variância
    stats['variancia'] = df_numerico.var()

    # Reorganizando as colunas para ficar bonito
    colunas_ordenadas = [
        'count', 'mean', 'mediana', 'moda', 'std', 
        'variancia', 'min', 'max', 'amplitude', '25%', '75%'
    ]
    
    return stats[colunas_ordenadas]
def import_data():
    data = pd.read_csv(arq)
    return data


if __name__ == "__main__":
    main()