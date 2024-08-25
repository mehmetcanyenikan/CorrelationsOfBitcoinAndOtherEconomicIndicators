import pandas as pd
from file_reader import ReadFolderCsvFiles
from data_processing import Merged, CommaConvert
from correlations import SpearmanCorrelation

def main():

    FOLDER_PATH = '/home/can/Desktop/SW/GaussianCloud/exchange_correlation/CorrelationOfBitcoinAndOtherEconomicIndicators/data'
    bitcoin_df = pd.read_csv(FOLDER_PATH+'/S&P 500 Futures Historical Data.csv')

    for csv_file_name in ReadFolderCsvFiles(path=FOLDER_PATH).read:
        df = pd.read_csv(FOLDER_PATH + '/' + csv_file_name)
        merged_df = Merged(df, bitcoin_df).merged_func
        comma_convert = CommaConvert(merged_df).remove_comma_and_convert()
        correlation_result = SpearmanCorrelation(comma_convert['Price_x'], comma_convert['Price_y']).correlation()
        print(correlation_result)


        # I will add different time series correlations to the code :)

if __name__ == '__main__':
    main()