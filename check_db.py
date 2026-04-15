import sqlite3

def check_database():
    conn = sqlite3.connect('health_news.db')
    cursor = conn.cursor()
    
    # 查看所有表
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print('数据库中的表：')
    for table in tables:
        print(f'  {table[0]}')
    
    # 查看guangxi_health_news表结构
    print('\nguangxi_health_news表结构：')
    cursor.execute("PRAGMA table_info(guangxi_health_news);")
    columns = cursor.fetchall()
    for col in columns:
        print(f'  {col[1]} ({col[2]})')
    
    # 查看数据示例
    cursor.execute('SELECT id, title, link, publish_date FROM guangxi_health_news LIMIT 5')
    rows = cursor.fetchall()
    print('\n数据示例（前5条）：')
    for row in rows:
        print(f'  ID: {row[0]}, 标题: {row[1][:30]}..., 链接: {row[2][:50]}..., 日期: {row[3]}')
    
    # 检查是否有空链接
    cursor.execute("SELECT COUNT(*) FROM guangxi_health_news WHERE link IS NULL OR link = ''")
    null_count = cursor.fetchone()[0]
    print(f'\n空链接数量: {null_count}')
    
    # 检查链接格式
    cursor.execute("SELECT link FROM guangxi_health_news WHERE link LIKE '%http%' LIMIT 3")
    links = cursor.fetchall()
    print('\n链接格式示例：')
    for link in links:
        print(f'  {link[0]}')
    
    conn.close()

if __name__ == "__main__":
    check_database()