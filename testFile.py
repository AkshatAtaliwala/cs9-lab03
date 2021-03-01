from lab03 import multiply
from lab03 import collectOddValues
from lab03 import countInts
from lab03 import reverseString
from lab03 import removeSubString


def test_multiply():
    assert multiply(5,4) == 20
    assert multiply(5,1) == 5
    assert multiply(1,5) == 5
    assert multiply(5,0) == 0
    
def test_collectOddValues():
    assert collectOddValues([1,2,3,4,5]) == [1,3,5]
    assert collectOddValues([1,1,1,1,1]) == [1,1,1,1,1]
    assert collectOddValues([2,2,2,2,2]) == []
    assert collectOddValues([1]) == [1]
    assert collectOddValues([2]) == []

def test_countInts():
    assert countInts([1,2,3,4,3,2,1], 2) == 2
    assert countInts([1,2,3,4,3,2,1], 5) == 0
    assert countInts([2,2,2,2,2,2,2], 2) == 7
    assert countInts([], 2) == 0
    assert countInts([14], 14) == 1
    assert countInts([14], 13) == 0

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("") == ""
    assert reverseString("C") == "C"
    assert reverseString("CM") == "MC"
    assert reverseString("123456789") == "987654321"

def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("Lolololol", "Lo") == "lololol"
    assert removeSubString("Lolololol", "jk") == "Lolololol"
    assert removeSubString("L", "l") == "L"
    assert removeSubString("LlolLlol", "lol") == "LL"
    assert removeSubString("jk", "jk") == ""


