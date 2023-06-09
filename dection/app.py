import logging
import os
import streamlit as st
from client import OpenAiTextClassifier
from text_examples import AI_TEXT

with open('api_key.txt', 'r') as file:
    API_KEY = file.read().strip()


st.set_page_config(page_title="OpenAI文本检测器", page_icon="🐙")
st.markdown("""
        <style>
                [data-testid="column"] {
                    width: calc(50% - 1rem);
                }
        </style>
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

if "origin_check_res" not in st.session_state:
    st.session_state.origin_check_res = ""
if "st.session_state.origin_text" not in st.session_state:
    st.session_state.origin_text = ""

detector = OpenAiTextClassifier(API_KEY)
CHECK_RES = "OpenAI文本分类器将文本视为 :{}[**{}**] AI生成.\n({:.2f}%)"


def get_category_color(category):
    color_dict = {
        'very unlikely': 'green',
        'unlikely': 'violet',
        'unclear if it is': 'blue',
        'possibly': 'orange',
        'likely': 'red'
    }
    return color_dict[category]


def origin_text_on_change():
    st.session_state.origin_check_res = ""


def check(text: str):
    '''
    Use OpenAI text classifier to check if text is AI-Generated.
    '''
    if text == '':
        text = AI_TEXT
    if len(text) < 200:
        st.session_state.origin_check_res = "文本不能少于1000个字符."
        return
    logging.info(f"正在检查文本...")
    with origin_text_result_placeholder:
        with st.spinner("正在检查您的文本，请稍候..."):
            rate, category = detector.detect(text)
            st.session_state.origin_check_res = CHECK_RES.format(get_category_color(category), category, rate)


st.header("OpenAI文本检测")
# st.write(
# '''
# 该应用程序将向您展示如何使用[OpenAI Text Classifier](https://platform.openai.com/ai-text-classifier) client.
# ''')
origin_text = st.text_area("**在下方粘贴检测的文本:** ", value=st.session_state.origin_text, key="original",
                           height=400, on_change=origin_text_on_change,
                           help="输入要检查的文本。如果保留为空，将使用默认文本.",
                           placeholder=AI_TEXT)
_, btn_col, _ = st.columns([1, 8, 1])
with btn_col:
    check_clicked = st.button("**AI生成的文本检查**", type="primary", use_container_width=True, on_click=check,
                              args=[origin_text])
origin_text_result_placeholder = st.empty()
if st.session_state.origin_check_res:
    with origin_text_result_placeholder:
        st.info(st.session_state.origin_check_res, icon="ℹ️")
