import seaborn as sns
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



class Graphs:
    @staticmethod
    def _setup_ax(ax, figsize=(10, 6)):
        """Método auxiliar para gerenciar a criação de figuras."""
        if ax is None:
            plt.figure(figsize=figsize)
            return plt.gca()
        return ax

    @staticmethod
    def scatter(df, x, y, ax=None, title=None, xlabel=None, ylabel=None):
        ax = Graphs._setup_ax(ax)
        sns.scatterplot(data=df, x=x, y=y, alpha=0.3, ax=ax)
        ax.set_title(title or f"{x} vs {y}")
        ax.set_xlabel(xlabel or x)
        ax.set_ylabel(ylabel or y)
        return ax

    @staticmethod
    def scatter_with_trend(df, x, y, ax=None, title=None):
        ax = Graphs._setup_ax(ax)
        # x_bins=50 divide os 10 milhões de pontos em 50 colunas verticais
        # e desenha apenas a média e o intervalo de confiança de cada coluna.
        sns.regplot(
            data=df, x=x, y=y, ax=ax,
            x_bins=50, 
            scatter_kws={'edgecolor': 'white'},
            line_kws={'color': 'red'}
        )
        return ax

    @staticmethod
    def histogram(df, column, ax=None, title=None, xlabel=None):
        ax = Graphs._setup_ax(ax)
        sns.histplot(data=df, x=column, kde=True, ax=ax)
        ax.set_title(title or f"Distribuição de {column}")
        ax.set_xlabel(xlabel or column)
        return ax

    @staticmethod
    def boxplot(df, column, group_by=None, ax=None, title=None, ylabel=None):
        ax = Graphs._setup_ax(ax)
        sns.boxplot(data=df, x=group_by, y=column, ax=ax)
        ax.set_title(title or f"Boxplot de {column}")
        ax.set_ylabel(ylabel or column)
        return ax

    @staticmethod
    def bar_count(df, column, ax=None, title=None, xlabel=None):
        ax = Graphs._setup_ax(ax)
        sns.countplot(data=df, x=column, ax=ax)
        ax.set_title(title or f"Contagem de {column}")
        ax.set_xlabel(xlabel or column)
        return ax

    @staticmethod
    def group_mean_line(df, group_col, target_col, ax=None, title=None):
        ax = Graphs._setup_ax(ax)
        grouped = df.groupby(group_col)[target_col].mean().reset_index()
        sns.lineplot(data=grouped, x=group_col, y=target_col, ax=ax, marker='o')
        ax.set_title(title or f"Média de {target_col} por {group_col}")
        return ax

    @staticmethod
    def correlation(df, ax=None, title="Matriz de Correlação"):
        ax = Graphs._setup_ax(ax, figsize=(10, 8))
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        ax.set_title(title)
        return ax

    @staticmethod
    def super_show(df, plot_configs, cols=2):
        """
        Gera um painel com múltiplos gráficos.
        plot_configs: Lista de tuplas (metodo, dicionario_de_parametros)
        """
        n_plots = len(plot_configs)
        rows = (n_plots + cols - 1) // cols
        
        fig, axes = plt.subplots(rows, cols, figsize=(cols * 7, rows * 6))
        axes = axes.flatten() if n_plots > 1 else [axes]

        for i, (method, params) in enumerate(plot_configs):
            method(df, ax=axes[i], **params)

        # Remove eixos extras se houver
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()
class Cols:
    AGE = "age"
    GENDER = "gender"
    INCOME = "income"
    DAILY_GAMING_HOURS = "daily_gaming_hours"
    WEEKLY_SESSIONS = "weekly_sessions"
    YEARS_GAMING = "years_gaming"
    SLEEP_HOURS = "sleep_hours"
    CAFFEINE_INTAKE = "caffeine_intake"
    EXERCISE_HOURS = "exercise_hours"
    STRESS_LEVEL = "stress_level"
    ANXIETY_SCORE = "anxiety_score"
    DEPRESSION_SCORE = "depression_score"
    SOCIAL_INTERACTION_SCORE = "social_interaction_score"
    RELATIONSHIP_SATISFACTION = "relationship_satisfaction"
    ACADEMIC_PERFORMANCE = "academic_performance"
    WORK_PRODUCTIVITY = "work_productivity"
    ADDICTION_LEVEL = "addiction_level"
    MULTIPLAYER_RATIO = "multiplayer_ratio"
    TOXIC_EXPOSURE = "toxic_exposure"
    VIOLENT_GAMES_RATIO = "violent_games_ratio"
    MOBILE_GAMING_RATIO = "mobile_gaming_ratio"
    NIGHT_GAMING_RATIO = "night_gaming_ratio"
    WEEKEND_GAMING_HOURS = "weekend_gaming_hours"
    FRIENDS_GAMING_COUNT = "friends_gaming_count"
    ONLINE_FRIENDS = "online_friends"
    STREAMING_HOURS = "streaming_hours"
    ESPORTS_INTEREST = "esports_interest"
    HEADSET_USAGE = "headset_usage"
    MICROTRANSACTIONS_SPENDING = "microtransactions_spending"
    PARENTAL_SUPERVISION = "parental_supervision"
    LONELINESS_SCORE = "loneliness_score"
    AGGRESSION_SCORE = "aggression_score"
    HAPPINESS_SCORE = "happiness_score"
    BMI = "bmi"
    SCREEN_TIME_TOTAL = "screen_time_total"
    EYE_STRAIN_SCORE = "eye_strain_score"
    BACK_PAIN_SCORE = "back_pain_score"
    COMPETITIVE_RANK = "competitive_rank"
    INTERNET_QUALITY = "internet_quality"