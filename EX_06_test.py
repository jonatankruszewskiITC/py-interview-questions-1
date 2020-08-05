from pytest import mark
from pytest import raises
from Exercises.EX_06_MineSweeper import num_grid


@ mark.parametrize(
    'args, result, assertion', [
        (
            [
                ["-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-"],
                ["-", "-", "#", "-", "-"],
                ["-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-"]
            ], [
                ["0", "0", "0", "0", "0"],
                ["0", "1", "1", "1", "0"],
                ["0", "1", "#", "1", "0"],
                ["0", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0"]
            ], 'General Case'),
        (
            [
                ["-", "-", "-", "-", "#"],
                ["-", "-", "-", "-", "-"],
                ["-", "-", "#", "-", "-"],
                ["-", "-", "-", "-", "-"],
                ["#", "-", "-", "-", "-"]
            ], [
                ["0", "0", "0", "1", "#"],
                ["0", "1", "1", "2", "1"],
                ["0", "1", "#", "1", "0"],
                ["1", "2", "1", "1", "0"],
                ["#", "1", "0", "0", "0"]
            ], 'General Case'),
        (
            [
                ["-", "-", "-", "#", "#"],
                ["-", "#", "-", "-", "-"],
                ["-", "-", "#", "-", "-"],
                ["-", "#", "#", "-", "-"],
                ["-", "-", "-", "-", "-"]
            ], [
                ["1", "1", "2", "#", "#"],
                ["1", "#", "3", "3", "2"],
                ["2", "4", "#", "2", "0"],
                ["1", "#", "#", "2", "0"],
                ["1", "2", "2", "1", "0"],
            ], 'General Case')
    ]
)
def test_params(args, result, assertion):
    assert num_grid(args) == result, assertion


@ mark.parametrize(
    'args, result, assertion', [
        (5, raises(TypeError), 'Int Type Eror'),
    ]
)
def test_exception(args, result, assertion):
    with raises(TypeError):
        assert num_grid(args) == result, assertion
