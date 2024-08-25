from abc import ABC, abstractmethod
from scipy import stats
import pandas as pd

class Correlation(ABC):
    def __init__(self, df, df_btc):
        self.df = df 
        self.df_btc = df_btc

    @abstractmethod
    def correlation(self):
        pass

class SpearmanCorrelation(Correlation):
    def correlation(self):
        correlation_not, p_value_not = stats.spearmanr(self.df, self.df_btc)
        return correlation_not, p_value_not
