import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model as sk
import pandas as pd
from _aux import Graphs as gr
from _aux import Cols as C
arq = "gaming_mental_health_10M_40features.csv"

def main():
    data = import_data()
    gr.boxplot(group_by(data, C.ADDICTION_LEVEL, True), C.AGE, "Idade por Nível de Vício", "Idade")

def group_by(df, column,numeric=True):
    df = df.groupby(column).mean(numeric_only=numeric).reset_index()
    return df

def import_data():
    data = pd.read_csv(arq)
    return data


if __name__ == "__main__":
    main()