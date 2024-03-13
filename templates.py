def html_template(body_text, file_name):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <meta charset="UTF-8">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <head>
    <link rel="stylesheet" type="text/css" href="{file_name}.css">
    </head>
    <body>
    {body_text}
    </body>
    <script src="{file_name}.js"></script>
    </html>
    """
    return html
