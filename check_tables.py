import sqlite3

conn = sqlite3.connect('health_news.db')
cursor = conn.cursor()

# 查看所有表
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print('数据库中的表：')
for table in tables:
    print(f'  {table[0]}')

# 如果有表，查看第一个表的结构
if tables:
    first_table = tables[0][0]
    print(f'\n{table}表结构：')
    cursor.execute(f"PRAGMA table_info({first_table})")
    columns = cursor.fetchall()
    for col in columns:
        print(f'  {col[1]} ({col[2]})')

conn.close()