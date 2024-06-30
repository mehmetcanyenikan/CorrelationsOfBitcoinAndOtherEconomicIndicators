import os
import glob
from correlation_of_change import correlation_of_change


def main():
    path = 'C:/Users/Can/Desktop/CorrelationOfBitcoinAndOtherEconomicIndicators/data/'
    csv_files = glob.glob(os.path.join(path, '*.csv'))
    csv_file_names = [os.path.basename(file) for file in csv_files]
    relations_names = []
    for csv_file_name in csv_file_names:
        l4 = correlation_of_change(path, csv_file_name)
        
        if l4.correlation_not_normal_dist(l4.change[0].iloc[1:],l4.change[1].iloc[1:])[1] <= 0.05:
            print('There is a statistically significant monotonic relationship between two variables (reject H0)')
            relations_names.append(csv_file_name)
        elif l4.correlation_not_normal_dist(l4.change[0].iloc[1:],l4.change[1].iloc[1:])[1] > 0.05:
            print('No statistically significant monotonic relationship between two variables (fail to reject H0)')
    print(relations_names)
if __name__ == "__main__":
    main()

"""
if self.normality_test(b) > 0.05:
            print("This is a Normal Distribution")
            self.correlation_normal_dist(a,b)[1]
        elif self.normality_test < 0.05:
            print("This is not a Normal Distribution")
            self.correlation_not_normal_dist(a,b)[1]
"""