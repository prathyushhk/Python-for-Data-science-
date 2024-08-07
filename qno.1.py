import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define the function to create the graph
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True, 
        subplot_titles=("Historical Share Price", "Historical Revenue"), 
        vertical_spacing=0.3
    )
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(stock_data['Date'], infer_datetime_format=True), 
            y=stock_data['Close'].astype("float"), 
            name="Share Price"
        ), 
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(revenue_data['Date'], infer_datetime_format=True), 
            y=revenue_data['Revenue'].astype("float"), 
            name="Revenue"
        ), 
        row=2, col=1
    )
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(
        showlegend=False,
        height=900,
        title=stock,
        xaxis_rangeslider_visible=True
    )
    fig.show()

# Fetch Tesla data using yfinance
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

# Create mock revenue data (as the actual data fetching is not shown in your script)
# In a real scenario, you would replace this with actual revenue data fetching logic
mock_revenue_data = {
    'Date': tesla_data['Date'], 
    'Revenue': (tesla_data['Close'] * 1000).apply(int)  # This is just a mock, replace with actual revenue data
}
revenue_data = pd.DataFrame(mock_revenue_data)

# Call the function to create and display the graph
make_graph(tesla_data, revenue_data, 'Tesla')
