from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML Demo", P("Welcome to FastHTML!"))

serve()
