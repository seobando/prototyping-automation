import ast
import os
from generative_ai.client import open_ai
from generative_ai.const import prompt
from generative_ai.prettify import prettify_text
from generative_ai.templates import html_template
from project_manager.client import get_user_story
from generative_ai.prompt import create_prompt


def get_completition(client, prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content


def get_data_dict(response):
    string_data = response.replace("`", '"""')
    data_dict = ast.literal_eval(string_data)
    return data_dict


def clean_text(text, file_type):
    lines = text.split("\n")
    text_without_line_breaker = "\n".join(
        [line.strip() for line in lines if line.strip()]
    )
    text_prettified = prettify_text(text_without_line_breaker, file_type)
    return text_prettified


def save_document(file_name, folder_name, text):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, f"{folder_name}/{file_name}")
    with open(file_path, "w") as file:
        file.write(text)


def generate_documents(ticket_id, data_dict, folder_name):
    for proposal_name, files in data_dict.items():
        print("proposal: ", proposal_name)
        for file_type, text in files.items():
            print("file_type: ", file_type)
            new_proposal_name = ticket_id + "_" + proposal_name
            if file_type == "html":
                html = html_template(text, new_proposal_name)
                text_clean = clean_text(html, file_type)
            else:
                text_clean = clean_text(text, file_type)

            file_name = new_proposal_name + "." + file_type
            save_document(file_name, folder_name, text_clean)


if __name__ == "__main__":
    folder_name = "prototypes"
    tickets = ["E3IG-3", "E3IG-4", "E3IG-5"]
    for ticket_id in tickets:
        try:
            user_story = get_user_story(ticket_id)
            prompt = create_prompt(user_story)
            response = get_completition(open_ai, prompt, model="gpt-3.5-turbo")
            data_dict = get_data_dict(response)
            generate_documents(ticket_id, data_dict, folder_name)            
        except:
            print(f"Please check the ticket {ticket_id} description")

