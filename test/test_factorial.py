from factorial_module.factorial_module import factorial_recursion, factorial_iterative, clumsy

def test_factorial_recursion_1():
    actual = factorial_recursion(8)
    expected = 40320
    assert actual == expected
    #
def test_factorial_recursion_2():
    actual = factorial_recursion(7)
    expected = 5040
    assert actual == expected
    #
def test_factorial_recursion_3():
    actual = factorial_recursion(9)
    expected = 362880
    assert actual == expected
    # --------------------

def test_factorial_iterative_1():
    actual = factorial_iterative(8)
    expected = 40320
    assert actual == expected
    #
def test_factorial_iterative_2():
    actual = factorial_iterative(7)
    expected = 5040
    assert actual == expected
    #
def test_factorial_iterative_3():
    actual = factorial_iterative(9)
    expected = 362880
    assert actual == expected
    #=======================

def test_clumsy_1():
    actual = clumsy(10)
    expected = 12
    assert actual == expected
    #
def test_clumsy_2():
    actual = clumsy(25)
    expected = 27
    assert actual == expected
    #
def test_clumsy_3():
    actual = clumsy(34)
    expected = 36
    assert actual == expected
    #
def test_clumsy_4():
    actual = clumsy(17)
    expected = 19
    assert actual == expected
    #
def test_clumsy_5():
    actual = clumsy(82)
    expected = 84
    assert actual == expected
    #