import itertools
import sys

from openai import OpenAI

from chatgpt_handler import print_chatgpt_response

INSTRUCTIONS = """You are an experienced Chinese chef and you always try to be as clear as possible. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.

You should only criticize recipes and suggest changes only for Chinese dishes. That is, if the user passes a recipe, suggest what could be improved. If you can't think of any changes, say: "Looks good to me." If the user says something irrelevant, say: "I decline to respond." 

If the user doesn't provide the recipe, say "No recipe was provided."

Remember, you are Chinese chef. You only now how to make Chinese dishes and recipes.
"""


def give_recipe_feedback(client: OpenAI, model: str) -> None:
    """Gives feedback on the user's recipe.

    If the input is not a recipe, it'll be pointed out.

    Args:
        client: An OpenAI client.
        model: An OpenAI model.
    """
    print('Enter your recipe (type "quit" when you\'re finished)')
    user_input = "".join(
        list(itertools.takewhile(lambda x: x.strip() != "quit", sys.stdin))
    )

    messages = [
        {
            "role": "system",
            "content": INSTRUCTIONS,
        },
        {
            "role": "user",
            "content": f"How can I improve the following recipe?\n{user_input}",
        },
    ]

    print_chatgpt_response(client, model, messages)
