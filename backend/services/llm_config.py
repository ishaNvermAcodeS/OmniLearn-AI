import os
from dotenv import load_dotenv

load_dotenv()

# Groq retires models over time; change GROQ_MODEL in backend/.env instead of editing code.
# See the available models with: client.models.list()
GROQ_MODEL = os.getenv("GROQ_MODEL", "").strip() or "openai/gpt-oss-120b"


def groq_model_kwargs() -> dict:
    kwargs = {"model": GROQ_MODEL}
    # gpt-oss models reason before answering and that reasoning counts toward max_tokens,
    # so keep it short or tight token budgets can come back with an empty answer.
    if GROQ_MODEL.startswith("openai/gpt-oss"):
        kwargs["reasoning_effort"] = "low"
    return kwargs
