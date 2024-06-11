# API KEY를 환경변수로 관리하기 위한 설정 파일
# 설치: pip install python-dotenv
from dotenv import load_dotenv
import openai
from langchain_openai import ChatOpenAI

# API KEY 정보로드
load_dotenv()

llm = ChatOpenAI(
    temperature=0.1,
    max_tokens=2048,
    model_name="gpt-3.5-turbo",
)

question = "대한민국의 수도는 어디인가요?"

print(f"[답변]: {llm.invoke(question)}")
