import pfp

def test_fizzbuzz_generator():
    assert 1 == next(pfp.fizzbuzz(1)) 

def test_fizzbuzz_of_two():
    fizz = pfp.fizzbuzz(2)
    assert [1,2] == [number for number in fizz]
    
def test_fizzbuzz_of_five():
    fizz = pfp.fizzbuzz(5)
    assert [1,2, "fizz", 4, "buzz"] == [number for number in fizz]

def test_fizzbuzz_of_15():
    fizz = pfp.fizzbuzz(15)
    assert [
        1,2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", 
        "buzz", 11, "fizz", 13, 14, "fizzbuzz"
        ] == [number for number in fizz]