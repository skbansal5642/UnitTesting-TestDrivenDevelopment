import pytest


def isMultiple(value, mod):
    return (value % mod) == 0

def fizzBuzz(value):
    if isMultiple(value, 15):
        return "FizzBuzz"
    if isMultiple(value, 5):
        return "Buzz"
    if isMultiple(value, 3):
        return "Fizz"
    return str(value)


def checkFizzBuzz(value, expected_result):
    rval = fizzBuzz(value)
    assert rval == expected_result

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")
    
def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

    
def test_returnsFizzWithMultipleOf3PassedIn():
    checkFizzBuzz(6, "Fizz")
    checkFizzBuzz(12, "Fizz")
    checkFizzBuzz(63, "Fizz")


def test_returnsBuzzWithMultipleOf5PassedIn():
    checkFizzBuzz(5, "Buzz")
    checkFizzBuzz(10, "Buzz")
    checkFizzBuzz(50, "Buzz")


def test_returnsFizzBuzzWithMultipleOf15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")
    checkFizzBuzz(60, "FizzBuzz")
    checkFizzBuzz(450, "FizzBuzz")
