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


def test_main(tmpdir):
    """test main()."""
    path_out = str(tmpdir.join('output.html'))
    file_in = tmpdir.join('in.md')
    file_in.write('''# hello world''')
    path_in = str(file_in)
    md_resume.main(file_out=path_out, file_in=path_in, style={})


def test_main_default_style(tmpdir):
    """test main()."""
    path_out = str(tmpdir.join('output.html'))
    file_in = tmpdir.join('in.md')
    file_in.write('''# hello world''')
    path_in = str(file_in)
    md_resume.main(file_out=path_out, file_in=path_in)


def test_main_no_dir(tmpdir):
    """test main()."""
    path_out = f'{tmpdir}/doesntexistyet/out.html'
    file_in = tmpdir.join('in.md')
    file_in.write('''# hello world''')
    path_in = str(file_in)
    md_resume.main(file_out=path_out, file_in=path_in)
