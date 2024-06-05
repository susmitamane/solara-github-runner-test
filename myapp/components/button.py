import solara


@solara.component
def MyButton(author: str):
    string = "Stolen! by" + author
    solara.Button(label=string)
