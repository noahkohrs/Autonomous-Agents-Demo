from langchain_openai import ChatOpenAI

def phi4():
    return ChatOpenAI(
        model="phi4",
        base_url="http://172.31.32.1:11434/v1"
    )