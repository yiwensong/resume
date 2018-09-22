"""md_resume"""
import os
import typing

import markdown

DEFAULT_STYLE = {
    'body': {
        'font-size': 'smaller',
        'font-family': '"Helvetica Neue", Arial, sanserif',
    },
    'h1': {
        'font-size': '5em',
        'margin-top': '0px',
        'margin-bottom': '5px',
    },
    'h2': {
        'margin-top': '2px',
        'margin-bottom': '0px',
    },
    'h3': {
        'margin-top': '2px',
        'margin-bottom': '0px',
    },
    'ul': {
        'margin-top': '0px',
        'margin-bottom': '0px',
    },
    'li': {
        'line-height': '1.1em',  # emojis
    },
    'p': {
        'margin-top': '0px',
        'margin-bottom': '0px',
        'line-height': '1.1em',  # emojis
    },
    'hr': {
        'margin-top': '3px',
        'margin-bottom': '3px',
    },
}


def convert_file(path: str) -> str:
    """Converts a markdown file into html text."""
    with open(path, 'r') as file_:
        text = file_.read()
    return markdown.markdown(text)


def generate_css_from_dict(css_dict: typing.Dict) -> str:
    """Returns a css string from a dictionary.

    Example input:

    {
        'p': {
            'font-size': '1em',
            'color': 'blue',
        },
        'h1': {
            'font-size': '2em',
            'color': 'red',
        },
    }
    """

    def subdict_to_string(dict_: typing.Dict) -> str:
        """Converts a style dict into a css string."""
        str_ = '{'
        for attr, value in dict_.items():
            str_ += f'{attr}:{value};'
        str_ += '}'
        return str_

    str_ = ''
    for elem, styles in css_dict.items():
        style_string = subdict_to_string(styles)
        str_ += f'{elem}{style_string}'
    return str_


def add_css_to_html(html: str, css: str) -> str:
    """Sticks the css into a <style> tag."""
    return f'''<style>{css}</style>{html}'''


def main(
        file_out: str = 'build/resume.html',
        file_in: str = 'README.md',
        style: typing.Optional[typing.Dict] = None,
) -> None:
    """Converts README.md into a nice html."""
    if style is None:
        style = DEFAULT_STYLE
    file_out_dir = os.path.dirname(file_out)
    if not os.path.exists(file_out_dir):
        os.makedirs(file_out_dir)
    html = convert_file(file_in)
    css = generate_css_from_dict(style)
    pretty = add_css_to_html(html, css)
    with open(file_out, 'w') as output_fd:
        output_fd.write(pretty)


if __name__ == '__main__':
    main()
