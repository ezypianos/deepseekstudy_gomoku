import os
import traceback
from openai import OpenAI

api_key = os.getenv("DEEPSEEK_API_KEY")
 
if not api_key:
	print("Can not find deepseek api key")
	exit()
else:
	print("Api key read successfully")

client = OpenAI(api_key = api_key,
		base_url = "https://api.deepseek.com/v1")

prompt = """请帮我用HTML生成一个五子棋游戏，所有的代码保存在一个HTML中"""
try:
	response = client.chat.completions.create(model = "deepseek-chat", 
messages = [
	{"role": "system", "content": "你是一个专业的Web开发助手，擅长用html/css/javascript编写游戏"}, 
	{"role": "user", "content": prompt}], stream=False)

	print("\n Deepseek response:")
	if response.choices and len(response.choices) > 0:	
		html_content = response.choices[0].message.content
		with open("gomoku.html", "w", encoding="utf-8") as f:
			f.write(html_content)

	else:
		print("No response returned")
except Exception as e:
	print(f"Invocation failed: {e}")
	traceback.print_exc()
