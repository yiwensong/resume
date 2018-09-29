"""md_resume_test.py

Tests for md_resume.
"""
import sys
from unittest import mock

import md_resume


def test_convert_file(tmpdir):
    """Tests a file conversion."""
    md_file = tmpdir.join('markdown.md')
    md_file.write('''# hello world''')
    html = md_resume.convert_file(str(md_file))
    assert '<h1>' in html
    assert 'hello world' in html
    assert '</h1>' in html


def test_convert_css_from_dict():
    """test dict to css conversion."""
    css_dict = {
        'p': {
            'font-size': '2em',
        },
        'h1': {
            'font-size': '1em',
            'color': 'red',
        },
    }
    css = md_resume.generate_css_from_dict(css_dict)
    assert css == 'p{font-size:2em;}h1{font-size:1em;color:red;}'


def test_add_css_to_html():
    """test adding css."""
    result = md_resume.add_css_to_html('a', 'b')
    assert result == '<style>b</style>a'


def test_convert_to_html(tmpdir):
    """test convert_to_html()."""
    path_out = str(tmpdir.join('output.html'))
    file_in = tmpdir.join('in.md')
    file_in.write('''# hello world''')
    path_in = str(file_in)
    md_resume.convert_to_html(file_out=path_out, file_in=path_in, style={})


def test_convert_to_html_default_style(tmpdir):
    """test convert_to_html()."""
    path_out = str(tmpdir.join('output.html'))
    file_in = tmpdir.join('in.md')
    file_in.write('''# hello world''')
    path_in = str(file_in)
    md_resume.convert_to_html(file_out=path_out, file_in=path_in)


def test_convert_to_html_no_dir(tmpdir):
    """test convert_to_html()."""
    path_out = f'{tmpdir}/doesntexistyet/out.html'
    file_in = tmpdir.join('in.md')
    file_in.write('''# hello world''')
    path_in = str(file_in)
    md_resume.convert_to_html(file_out=path_out, file_in=path_in)


def test_convert_to_html_stylesheet(tmpdir):
    """test convert_to_html() with a stylesheet."""
    path_out = f'{tmpdir}/doesntexistyet/out.html'
    file_in = tmpdir.join('in.md')
    file_in.write('''# hello world''')
    path_in = str(file_in)
    stylesheet = tmpdir.join('style.css')
    stylesheet.write('.p {font-size: 10px}')
    md_resume.convert_to_html(
        file_out=path_out,
        file_in=path_in,
        stylesheet=str(stylesheet),
    )


@mock.patch('md_resume.convert_to_html')
def test_main(mock_convert_to_html):
    """Tests the argparsing of md_resume."""
    sys.argv.clear()
    sys.argv.extend(['garbage', 'input', 'output', '--style', 'stylesheet'])
    md_resume.main()
    mock_convert_to_html.assert_called_with(
        file_in='input',
        file_out='output',
        stylesheet='stylesheet',
    )
