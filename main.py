from correlation import dataRead

path = "C:/Users/Can/Desktop/myHugeProject/data/"
file_names = [
    "AEX Futures Historical Data.csv",
    "AUD_USD Historical Data.csv",
    "Australia 10-Year Bond Yield Historical Data.csv",
    "Bank NIFTY Futures Historical Data.csv",
    "Brazil 10-Year Bond Yield Historical Data.csv",
    "Brent Oil Futures Historical Data.csv",
    "BTC_USD Bitfinex Historical Data.csv",
    "CAC 40 Futures Historical Data.csv",
    "Canada 10-Year Bond Yield Historical Data.csv",
    "China A50 Futures Historical Data.csv",
    "China H-Shares Futures Historical Data.csv",
    "Copper Futures Historical Data.csv",
    "Crude Oil WTI Futures Historical Data.csv",
    "CSI 300 Futures Historical Data.csv",
    "DAX Futures Historical Data.csv",
    "Dow Jones Futures Historical Data.csv",
    "EUR_GBP Historical Data.csv",
    "EUR_JPY Historical Data.csv",
    "EUR_USD Historical Data.csv",
    "Euro Stoxx 50 Futures Historical Data.csv",
    "France 10-Year Bond Yield Historical Data.csv",
    "FTSE 100 Futures Historical Data.csv",
    "FTSE MIB Futures Historical Data.csv",
    "GBP_JPY Historical Data.csv",
    "GBP_USD Historical Data.csv",
    "Germany 10-Year Bond Yield Historical Data.csv",
    "Gold Futures Historical Data.csv",
    "Hang Seng Futures Historical Data.csv",
    "Heating Oil Futures Historical Data.csv",
    "Hong Kong 10-Year Bond Yield Historical Data.csv",
    "IBEX 35 Futures Historical Data.csv",
    "iBovespa Futures Historical Data.csv",
    "Italy 10-Year Bond Yield Historical Data.csv",
    "Japan 10-Year Bond Yield Historical Data.csv",
    "KOSPI 200 Futures Historical Data.csv",
    "London Sugar Futures Historical Data.csv",
    "Nasdaq 100 Futures Historical Data.csv",
    "Natural Gas Futures Historical Data.csv",
    "Nifty 50 Futures Historical Data.csv",
    "Nikkei 225 Futures Historical Data.csv",
    "NZD_USD Historical Data.csv",
    "Platinum Futures Historical Data.csv",
    "RTS Futures Historical Data.csv",
    "Russell 2000 Futures Historical Data.csv",
    "S&P 500 Futures Historical Data.csv",
    "S&P_ASX 200 Futures Historical Data.csv",
    "SGX FTSE Taiwan F Futures Historical Data.csv",
    "Silver Futures Historical Data.csv",
    "Singapore MSCI Futures Historical Data.csv",
    "SMI Futures Historical Data.csv",
    "South Africa 40 Futures Historical Data.csv",
    "Spain 10-Year Bond Yield Historical Data.csv",
    "TecDAX Futures Historical Data.csv",
    "TOPIX Futures Historical Data.csv",
    "United Kingdom 10-Year Bond Yield Historical Data.csv",
    "United States 2-Year Bond Yield Historical Data.csv",
    "United States 5-Year Bond Yield Historical Data.csv",
    "United States 10-Year Bond Yield Historical Data.csv",
    "United States 30-Year Bond Yield Historical Data.csv",
    "US Coffee C Futures Historical Data.csv",
    "US Corn Futures Historical Data.csv",
    "US Cotton #2 Futures Historical Data.csv",
    "US Wheat Futures Historical Data.csv",
    "USD_CAD Historical Data.csv",
    "USD_CHF Historical Data.csv",
    "USD_JPY Historical Data.csv",
    "WIG20 Futures Historical Data.csv"
]


correlation_related = {
    "positive":[],
    "negative":[]
}
correlation_notrelated = {
    "positive":[],
    "negative":[]
}

for file_name in file_names:
    try:
        l1 = dataRead(path,file_name)
        a = l1.mergedFunc(l1.DF)
        a["Price_x"] = a["Price_x"].apply(l1.remove_comma_and_convert)
        print(file_name)
        print("Normality Test", l1.normalityTest(a))
        print("Correlation", l1.correlation(a)[1])
        if l1.correlation(a)[1] < 0.05 and l1.correlation(a)[0]>0:
            correlation_related["positive"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))
        elif l1.correlation(a)[1] < 0.05 and l1.correlation(a)[0]<0:
            correlation_related["negative"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))
            
    except ValueError:
        l1 = dataRead(path,file_name)
        a = l1.mergedFunc(l1.DF)
        a["Price_x"] = a["Price_x"].apply(l1.remove_comma_and_convert)
        a["Price_y"] = a["Price_y"].apply(l1.remove_comma_and_convert)
        print(file_name)
        print("Normality Test", l1.normalityTest(a))
        print("Correlation", l1.correlation(a)[1])
        if l1.correlation(a)[1] > 0.05 and l1.correlation(a)[0] >0:
            correlation_notrelated["positive"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))
        elif l1.correlation(a)[1] > 0.05 and l1.correlation(a)[0] <0:
            correlation_notrelated["negative"].append((file_name, l1.correlation(a)[0], l1.correlation(a)[1]))


print("related positive:", correlation_related["positive"])
print("related negative:", correlation_related["negative"])

print("not related", correlation_notrelated["positive"])
print("not related", correlation_notrelated["negative"])


