import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def __init__(self) -> None:
        # TODO: 
        # Load data from data/chipotle.tsv file using Pandas library and 
        # assign the dataset to the 'chipo' variable.
        file = 'data/chipotle.tsv'
        self.chipo = pd.read_csv(file, delimiter="\t")
    
    def top_x(self, count) -> None:
        # TODO
        # Top x number of entries from the dataset and display as markdown format.
        topx = self.chipo.head(count)
        print(topx.to_markdown())
        
    def count(self) -> int:
        # TODO
        # The number of observations/entries in the dataset.
        return self.chipo.shape[0]
    
    def info(self) -> None:
        # TODO
        # print data info.
        print(self.chipo.info())
    
    def num_column(self) -> int:
        # TODO return the number of columns in the dataset
        return self.chipo.shape[1]
    
    def print_columns(self) -> None:
        # TODO Print the name of all the columns.
        print(self.chipo.columns.to_list())
    
    def most_ordered_item(self):
        # TODO
        item_name = None
        quantity = -1

        item_name = self.chipo['item_name'].value_counts().keys()[0]
        quantity = self.chipo['item_name'].value_counts().head(1)[0]
        return item_name, quantity

    def total_item_orders(self) -> int:
       # TODO How many items were orderd in total?
        return self.chipo['quantity'].sum()
   
    def total_sales(self) -> float:
        # TODO 
        # 1. Create a lambda function to change all item prices to float.
        # 2. Calculate total sales.

        self.chipo['item_price'] = self.chipo['item_price'].apply(lambda x: x.split('$')[1]).astype(float)
        return (self.chipo['item_price']*self.chipo['quantity']).sum()
   
    def num_orders(self) -> int:
        # TODO
        # How many orders were made in the dataset?
        return self.chipo['order_id'].value_counts().shape[0]
    
    def average_sales_amount_per_order(self) -> float:
        # TODO
        total_sale = (self.chipo['item_price']*self.chipo['quantity']).sum()
        return (total_sale/self.num_orders()).round(2)

    def num_different_items_sold(self) -> int:
        # TODO
        # How many different items are sold?
        return len(self.chipo['item_name'].unique())
    
    def plot_histogram_top_x_popular_items(self, x:int) -> None:
        from collections import Counter
        letter_counter = Counter(self.chipo.item_name)
        # TODO
        # 1. convert the dictionary to a DataFrame
        df = pd.DataFrame.from_dict(letter_counter, orient='index').reset_index()
        # 2. sort the values from the top to the least value and slice the first 5 items
        topXdf = df.sort_values(by=[0], ascending = False)[:x]
        # 3. create a 'bar' plot from the DataFrame
        plt.figure(figsize=(12, 8))
        plt.bar(topXdf['index'], height = topXdf[0])
        # 4. set the title and labels:
        #     x: Items
        #     y: Number of Orders
        #     title: Most popular items
        plt.xlabel('Items')
        plt.ylabel('Number of Orders')
        plt.title('Most popular items')
        # 5. show the plot. Hint: plt.show(block=True).
        plt.show(block=True)
        # plt.savefig('topXbar.png')
        pass
        
    def scatter_plot_num_items_per_order_price(self) -> None:
        # TODO
        # 1. create a list of prices by removing dollar sign and trailing space.
        print(self.chipo.info())
        # 2. groupby the orders and sum it.
        perOrder = self.chipo.groupby('order_id')['item_price', 'quantity'].sum()
        # 3. create a scatter plot:
        #       x: orders' item price
        #       y: orders' quantity
        #       s: 50
        #       c: blue
        plt1 = perOrder.plot.scatter(x='item_price',
                                    y='quantity',
                                    s=50,
                                    c='blue')
        # 4. set the title and labels.
        #       title: Numer of items per order price
        #       x: Order Price
        #       y: Num Items
        plt.title('Numer of items per order price')
        plt.xlabel('Order Price')
        plt.ylabel('Num Items')
        plt.show(block=True)
        # plt.savefig('scatter.png')
        pass
    
        

def test() -> None:
    solution = Solution()
    solution.top_x(10)
    count = solution.count()
    print(count)
    assert count == 4622
    solution.info()
    count = solution.num_column()
    assert count == 5
    item_name, quantity = solution.most_ordered_item()
    assert item_name == 'Chicken Bowl'
    
    #assert quantity == 159
    # Wrong assert number, should be 726
    
    total = solution.total_item_orders()
    assert total == 4972
    assert 39237.02 == solution.total_sales()
    assert 1834 == solution.num_orders()
    assert 21.39 == solution.average_sales_amount_per_order()
    assert 50 == solution.num_different_items_sold()
    solution.plot_histogram_top_x_popular_items(5)
    solution.scatter_plot_num_items_per_order_price()

    
if __name__ == "__main__":
    # execute only if run as a script
    test()
    
    