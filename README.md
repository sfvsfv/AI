填写密钥
```python
    api_key = os.getenv('OPENAI_API_KEY')
    classifier = OpenAiTextClassifier(api_key)
    score, category = classifier.detect(YOUR_TEXT)
```

执行程序：

```python
streamlit run app.py
```

环境安装
```python
pip install -r requirements.txt
```

配置：
1. sudo yum install python3-virtualenv 安装虚拟环境
2. virtualenv myenv  创建一个新的虚拟环境
3. source myenv/bin/activate  激活虚拟环境
4. 
