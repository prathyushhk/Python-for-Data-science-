import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, stock):
    fig = make_subplots(rows=1, cols=1, subplot_titles=("Historical Share Price"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data['Date'], infer_datetime_format=True), y=stock_data['Close'].astype("float"), name="Share Price"), row=1, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_layout(showlegend=False,
                      height=600,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    fig.show()

# Extract Tesla stock data
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period='max')
tesla_data.reset_index(inplace=True)

# Display the graph
make_graph(tesla_data[['Date', 'Close']], 'Tesla')

# Display the first few rows of the data
print(tesla_data.head())
