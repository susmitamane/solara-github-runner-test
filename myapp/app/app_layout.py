import solara
from typing import List

print("app_layout.oy loading")


@solara.component
def App(children: List[solara.Element] = []):
    print("render app_layout 2")
    solara.Card(children=children, style="max-width: 20vw;")
