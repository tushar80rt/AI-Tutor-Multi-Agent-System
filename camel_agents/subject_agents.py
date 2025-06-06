from camel.messages import BaseMessage
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import MistralConfig
import os
from dotenv import load_dotenv


load_dotenv("api.env")


mistral_config = MistralConfig(temperature=0.0)
mistral_model = ModelFactory.create(
    model_platform=ModelPlatformType.MISTRAL,
    model_type=ModelType.MISTRAL_LARGE,
    model_config_dict=mistral_config.as_dict(),
    api_key=os.getenv("MISTRAL_API_KEY")
)

def create_camel_agent(role_desc: str, user_query: str):
    system_message = BaseMessage.make_assistant_message(
        role_name="assistant",
        content=f"You are a helpful document assistant. Always answer based only on the provided OCR document and act as an expert in {role_desc}."
    )
    agent = ChatAgent(
        system_message=system_message,
        message_window_size=10,
        model=mistral_model,
    )
    user_message = BaseMessage.make_user_message(
        role_name="user",
        content=user_query
    )
    response = agent.step(user_message)
    return response.msg.content

def get_agent_by_subject(subject: str):
    subject_map = {
        "physics": "Physics",
        "math": "Mathematics",
        "history": "History",
        "biology": "Biology",
        "chemistry": "Chemistry",
        "english": "English Literature"
    }
    subject = subject.strip().lower()
    if subject not in subject_map:
        def fallback_agent(user_query):
            return create_camel_agent("General Knowledge", user_query)
        return fallback_agent
    def run_agent(user_query):
        return create_camel_agent(subject_map[subject], user_query)
    return run_agent

