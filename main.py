# Data taken from investing.com.
import os
import glob
from correlation import data_read

path = "C:/Users/Can/Desktop/CorrelationOfBitcoinAndOtherEconomicIndicators/data/"


csv_files = glob.glob(os.path.join(path, '*.csv'))
csv_file_names = [os.path.basename(file) for file in csv_files]

# Sonuçları yazdırın
print(csv_file_names)


correlation_related = {
    "positive": [],
    "negative": []
}
correlation_notrelated = {
    "positive":[],
    "negative":[]
}

for file_name in csv_file_names:
    try:
        l1 = data_read(path, file_name)
        a = l1.merged_func
        a["Price_x"] = a["Price_x"].apply(l1.remove_comma_and_convert)
        print(a)
        print("Normality Test", l1.normality_test(a))
        print("Correlation", l1.correlation(a)[1])
        if l1.correlation(a)[1] < 0.05 and l1.correlation(a)[0] > 0:
            correlation_related["positive"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))

        elif l1.correlation(a)[1] < 0.05 and l1.correlation(a)[0] < 0:
            correlation_related["negative"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))

        elif l1.correlation(a)[1] > 0.05 and l1.correlation(a)[0] > 0:
            correlation_notrelated["positive"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))

        elif l1.correlation(a)[1] > 0.05 and l1.correlation(a)[0] < 0:
            correlation_notrelated["negative"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))

    except ValueError:
        l1 = data_read(path, file_name)
        a = l1.merged_func
        a["Price_x"] = a["Price_x"].apply(l1.remove_comma_and_convert)
        a["Price_y"] = a["Price_y"].apply(l1.remove_comma_and_convert)
        print(file_name)
        print("Normality Test", l1.normality_test(a))
        print("Correlation", l1.correlation(a)[1])
        if l1.correlation(a)[1] < 0.05 and l1.correlation(a)[0] > 0:
            correlation_related["positive"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))

        elif l1.correlation(a)[1] < 0.05 and l1.correlation(a)[0] < 0:
            correlation_related["negative"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))

        elif l1.correlation(a)[1] > 0.05 and l1.correlation(a)[0] > 0:
            correlation_notrelated["positive"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))

        elif l1.correlation(a)[1] > 0.05 and l1.correlation(a)[0] < 0:
            correlation_notrelated["negative"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))


print("related positive:", correlation_related["positive"])
print("related negative:", correlation_related["negative"])

print("not related", correlation_notrelated["positive"])
print("not related", correlation_notrelated["negative"])

# if __name__ == "__main__":