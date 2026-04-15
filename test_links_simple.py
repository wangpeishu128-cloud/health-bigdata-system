import requests
import json

# 测试API是否返回链接字段
def test_api_links():
    base_url = "http://127.0.0.1:5000"
    
    # 首先登录获取session
    session = requests.Session()
    
    # 登录为管理员
    login_data = {
        'username': 'admin',
        'password': 'admin123',
        'role': 'admin'
    }
    
    print("登录中...")
    try:
        login_response = session.post(f"{base_url}/login", data=login_data)
        if login_response.status_code == 200:
            print("登录成功")
        else:
            print(f"登录失败: {login_response.status_code}")
            return
    except Exception as e:
        print(f"登录异常: {e}")
        return
    
    # 测试广西新闻API
    print("\n测试广西新闻API...")
    try:
        response = session.get(f"{base_url}/api/news/region?scope=guangxi")
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if items:
                print(f"  成功获取 {len(items)} 条新闻")
                # 检查第一条新闻是否有链接字段
                first_item = items[0]
                print(f"  第一条新闻:")
                print(f"    ID: {first_item.get('id')}")
                print(f"    标题: {first_item.get('title')}")
                print(f"    链接: {first_item.get('link', '未找到链接字段')}")
                print(f"    发布日期: {first_item.get('publish_date')}")
                print(f"    来源: {first_item.get('source')}")
                
                # 检查所有新闻是否有链接
                with_links = sum(1 for item in items if item.get('link'))
                print(f"  有链接的新闻: {with_links}/{len(items)}")
            else:
                print("  没有获取到新闻数据")
        else:
            print(f"  API请求失败: {response.status_code}")
            print(f"  响应内容: {response.text}")
    except Exception as e:
        print(f"  请求异常: {e}")
    
    print("\n测试国家新闻API...")
    try:
        response = session.get(f"{base_url}/api/news/region?scope=national")
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if items:
                print(f"  成功获取 {len(items)} 条新闻")
                # 检查第一条新闻是否有链接字段
                first_item = items[0]
                print(f"  第一条新闻:")
                print(f"    ID: {first_item.get('id')}")
                print(f"    标题: {first_item.get('title')}")
                print(f"    链接: {first_item.get('link', '未找到链接字段')}")
                print(f"    发布日期: {first_item.get('publish_date')}")
                print(f"    来源: {first_item.get('source')}")
                
                # 检查所有新闻是否有链接
                with_links = sum(1 for item in items if item.get('link'))
                print(f"  有链接的新闻: {with_links}/{len(items)}")
            else:
                print("  没有获取到新闻数据")
        else:
            print(f"  API请求失败: {response.status_code}")
            print(f"  响应内容: {response.text}")
    except Exception as e:
        print(f"  请求异常: {e}")
    
    print("\n测试全部新闻API...")
    try:
        response = session.get(f"{base_url}/api/news/region?scope=all")
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if items:
                print(f"  成功获取 {len(items)} 条新闻")
                # 检查第一条新闻是否有链接字段
                first_item = items[0]
                print(f"  第一条新闻:")
                print(f"    ID: {first_item.get('id')}")
                print(f"    标题: {first_item.get('title')}")
                print(f"    链接: {first_item.get('link', '未找到链接字段')}")
                print(f"    发布日期: {first_item.get('publish_date')}")
                print(f"    来源: {first_item.get('source')}")
                
                # 检查所有新闻是否有链接
                with_links = sum(1 for item in items if item.get('link'))
                print(f"  有链接的新闻: {with_links}/{len(items)}")
            else:
                print("  没有获取到新闻数据")
        else:
            print(f"  API请求失败: {response.status_code}")
            print(f"  响应内容: {response.text}")
    except Exception as e:
        print(f"  请求异常: {e}")

if __name__ == "__main__":
    test_api_links()