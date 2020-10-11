import hello


def test_says_world():
    assert hello.say_what() == 'world'

def test_empty():
    assert len(hello.say_what()) != ''
    
def test_1():
    assert 1==1

def test_2():
    assert 2+2==4
 
def test_null():
    assert 2+2!=null
