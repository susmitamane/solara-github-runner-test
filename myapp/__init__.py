from pathlib import Path

__all__ = ["app", "components"]

__main__ = Path(__file__)

from .app import App, Page
from .components import MyButton, MyComponent
