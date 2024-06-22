import pandas as pd
from scipy.stats import shapiro
from scipy import stats
from statsmodels.tsa.stattools import adfuller


class data_read:

    def __init__(self, path, file):
        self.path = path
        self.file = file
        self.bitcoin_df = pd.read_csv("C:/Users/Can/Desktop/CorrelationOfBitcoinAndOtherEconomicIndicators/data/Bitcoin Historical Data.csv")
        self.other_df = pd.read_csv(self.path + self.file)

    @property
    def merged_func(self):
        self.merged_df = pd.merge(self.bitcoin_df, self.other_df, on='Date')
        return self.merged_df

    def remove_comma_and_convert(self, value):
        value = value.replace(',', '')
        return float(value)

    def normality_test(self, k):
        return shapiro(k["Price_y"]).pvalue

    def correlation(self, k):
        correlation, p_value = stats.spearmanr(k["Price_x"], k["Price_y"])
        return correlation, p_value

    def augmented_dickey_fuller(self, k):
        return print(adfuller(k))
