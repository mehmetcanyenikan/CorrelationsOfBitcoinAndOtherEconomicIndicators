import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro 
from scipy import stats


class dataRead:
    def __init__(self,path,file):
        self.path = path
        self.file = file
        self.bitcoinDF = pd.read_csv("C:/Users/Can/Desktop/myHugeProject/data/BTC_USD Bitfinex Historical Data.csv")
    @property
    def DF(self):
        self.x = pd.read_csv(self.path+self.file)
        return self.x
    @DF.setter
    def DF(self,files):
        self.files = files
    
    def mergedFunc(self,x):
        self.merged_df = pd.merge(self.bitcoinDF, self.x, on='Date')
        return self.merged_df

    def remove_comma_and_convert(self,value):
        value = value.replace(',', '')
        return float(value)
    
    def normalityTest(self,k):
        return shapiro(k["Price_y"]).pvalue

    def correlation(self,k):
        correlation, p_value = stats.spearmanr(k["Price_x"], k["Price_y"])
        return correlation,p_value
        # return stats.spearmanr(k["Price_y"], k["Price_x"]).pvalue