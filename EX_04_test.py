from pytest import mark
from pytest import raises
from Exercises.EX_04_flip_list import flip_list


@ mark.parametrize(
    'args, result, assertion', [
        ([1, 2, 3, 4], [[1], [2], [3], [4]],  "General Case"),
        ([[5], [6], [9]], [5, 6, 9], "General Case"),
        ([[7], [8], [9], [55]], [7, 8, 9, 55], "General Case"),
        ([7, 8, 9, 55], [[7], [8], [9], [55]], "General Case"),
        ([[1], [2]], [1, 2], "General Case"),
        ([5, 8], [[5], [8]], "General Case"),
        ([2], [[2]], "General Case"),
        ([], [], "General Case"),
        ('hello', [['h'], ['e'], ['l'], ['l'], ['o']], 'String')
    ]
)
def test_params(args, result, assertion):
    assert flip_list(args) == result, assertion


@ mark.parametrize(
    'args, result, assertion', [
        (5, raises(TypeError), 'Int Type Eror')
    ]
)
def test_exception(args, result, assertion):
    with raises(TypeError):
        assert flip_list(args) == result, assertion
