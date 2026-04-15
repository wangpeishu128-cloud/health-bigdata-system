import mysql.connector

def check_mysql_links():
    try:
        # 连接到MySQL数据库
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rootpassword',
            database='health_db'
        )
        cursor = conn.cursor(dictionary=True)
        
        print("成功连接到MySQL数据库")
        
        # 查看数据库中的表
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("\n数据库中的表：")
        for table in tables:
            print(f"  {list(table.values())[0]}")
        
        # 检查guangxi_news表
        print("\n检查guangxi_news表...")
        cursor.execute("DESCRIBE guangxi_news")
        columns = cursor.fetchall()
        print("表结构：")
        for col in columns:
            print(f"  {col['Field']} ({col['Type']})")
        
        # 查看数据示例
        cursor.execute("SELECT id, title, link, publish_date FROM guangxi_news LIMIT 5")
        rows = cursor.fetchall()
        print("\n数据示例（前5条）：")
        for row in rows:
            print(f"  ID: {row['id']}, 标题: {row['title'][:30]}..., 链接: {row['link'][:50]}..., 日期: {row['publish_date']}")
        
        # 检查是否有空链接
        cursor.execute("SELECT COUNT(*) as count FROM guangxi_news WHERE link IS NULL OR link = ''")
        null_count = cursor.fetchone()['count']
        print(f"\n空链接数量: {null_count}")
        
        # 检查总记录数
        cursor.execute("SELECT COUNT(*) as total FROM guangxi_news")
        total = cursor.fetchone()['total']
        print(f"总记录数: {total}")
        
        # 检查链接格式
        cursor.execute("SELECT link FROM guangxi_news WHERE link LIKE '%http%' LIMIT 3")
        links = cursor.fetchall()
        print("\n链接格式示例：")
        for link in links:
            print(f"  {link['link']}")
        
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        print(f"MySQL错误: {err}")
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    check_mysql_links()