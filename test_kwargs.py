
def test(**kwargs):
    for k,v in kwargs.items():
        print(k, "=", v)

def test2(kwargs={}):
    for k,v in kwargs.items():
        print(k, "=", v)
d = {
    "k1": "v1",
    "k2": "v2"
}

test(**d)
test2(d)
test()
test2()
