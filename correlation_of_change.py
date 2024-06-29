from regularization import merged
from scipy.stats import shapiro
from scipy import stats


class correlation_of_change(merged):
    def __init__(self, file_path, file_name):
        super().__init__(file_path, file_name)

    def change(self):
        return self.remove_comma_and_convert(self.merged_func)['Price_y'].pct_change(), self.remove_comma_and_convert(self.merged_func)['Price_x'].pct_change()

    def normality_test(self):
        return shapiro(self.remove_comma_and_convert(self.merged_func)['Price_y'].pct_change()).pvalue

    def correlation(self, k):
        correlation, p_value = stats.spearmanr(k["Price_x"], k["Price_y"])
        return correlation, p_value
