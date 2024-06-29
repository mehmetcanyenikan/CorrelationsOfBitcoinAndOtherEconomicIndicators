import os
import glob
from data_read import data_read
import pandas as pd
from regularization import merged
from correlation_of_change import correlation_of_change


def main():
    path = '/home/can/Desktop/GaussCloud/data/'
    csv_files = glob.glob(os.path.join(path, '*.csv'))
    csv_file_names = [os.path.basename(file) for file in csv_files]

    for csv_file_name in csv_file_names:
        l2 = correlation_of_change(path, csv_file_name)
        print(l2.correlation())


if __name__ == "__main__":
    main()
