from typing import Optional
from jinja2 import Environment, FileSystemLoader


class RenderHTML:
    def __init__(self, template_dir: Optional[str]=None) -> None:
        if template_dir:
            self.template_dir = template_dir
        else:
            self.template_dir = "./"
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def render_template(self, filename: str, **kwargs) -> str:
        """Returns a html template replacing placeholders with key word args"""
        return self.env.get_template(filename).render(kwargs)