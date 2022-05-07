from error_anonymizer import hello_world
# just to test travis, not for actual functionality

def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'This is my first pip package!\n'
    assert captured.err == ''