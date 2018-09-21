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
