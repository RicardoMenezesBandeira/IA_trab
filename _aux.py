import seaborn as sns
import matplotlib.pyplot as plt


class Graphs:

    @staticmethod
    def scatter(df, x, y, title=None, xlabel=None, ylabel=None):
        plt.figure()
        sns.scatterplot(data=df, x=x, y=y)

        plt.title(title or f"{x} vs {y}")
        plt.xlabel(xlabel or x)
        plt.ylabel(ylabel or y)
        plt.show()

    @staticmethod
    def scatter_with_trend(df, x, y, title=None, xlabel=None, ylabel=None):
        plt.figure()
        sns.regplot(data=df, x=x, y=y)

        plt.title(title or f"{x} vs {y}")
        plt.xlabel(xlabel or x)
        plt.ylabel(ylabel or y)
        plt.show()

    @staticmethod
    def histogram(df, column, title=None, xlabel=None):
        plt.figure()
        sns.histplot(data=df, x=column, kde=True)

        plt.title(title or f"Distribuição de {column}")
        plt.xlabel(xlabel or column)
        plt.show()

    @staticmethod
    def boxplot(df, column, title=None, ylabel=None):
        plt.figure()
        sns.boxplot(data=df, y=column)

        plt.title(title or f"Boxplot de {column}")
        plt.ylabel(ylabel or column)
        plt.show()

    @staticmethod
    def bar_count(df, column, title=None, xlabel=None, ylabel="Quantidade"):
        plt.figure()
        sns.countplot(data=df, x=column)

        plt.title(title or f"Contagem de {column}")
        plt.xlabel(xlabel or column)
        plt.ylabel(ylabel)
        plt.show()

    @staticmethod
    def group_mean(df, group_col, target_col, title=None):
        grouped = df.groupby(group_col)[target_col].mean().reset_index()

        plt.figure()
        sns.lineplot(data=grouped, x=group_col, y=target_col)

        plt.title(title or f"Média de {target_col} por {group_col}")
        plt.xlabel(group_col)
        plt.ylabel(target_col)
        plt.show()

    @staticmethod
    def correlation(df, title="Matriz de Correlação"):
        plt.figure(figsize=(10, 8))
        corr = df.corr(numeric_only=True)
        sns.heatmap(corr)

        plt.title(title)
        plt.show()

    @staticmethod
    def multivariate(df, x, y, hue=None, title=None):
        plt.figure()
        sns.scatterplot(data=df, x=x, y=y, hue=hue)

        plt.title(title or f"{x} vs {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

class Cols:
    AGE = "age"
    GENDER = "gender"
    INCOME = "income"
    DAILY_GAMING = "daily_gaming_hours"
    WEEKLY_SESSIONS = "weekly_sessions"
    YEARS_GAMING = "years_gaming"
    SLEEP = "sleep_hours"
    CAFFEINE = "caffeine_intake"
    EXERCISE = "exercise_hours"
    STRESS = "stress_level"
    ANXIETY = "anxiety_score"
    DEPRESSION = "depression_score"
    SOCIAL = "social_interaction_score"
    RELATIONSHIP = "relationship_satisfaction"
    ACADEMIC = "academic_performance"
    PRODUCTIVITY = "work_productivity"
    ADDICTION = "addiction_level"
    MULTIPLAYER = "multiplayer_ratio"
    TOXIC = "toxic_exposure"
    VIOLENT = "violent_games_ratio"
    MOBILE = "mobile_gaming_ratio"
    NIGHT = "night_gaming_ratio"
    WEEKEND = "weekend_gaming_hours"
    FRIENDS_GAMING = "friends_gaming_count"
    ONLINE_FRIENDS = "online_friends"
    STREAMING = "streaming_hours"
    ESPORTS = "esports_interest"
    HEADSET = "headset_usage"
    MICROTRANSACTIONS = "microtransactions_spending"
    PARENTAL = "parental_supervision"
    LONELINESS = "loneliness_score"
    AGGRESSION = "aggression_score"
    HAPPINESS = "happiness_score"
    BMI = "bmi"
    SCREEN_TIME = "screen_time_total"
    EYE_STRAIN = "eye_strain_score"
    BACK_PAIN = "back_pain_score"
    RANK = "competitive_rank"
    INTERNET = "internet_quality"
    ADDICTION_LEVEL = "addiction_level"