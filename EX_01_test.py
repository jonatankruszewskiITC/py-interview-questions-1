from pytest import mark
from pytest import raises
from Exercises.EX_01_fizz_buzz import fizz_buzz

@mark.parametrize(
    'args, result, assertion', [
        (3, 'Fizz', "General Case"),
        (20, 'Buzz', "General Case"),
        (15, 'FizzBuzz', "General Case"),
        (4, '4', "General Case"),
        (-2, '-2', "General Case"),
    ]
)
def test_params(args, result, assertion):
    assert fizz_buzz(args) == result, assertion


@mark.parametrize(
    'args, result, assertion', [
        ("hello", raises(TypeError), 'String')
    ]
)
def test_exception(args, result, assertion):
    with raises(TypeError):
        assert fizz_buzz(*args) == result, assertion
