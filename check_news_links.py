import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost', user='root', password='rootpassword', database='health_db')
    cursor = conn.cursor(dictionary=True)
    
    # 检查guangxi_news表中是否有链接数据
    cursor.execute("SELECT COUNT(*) as total FROM guangxi_news")
    total = cursor.fetchone()['total']
    cursor.execute("SELECT COUNT(*) as with_link FROM guangxi_news WHERE link IS NOT NULL AND link != ''")
    with_link = cursor.fetchone()['with_link']
    
    print('广西新闻表链接统计:')
    print(f'  总记录数: {total}')
    print(f'  有链接的记录数: {with_link}')
    print(f'  无链接的记录数: {total - with_link}')
    
    # 检查一些示例数据
    cursor.execute("SELECT id, title, link FROM guangxi_news WHERE link IS NOT NULL AND link != '' LIMIT 3")
    print('\n广西新闻示例（有链接）:')
    for row in cursor.fetchall():
        title = row['title'][:30] + '...' if len(row['title']) > 30 else row['title']
        link = row['link'][:50] + '...' if len(row['link']) > 50 else row['link']
        print(f'  ID: {row["id"]}, 标题: {title}, 链接: {link}')
    
    print()
    
    # 检查national_news表中是否有链接数据
    cursor.execute("SELECT COUNT(*) as total FROM national_news")
    total = cursor.fetchone()['total']
    cursor.execute("SELECT COUNT(*) as with_link FROM national_news WHERE link IS NOT NULL AND link != ''")
    with_link = cursor.fetchone()['with_link']
    
    print('国家新闻表链接统计:')
    print(f'  总记录数: {total}')
    print(f'  有链接的记录数: {with_link}')
    print(f'  无链接的记录数: {total - with_link}')
    
    # 检查一些示例数据
    cursor.execute("SELECT id, title, link FROM national_news WHERE link IS NOT NULL AND link != '' LIMIT 3")
    print('\n国家新闻示例（有链接）:')
    for row in cursor.fetchall():
        title = row['title'][:30] + '...' if len(row['title']) > 30 else row['title']
        link = row['link'][:50] + '...' if len(row['link']) > 50 else row['link']
        print(f'  ID: {row["id"]}, 标题: {title}, 链接: {link}')
    
    conn.close()
except Exception as e:
    print(f'错误: {e}')