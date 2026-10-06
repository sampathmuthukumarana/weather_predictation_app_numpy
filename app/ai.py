from openai import AsyncOpenAI
from app.config import settings

client = AsyncOpenAI(api_key=settings.openai_api_key)

async def call_model(message: str) -> str:

    response = await client.responses.create(
        model=settings.openai_model,
        input=message,
    )
    return response.output_text
