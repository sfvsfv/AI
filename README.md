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

