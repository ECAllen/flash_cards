from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    form = Form(
        Group(
            Label("Question:", Input(id="question", name="question", type="text")),
            Label("Answer:", Input(id="answer", name="answer", type="text")),
            Button("Submit", type="submit")
        ),
        method="post",
        action="/"
    )
    
    return Titled("Q&A Form", form)

@rt("/")
def post(question: str, answer: str):
    return Titled("Submitted!", 
        P(f"Question: {question}"),
        P(f"Answer: {answer}"),
        A("Back to form", href="/")
    )

serve()
