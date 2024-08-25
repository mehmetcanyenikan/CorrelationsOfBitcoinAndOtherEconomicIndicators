import pandas as pd

class Merged:
    def __init__(self, df, df_btc) -> pd.DataFrame:
        self.df = df
        self.df_btc = df_btc

    @property
    def merged_func(self):
        self.merged_df = pd.merge(self.df_btc, self.df, on='Date')
        return self.merged_df

class CommaConvert:
    def __init__(self, df) -> None:
        self.df = df

    def remove_comma_and_convert(self):
        self.df['Price_x'] = self.df['Price_x'].astype(str).str.replace(',', '')
        self.df['Price_x'] = self.df['Price_x'].astype(float)

        self.df['Price_y'] = self.df['Price_y'].astype(str).str.replace(',', '')
        self.df['Price_y'] = self.df['Price_y'].astype(float)
        return self.df
