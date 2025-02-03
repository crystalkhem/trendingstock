<h2>Trending Stocks Screener</h2>
A Python script that scrapes Finviz for high-growth stocks based on specific screening criteria and exports the ticker symbols to a CSV file.

Productivity script to scan for daily trending high volatilty stocks of at least 10% change, 5x relative volume, small cap stock (20M). These stocks narrow down big movers and extremely liquid movers for the day. Results are printed and exported as a CSV to allow for easy WeBull watchlist drop or generally import. Utilizes FinViz's API.

<h3>Features</h3>
<li>Float under 10M</li>
<li>Price between $1 and $20</li>
<li>Relative volume above 5</li>
<li>Daily performance above 10%</li>
<li>Handles pagination to collect all relevant stocks</li>

<h3>Outputs:</h3>
<li>A formatted DataFrame for analysis</li>
<li>A CSV file (tickers_only.csv) with just the stock tickers</li>
