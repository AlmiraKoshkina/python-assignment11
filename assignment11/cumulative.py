import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os


base_dir = os.path.dirname(__file__)  # путь к папке assignment11
db_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'python_homework', 'db', 'lesson.db'))


conn = sqlite3.connect(db_path)

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""
df = pd.read_sql(query, conn)

def cumulative(row):
    return df['total_price'][0:row.name + 1].sum()

df['cumulative'] = df.apply(cumulative, axis=1)

df.plot(x='order_id', y='cumulative', kind='line', marker='o')
plt.title('Cumulative Revenue Over Orders')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.grid(True)
plt.tight_layout()
plt.show()
