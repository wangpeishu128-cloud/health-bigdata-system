import requests
import json

# 测试登录
login_url = "http://127.0.0.1:5000/login"
admin_dashboard_url = "http://127.0.0.1:5000/admin/dashboard"
api_action_url = "http://127.0.0.1:5000/admin/api/action"

# 创建会话
session = requests.Session()

print("1. 测试登录...")
# 首先获取登录页面
response = session.get(login_url)
print(f"登录页面状态码: {response.status_code}")

# 尝试登录
login_data = {
    'username': 'admin',
    'password': 'admin123',
    'role': 'admin'
}

response = session.post(login_url, data=login_data)
print(f"登录响应状态码: {response.status_code}")
print(f"登录后重定向到: {response.url}")

print("\n2. 测试管理员仪表板...")
response = session.get(admin_dashboard_url)
print(f"管理员仪表板状态码: {response.status_code}")
print(f"页面标题包含'管理员': {'管理员' in response.text}")

print("\n3. 测试新添加的快捷管理API...")
# 测试数据清理功能
action_data = {'action': 'clean_data'}
response = session.post(api_action_url, json=action_data)
print(f"数据清理API状态码: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print(f"响应结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
else:
    print(f"响应内容: {response.text}")

print("\n4. 测试数据备份功能...")
action_data = {'action': 'backup_data'}
response = session.post(api_action_url, json=action_data)
print(f"数据备份API状态码: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print(f"响应结果: {json.dumps(result, ensure_ascii=False, indent=2)}")

print("\n5. 测试用户管理功能...")
action_data = {'action': 'user_management'}
response = session.post(api_action_url, json=action_data)
print(f"用户管理API状态码: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print(f"响应结果: {json.dumps(result, ensure_ascii=False, indent=2)}")

print("\n6. 测试系统日志功能...")
action_data = {'action': 'system_logs'}
response = session.post(api_action_url, json=action_data)
print(f"系统日志API状态码: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print(f"响应结果: {json.dumps(result, ensure_ascii=False, indent=2)}")