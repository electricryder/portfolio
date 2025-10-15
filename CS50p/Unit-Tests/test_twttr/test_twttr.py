from twttr import shorten

def test_shorten():
    assert shorten("Pedro") == "Pdr"
    assert shorten("pedro") == "pdr"
    assert shorten("PEDRO") == "PDR"
    assert shorten("Electric.RYDER") == "lctrc.RYDR"
    assert shorten("CristianoRonaldo7") == "CrstnRnld7"
