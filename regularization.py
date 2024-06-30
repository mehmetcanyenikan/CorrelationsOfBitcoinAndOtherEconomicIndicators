from data_read import data_read
import pandas as pd


class merged(data_read):
    def __init__(self, file_path, file_name):
        super().__init__(file_path, file_name)
        self.bitcoin_df = pd.read_csv(file_path+'Bitcoin Historical Data.csv')

    @property
    def merged_func(self):
        self.merged_df = pd.merge(self.bitcoin_df, self.read_csv, on='Date')
        return self.merged_df

    def remove_comma_and_convert(self, value):
        value['Price_x'] = value['Price_x'].astype(str).str.replace(',', '')
        value['Price_x'] = value['Price_x'].astype(float)

        value['Price_y'] = value['Price_y'].astype(str).str.replace(',', '')
        value['Price_y'] = value['Price_y'].astype(float)
        return (value)
