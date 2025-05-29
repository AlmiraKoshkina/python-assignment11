import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt


base_dir = os.path.dirname(__file__)
db_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'python_homework', 'db', 'lesson.db'))

conn = sqlite3.connect(db_path)

query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""
df = pd.read_sql(query, conn)

df.plot(kind='bar', x='last_name', y='revenue', color='skyblue', legend=False)
plt.title('Revenue by Employee')
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.show()
