import ast
import os
from client import open_ai
from const import prompt
from prettify import prettify_text
from templates import html_template


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


def generate_documents(data_dict, folder_name):
    for proposal_name, files in data_dict.items():
        print("proposal: ", proposal_name)
        for file_type, text in files.items():
            print("file_type: ", file_type)

            if file_type == "html":
                html = html_template(text, proposal_name)
                text_clean = clean_text(html, file_type)
            else:
                text_clean = clean_text(text, file_type)

            file_name = proposal_name + "." + file_type
            save_document(file_name, folder_name, text_clean)


if __name__ == "__main__":
    folder_name = "prototypes"
    response = get_completition(open_ai, prompt, model="gpt-3.5-turbo")
    data_dict = get_data_dict(response)
    generate_documents(data_dict, folder_name)
