from fasthtml.common import *
from dataclasses import dataclass

# Initialize database
db = database('qa.db')
qa_table = db.t.qa
if qa_table not in db.t:
    qa_table.create(id=int, question=str, answer=str, pk='id')
QA = qa_table.dataclass()

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
    # Insert into database
    qa_table.insert({"question": question, "answer": answer})
    
    # Show all Q&As
    qas = qa_table()
    qa_list = Ul(*[Li(f"Q: {qa.question} - A: {qa.answer}") for qa in qas])
    
    return Titled("Submitted!",
        P(f"Added new Q&A:"),
        P(f"Question: {question}"),
        P(f"Answer: {answer}"),
        H2("All Questions and Answers:"),
        qa_list,
        A("Back to form", href="/")
    )

serve()
