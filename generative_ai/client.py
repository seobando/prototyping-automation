import os
from openai import OpenAI

api_key  = os.environ.get("OPENAI_API_KEY")

open_ai = OpenAI(
    api_key=api_key
)

