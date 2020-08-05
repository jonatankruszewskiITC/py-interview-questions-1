from pytest import mark
from pytest import raises
from Exercises.EX_02_invert_dict import invert


@mark.parametrize(
    'args, result, assertion', [
        ({"a": 1, "b": 2, "c": 3}, {1: "a", 2: "b", 3: "c"}, "General Case"),
        ({"z": "q", "w": "f"}, {"q": "z", "f": "w"}, 'General case'),
        ({"zebra": "koala", "horse": "camel"},
         {"koala": "zebra", "camel": "horse"}, 'General Case')
    ]
)
def test_params(args, result, assertion):
    assert invert(args) == result, assertion


@ mark.parametrize(
    'args, result, assertion', [
        ("hello", raises(TypeError), 'String not being parsed')
    ]
)
def test_exception(args, result, assertion):
    with raises(TypeError):
        assert invert(*args) == result, assertion
