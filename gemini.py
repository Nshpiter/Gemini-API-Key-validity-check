import requests

def check_gemini_key(proxy_url, gemini_key):
    # 使用 Gemini API 的模型端点来验证
    url = f"{proxy_url}/v1beta/models/gemini-pro"  # 修改为实际的 Gemini API 端点
    headers = {
        "x-goog-api-key": gemini_key  # 修改认证头格式
    }
    try:
        response = requests.get(url, headers=headers)
        print(f"Debug: Response status code: {response.status_code}")
        print(f"Debug: Response text: {response.text}")
        # 200 表示成功，403 通常表示认证失败
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking Gemini key: {e}")
        return False

def process_gemini_keys(input_file, output_file, proxy_url):
    valid_keys = []
    invalid_count = 0

    with open(input_file, 'r') as file:
        keys = file.readlines()

    for key in keys:
        gemini_key = key.strip()
        if check_gemini_key(proxy_url, gemini_key):
            valid_keys.append(gemini_key)
        else:
            invalid_count += 1

    with open(output_file, 'w') as file:
        for key in valid_keys:
            file.write(f"{key}\n")

    print(f"Valid keys count: {len(valid_keys)}")
    print(f"Invalid keys count: {invalid_count}")

# Example usage
proxy_url = "https://exquisite-marzipan-e599d6.netlify.app"
input_file = "gemini.txt"
output_file = "valid_gemini_keys.txt"
process_gemini_keys(input_file, output_file, proxy_url)