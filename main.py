from flask import Flask, request, jsonify
from flask_cors import CORS  # 解决跨域
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)  # 允许油猴脚本跨域请求



#AI调用
def ai(subject):
    # 创建OpenAI客户端
    client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    # 构造提示词 - 只问书名相关的问题
    prompt=f'''
    以下为任务要求：
    1. 题目列表：{subject}
    2. 请执行以下操作：
    - 为每道题生成对应的答案（选择题输出选项字母，如"A"、"BCD"；其他题型输出正确内容）
    - 答案必须与题目一一对应，按顺序排列
    3. 输出格式要求：
    - 纯JSON数组格式:["答案1","答案2","答案3",...]
    - 数组长度必须等于题目总数量
    - 只输出JSON数组,不要添加任何解释、说明或其他文字
    5. 示例：
    输入：[{{题目A}},{{题目B}},{{题目C}}]
    输出：["A","B","C"]
    '''
    completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": "你负责题目解答"},
        {"role": "user", "content": prompt}
    ]
    )
    return completion.choices[0].message.content
    


#数据接收
@app.route('/solve', methods=['POST'])
def solve():
    print("接收到请求")
    data = request.json
    subject= data.get('subject',[])
    answer=ai(subject)
    print(answer)
    return jsonify(answer)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #print(completion.choices[0].message.content)
    #return jsonify({"answer":completion.choices[0].message.content})


    


