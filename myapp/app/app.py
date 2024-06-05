import myapp
import solara

print("loading app.py")


@solara.component
def Page():
    print("render 2")
    btn = [myapp.MyButton("ME!"), solara.Button(label="Maybe")]

    with solara.Div(style="height: 40vh; width: 85vw; background-color: red;"):
        with myapp.App():
            myapp.MyComponent("Oh yes", btn)
