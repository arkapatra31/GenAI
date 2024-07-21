from langchain_core.prompts import  ChatPromptTemplate
from langchain_ollama.llms import  OllamaLLM

template = """Question: {question}
Answer: Let's think step by step."""

llm = OllamaLLM(model = "llama3")

prompt = ChatPromptTemplate.from_template((template))

chain = prompt | llm

chain.invoke({"question": "Tell me about Langchain"})