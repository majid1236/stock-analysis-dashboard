import matplotlib.pyplot as plt

def make_graph(stock_data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Date'], stock_data['Close'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price USD')
    plt.grid(True)
    plt.show()

# Example:
# make_graph(gme_data, 'GameStop Stock Price Over Time')
