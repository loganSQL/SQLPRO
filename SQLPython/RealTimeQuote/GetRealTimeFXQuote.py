# Python program to get the real-time Financial Data by using Alpha Vantage API
# https://www.alphavantage.co/documentation/ 
# https://www.geeksforgeeks.org/python-get-the-real-time-currency-exchange-rate/
  

# Python program to get the real-time 
# currency exchange rate 
  
# Function to get real time currency exchange  
def GetRealTimeFXQuote(from_currency, to_currency, api_key) : 
  
    # importing required libraries 
    import requests, json 
  
    # base_url variable store base url  
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
  
    # main_url variable store complete url 
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key 
  
    # get method of requests module  
    # return response object  
    req_ob = requests.get(main_url) 
  
    # json method return json format 
    # data into python dictionary data type. 
      
    # result contains list of nested dictionaries 
    result = req_ob.json() 
  
    print(" Result before parsing the json data :\n", result) 
  
      
    print("\n After parsing : \n Realtime Currency Exchange Rate for", 
          result["Realtime Currency Exchange Rate"] 
                ["2. From_Currency Name"], "TO", 
          result["Realtime Currency Exchange Rate"] 
                ["4. To_Currency Name"], "is", 
          result["Realtime Currency Exchange Rate"] 
                ['5. Exchange Rate'], to_currency) 
  
  
  
# Driver code 
if __name__ == "__main__" : 
  
    # currency code 
    from_currency = "USD"
    to_currency = "CAD"
  
    # enter your api key here  
    #api_key = "YourSecretKey"
  
    # function calling USD to CAD
    GetRealTimeFXQuote(from_currency, to_currency, api_key) 
    # function calling CAD to USD
    GetRealTimeFXQuote(to_currency, from_currency, api_key) 