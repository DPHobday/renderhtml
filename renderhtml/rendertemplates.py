from jinja2 import Environment, FileSystemLoader


class RenderHTML:
    def __init__(self, template_dir: str) -> None:
        """Provides HTML rendering tools. [template_dir] is a relative path to the directory it will search for templates"""
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def render_template(self, filename: str, **kwargs) -> str:
        """Returns HTML from a template using Jinja2 {{ var }} syntax. [filename] must be an existing template within [RenderHTML.template_dir]"""
        return self.env.get_template(filename).render(kwargs)
