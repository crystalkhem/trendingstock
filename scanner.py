import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# scrape finviz
def growth_screener():
    try:
        frames = []
        for i in range(1, 105, 20):  # Pagination loop
            # Correct the URL by using f-string for pagination
            url = f"https://finviz.com/screener.ashx?v=111&f=sh_float_u10,sh_price_1to20,sh_relvol_o5,ta_perf_d10o&r={i}"
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            html = soup(webpage, "html.parser")
            
            # Parse the table
            stocks = pd.read_html(str(html))[-2]  # Get the second last table
            stocks = stocks.set_index('Ticker')  # Set ticker as index
            frames.append(stocks)  # Append to the list of frames

        # Concatenate all frames
        df = pd.concat(frames)
        df = df.drop_duplicates()  # Remove any duplicates
        df = df.drop(columns=['No.'])  # Drop the "No." column
        return df
    except Exception as e:
        return f'Error: {e}'

# Run the function
df = growth_screener()

# Check if df is a string (in case of error) or a DataFrame
if isinstance(df, str):
    print(df)
else:
    # Ensure df is not empty
    if not df.empty:
        # Full DataFrame
        print('\nGrowth Stocks Screener:')
        print(df)

        # List of Tickers
        tickers = df.index
        print('\nList of Tickers:')
        print(*tickers, sep='\n')

        tickers = pd.DataFrame(df.index)
        tickers.to_csv('tickers_only.csv', header=False, index=False) 
    else:
        print('No tickers found or the DataFrame is empty.')
