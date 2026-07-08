def test_print_output(capsys):
    print("hello world")
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello world"
