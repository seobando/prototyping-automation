user_story = """
Acceptance Criteria:

Create a form that contains the following fields with their data types:
  - Complejidad - type list with the values 'Alta', 'Media', 'Baja'
  - Referencia - type list with the values 'Apple', 'Samsung', 'Motorola'
  - Asesor(a) - type string
  - Técnico - type string
  - Suministros - type string

The form should have some validations:
  - The fields of type string should be emails.

The form should following desing criteria:
  - Each field is properly separated.
  - The form should be responsive.

"""

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