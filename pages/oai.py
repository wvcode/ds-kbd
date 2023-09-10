"""OpenAI API connector."""

# Import from standard library
import os
import logging

# Import from 3rd party libraries
import openai

import os

# Suppress openai request/response logging
# Handle by manually changing the respective APIRequestor methods in the openai package
# Does not work hosted on Streamlit since all packages are re-installed by Poetry
# Alternatively (affects all messages from this logger):
logging.getLogger("openai").setLevel(logging.WARNING)


class Openai:
    """OpenAI Connector."""

    @staticmethod
    def set_key(key: str):
        openai.api_key = key

    @staticmethod
    def moderate(prompt: str) -> bool:
        """Call OpenAI GPT Moderation with text prompt.
        Args:
            prompt: text prompt
        Return: boolean if flagged
        """
        try:
            response = openai.Moderation.create(prompt)
            return response["results"][0]["flagged"]

        except Exception as e:
            logging.error(f"OpenAI API error: {e}")

    @staticmethod
    def complete(prompt: str, temperature: float = 0.9, max_tokens: int = 2048) -> str:
        """Call OpenAI GPT Completion with text prompt.
        Args:
            prompt: text prompt
        Return: predicted response text
        """
        kwargs = {
            "engine": "text-davinci-003",
            "prompt": prompt,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": 1,  # default
            "frequency_penalty": 0,  # default,
            "presence_penalty": 0,  # default
        }
        try:
            response = openai.Completion.create(**kwargs)
            lst_resp = [x["text"] for x in response["choices"]]
            return "\n".join(lst_resp)

        except Exception as e:
            logging.error(f"OpenAI API error: {e}")

    @staticmethod
    def image(prompt: str) -> str:
        """Call OpenAI Image Create with text prompt.
        Args:
            prompt: text prompt
        Return: image url
        """
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512",
                response_format="url",
            )
            return response["data"][0]["url"]

        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
