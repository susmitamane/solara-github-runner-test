import solara
from typing import List


@solara.component
def MyComponent(content: str, btn: List[solara.Element]):
    with solara.Column(children=btn):
        solara.Text(content + "Hiyo")
