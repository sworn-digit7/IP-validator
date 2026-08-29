from numb3rs import validates

def test_validates():
    
    assert validates('255.255.255.255') == "True"
    assert validates('512.512.512.512') == "False"
    assert validates('1.2.3.1000') == "False"
    assert validates('192.168.001.1') == "False"
    assert validates('cat') == "False"
