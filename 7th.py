import pandas as pd
data = {
    'customer ID': [11, 12, 13,14, 15, 12, 11],
    'order date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05', '2023-07-06', '2023-07-07'],
    'product name': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'order quantity': [1, 3, 5, 2, 3, 5, 6]
}
order_data = pd.DataFrame(data)
order_data['order date'] = pd.to_datetime(order_data['order date'])
total_orders_per_customer = order_data['customer ID'].value_counts()
average_order_quantity_per_product = order_data.groupby('product name')['order quantity'].mean()
earliest_order_date = order_data['order date'].min()
latest_order_date = order_data['order date'].max()
print("Total number of orders made by each customer:")
print(total_orders_per_customer)
print("\nAverage order quantity for each product:")
print(average_order_quantity_per_product)
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
