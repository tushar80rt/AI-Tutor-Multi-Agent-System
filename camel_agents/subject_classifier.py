from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.configs import MistralConfig
from camel.agents import ChatAgent
from camel.messages import BaseMessage
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

def classify_subject(query: str) -> str:
    system_message = BaseMessage.make_assistant_message(
        role_name="assistant",
        content="You are a helpful assistant. Classify the subject of the user's query using only one word like: physics, chemistry, biology, math, history, english, or general."
    )

    agent = ChatAgent(
        system_message=system_message,
        message_window_size=10,
        model=mistral_model,
    )

    user_message = BaseMessage.make_user_message(
        role_name="user",
        content=query
    )

    response = agent.step(user_message)
    full_response = response.msg.content.strip().lower()


    for subject in ["physics", "chemistry", "biology", "math", "history", "english", "general"]:
        if subject in full_response:
            return subject

    return "general"
