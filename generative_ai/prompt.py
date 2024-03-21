def create_prompt(user_story):
    output_format = """
    {
    'proposal_1':{
        'css':'<code_here>',
        'js':'<code_here>',
        'html':'<code_here>'
    },
    "proposal_2":{
        'css':'<code_here>',
        'js':'<code_here>',
        'html':'<code_here>'
    },
    "proposal_3":{
        'css':'<code_here>',
        'js':'<code_here>',
        'html':'<code_here>'
    },
    }
    """

    prompt = f"""
    Act as a front-end web developer expert with deep knowledge of UI/UX best practices.

    Based on the following user story delimited by triple backticks create three proposals with the code in html, css and javascript.

    ```{user_story}```

    You should fill the <code_here> parts of the following output format:

    {output_format}

    """
    return prompt
