from pytest import mark
from pytest import raises
from Exercises.EX_03_factorial import factorial


@mark.parametrize(
    'args, result, assertion', [
        (7, 5040, "General Case"),
        (1, 1, 'General case'),
        (9, 362880, 'General Case'),
        (2, 2, 'General Case')
    ]
)
def test_params(args, result, assertion):
    assert factorial(args) == result, assertion


@ mark.parametrize(
    'args, result, assertion', [
        ("hello", raises(TypeError), 'String')
    ]
)
def test_exception(args, result, assertion):
    with raises(TypeError):
        assert factorial(args) == result, assertion
