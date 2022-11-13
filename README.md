<h1 align="center">Renderhtml</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/dan-hobday/renderhtml?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/dan-hobday/renderhtml?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/dan-hobday/renderhtml?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/dan-hobday/renderhtml?color=56BEB8">

</p>

<!-- Status -->

 <h4 align="center"> 
	🚧  Renderhtml 🚀 Under construction...  🚧
</h4> 

<hr>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/dan-hobday" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

A simple module for dynamically building html with Python code. It was written as a helper for my work in data manipulation and will probably grow with those requirements. 

## :sparkles: Features ##

:heavy_check_mark: Dynamically build HTML;\
:heavy_check_mark: Set the values of HTML placeholders;\
:heavy_check_mark: Combine multiple templates;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python3](https://python.org/)
- [Jinja2](https://pypi.org/project/Jinja2/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python](https://python.org/) V3.6+ and [Pip](https://pypi.org/project/Jinja2/) installed. It is highly recomended you use a virtual environment like venv! If you do not already have [Jinja2](https://pypi.org/project/Jinja2/) installed in your env it will be installed with this package.

## :checkered_flag: Starting ##

```bash
# Clone this project

$ cd /my/install/location

$ git clone https://github.com/dphobday/renderhtml
```
## :computer: Use ##
```bash
$ pip install /my/install/location/renderhtml
```

```html
<!--example.html-->

<p><strong>{{ title }}</strong></p>
```

``` python
# main.py

from renderhtml import RenderHTML

# Setup
render = RenderHTML("/Path/to/my/templates")

def main():
  title = "Hello World!"
  html = render.render_template("example.html", title=title)

main()
```


## :memo: License ##

This project is licensed under GPL-3.0. For more details, see the [LICENSE](LICENSE) file.


Made by <a href="https://github.com/dphobday" target="_blank">github.com/dphobday</a>

&#xa0;

<a href="#top">Back to top</a>
