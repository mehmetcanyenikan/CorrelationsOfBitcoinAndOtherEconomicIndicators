from regularization import merged
from scipy.stats import shapiro
from scipy import stats


class correlation_of_change(merged):
    def __init__(self, file_path, file_name):
        super().__init__(file_path, file_name)

    @property
    def change(self):
        self.A = self.remove_comma_and_convert(self.merged_func)['Price_y'].pct_change()
        self.B = self.remove_comma_and_convert(self.merged_func)['Price_x'].pct_change()
        return self.A, self.B

    def normality_test(self, a):
        return shapiro(a).pvalue

    def correlation_not_normal_dist(self, a, b):
        correlation_not, p_value_not = stats.spearmanr(a, b)
        return correlation_not, p_value_not

    def correlation_normal_dist(self, a, b):
        correlation, p_value = stats.pearsonr(a, b)
        return correlation, p_value

