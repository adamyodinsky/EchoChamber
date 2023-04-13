import time
import tiktoken
import os
import openai

TOKENIZER = tiktoken.get_encoding("cl100k_base")

def exceeding_token_limit(total_usage: int, token_limit: int):
    """Returns True if the total_usage is greater than the token limit with some safe buffer."""

    return total_usage > token_limit


def num_tokens_from_messages(messages) -> int:
    """Returns the number of tokens used by a list of messages."""

    encoding = TOKENIZER
    num_tokens = 0
    for message in messages:
        num_tokens += (
            4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        )
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens -= 1  # role is always required and always 1 token
    num_tokens -= 2  # every reply is primed with <im_start>assistant
    return num_tokens


def reduce_tokens(messages: list, token_limit: int, total_usage: int):
    """Reduce tokens in messages context."""

    reduce_amount = total_usage - token_limit
    tokenized_message = []
    while exceeding_token_limit(total_usage, token_limit):
        message = messages.pop(1)
        tokenized_message = TOKENIZER.encode(message["content"])

        while reduce_amount > 0 and len(tokenized_message) > 0:
            total_usage -= 1
            reduce_amount -= 1
            tokenized_message.pop(0)

        if len(tokenized_message) == 0 and exceeding_token_limit(
            total_usage, token_limit
        ):
            # every message follows <im_start>{role/name}\n{content}<im_end>\n
            # thus we need to remove 4 tokens for every message that will be removed
            # so if the message is empty
            reduce_amount -= 4
            total_usage -= 4

            for key, _ in message.items():
                if key == "name":  # if there's a name, the role is omitted
                    # role is always required and always 1 token
                    reduce_amount += 1
                    total_usage += 1

    if len(tokenized_message) > 0:
        message["content"] = TOKENIZER.decode(tokenized_message)
        messages.insert(1, message)

    if os.environ.get("LOG_LEVEL") == "DEBUG":
        counted_tokens = num_tokens_from_messages(messages)
        print(f"Counted usage: {total_usage}")
        print(f"Real usage tokens: {counted_tokens}")

    return messages, total_usage



def get_user_answer(messages):
    """Returns the answer from OpenAI API."""

    while True:
        try:
          answer = openai.ChatCompletion.create(
              model='gpt-3.5-turbo-0301', messages=messages
          )
          return answer
        except openai.error.InvalidRequestError as error:
            if "Please reduce the length of the messages" in str(error):
                messages.pop(1)
                time.sleep(0.5)
            else:
                raise error