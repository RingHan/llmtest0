import os
from openai import OpenAI

from dotenv import load_dotenv,find_dotenv

# LangChain 的核心组件
# 模型 I/O 封装
# LLMs：大语言模型
# Chat Models：一般基于 LLMs，但按对话结构重新封装
# PromptTemple：提示词模板
# OutputParser：解析输出
# 数据连接封装
# Document Loaders：各种格式文件的加载器
# Document Transformers：对文档的常用操作，如：split, filter, translate, extract metadata, etc
# Text Embedding Models：文本向量化表示，用于检索等操作（啥意思？别急，后面详细讲）
# Verctorstores: （面向检索的）向量的存储
# Retrievers: 向量的检索
# 对话历史管理
# 对话历史的存储、加载与剪裁
# 架构封装
# Chain：实现一个功能或者一系列顺序功能组合
# Agent：根据用户输入，自动规划执行步骤，自动选择每步需要的工具，最终完成用户指定的功能
# Tools：调用外部功能的函数，例如：调 google 搜索、文件 I/O、Linux Shell 等等
# Toolkits：操作某软件的一组工具集，例如：操作 DB、操作 Gmail 等等
# Callbacks
_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")
)

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

response = llm.invoke("你是谁")
print(response.content)

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

message = [
    SystemMessage(content="你是AGIClass的课程助理。"),
    HumanMessage(content="我是学员，我叫王卓然。"),
    AIMessage(content="欢迎！"),
    HumanMessage(content="我是谁")
]

ret = llm.invoke(message)

print(ret.content)


# # !pip install qianfan
# # 其它模型分装在 langchain_community 底包中
# from langchain_community.chat_models import QianfanChatEndpoint
# from langchain_core.messages import HumanMessage
# import os
#
# llm = QianfanChatEndpoint(
#     qianfan_ak=os.getenv('ERNIE_CLIENT_ID'),
#     qianfan_sk=os.getenv('ERNIE_CLIENT_SECRET')
# )
#
# messages = [
#     HumanMessage(content="介绍一下你自己")
# ]
#
# ret = llm.invoke(messages)
#
# print(ret.content)


from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template("给我讲个关于{subject}的笑话")
print("===Template===")
print(template)
print("===Prompt===")
print(template.format(subject='小明'))


print("===Invoke===")
llm2 = ChatOpenAI(model="gpt-3.5-turbo")
ret = llm2.invoke(template.format(subject='小明'))
print(ret.content)

from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate
)
from langchain_openai import ChatOpenAI


message3 = [
        SystemMessagePromptTemplate.from_template(
            "你是{product}的客服助手，你的名字叫{name}"
        ),
        HumanMessagePromptTemplate.from_template("{query}")
    ]
template3 = ChatPromptTemplate.from_messages(message3)
llm3 = ChatOpenAI(model="gpt-3.5-turbo")
prompt3 = template3.format(
    product = "AGI课堂",
    name = "瓜瓜",
    query = "你是谁"
)
print(prompt3)
response3 = llm3.invoke(prompt3)
print("===Invoke===")
print(response3.content)


print("========================================================")

from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
human_prompt = "Translate your answer to {language}"
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)
chat_prompt = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder("history"),human_message_template]
)
