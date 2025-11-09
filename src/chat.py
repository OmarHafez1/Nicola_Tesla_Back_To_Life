from __future__ import annotations

import os
from typing import List

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI


def _build_system_prompt() -> str:
    return (
        "You are Nikola Tesla, the visionary electrical engineer and inventor. "
        "Answer questions with enthusiasm for science, electricity, and "
        "innovation. Provide thoughtful, historically informed responses, "
        "and keep your tone curious, humble, and inspirational."
    )


def _load_model() -> ChatGoogleGenerativeAI:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY is not set. Please add it to your environment or .env file."
        )

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    temperature = float(os.getenv("GEMINI_TEMPERATURE", "0.7"))

    try:
        return ChatGoogleGenerativeAI(
            model=model, temperature=temperature, google_api_key=api_key
        )
    except Exception as exc:  # pragma: no cover - defensive guard for setup issues
        raise RuntimeError(
            "Failed to initialise the Gemini chat model. Please verify the model "
            "name and that your API key has access to it."
        ) from exc


def chat_loop() -> None:
    llm = _load_model()
    system_message = SystemMessage(content=_build_system_prompt())
    history: List[AIMessage | HumanMessage] = []

    print("Welcome! Ask Nikola Tesla anything. Type 'exit' to quit.\n")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        messages = [system_message, *history, HumanMessage(content=user_input)]
        response = llm.invoke(messages)
        history.extend([HumanMessage(content=user_input), response])

        print(f"Tesla: {response.content}\n")


if __name__ == "__main__":
    chat_loop()
