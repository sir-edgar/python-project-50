from gendiff.modules.difference import generate_diff


def test_diff():
    assert generate_diff('gendiff/file1.json',
                         'gendiff/file2.json') == ('- follow: False\n'
                                                   '  host: hexlet.io\n'
                                                   '- proxy: 123.234.53.22\n'
                                                   '- timeout: 50\n'
                                                   '+ timeout: 20\n'
                                                   '+ verbose: True\n')