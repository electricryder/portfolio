from bank import value

def test_hello():
    assert value("Hello there!") == 0
    assert value("hello") == 0
    assert value("Hello my friend!") == 0
    assert value("hello sir!") == 0
    assert value("hello mate") == 0


def test_h():
    assert value("Hey sir") == 20
    assert value("How are you?") == 20
    assert value("how have you been, sir?") == 20
    assert value("hell yeah!") == 20
    assert value("Here's Johnny!!!") == 20


def test_other_sit():
    assert value("Doing fine?") == 100
    assert value("What's up!") == 100
    assert value("Sup dude!") == 100
    assert value("My friend!!") == 100
    assert value("Look who he is!") == 100
    assert value("Can I help you, ma'm?") == 100

