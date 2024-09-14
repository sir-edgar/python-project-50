from gendiff.modules.difference import generate_diff


def test_diff_json():
    assert generate_diff('/Users/timurvitrov/python-project-50/gendiff/file1.json',
                         '/Users/timurvitrov/python-project-50/gendiff/file2.json') == ('{\n'
                                                                                        '  - follow: False\n'
                                                                                        '    host: hexlet.io\n'
                                                                                        '  - proxy: 123.234.53.22\n'
                                                                                        '  - timeout: 50\n'
                                                                                        '  + timeout: 20\n'
                                                                                        '  + verbose: True\n'
                                                                                        '}')

def test_diff_yaml():
    assert generate_diff('/Users/timurvitrov/python-project-50/gendiff/file1.yaml',
                         '/Users/timurvitrov/python-project-50/gendiff/file2.yaml') == ('{\n'
                                                                                        '  - follow: False\n'
                                                                                        '    host: hexlet.io\n'
                                                                                        '  - proxy: 123.234.53.22\n'
                                                                                        '  - timeout: 50\n'
                                                                                        '  + timeout: 20\n'
                                                                                        '  + verbose: True\n'
                                                                                        '}')