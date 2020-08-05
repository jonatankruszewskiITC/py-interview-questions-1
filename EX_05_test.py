from pytest import mark
from pytest import raises
from Exercises.EX_05_split import split


@ mark.parametrize(
    'args, result, assertion', [
        ("()()()", ["()", "()", "()"], 'General Case'),
        ("", [], 'General Case'),
        ("()()(())", ["()", "()", "(())"], 'General Case'),
        ("(())(())", ["(())", "(())"], 'General Case'),
        ("((()))", ["((()))"], 'General Case'),
        ("()(((((((((())))))))))", [
         "()", "(((((((((())))))))))"], 'General Case'),
        ("((())()(()))(()(())())(()())", [
         "((())()(()))", "(()(())())", "(()())"], 'General Case'),
        ("((()))(())()()(()())", ["((()))", "(())",
                                  "()", "()", "(()())"], 'General Case'),
        ("((())())(()(()()))", ["((())())", "(()(()()))"], 'General Case'),
        ("(()(()()))()(((()))()(()))(()((()))(())())", [
         "(()(()()))", "()", "(((()))()(()))", "(()((()))(())())"], 'General Case')
    ]
)
def test_params(args, result, assertion):
    assert split(args) == result, assertion


@ mark.parametrize(
    'args, result, assertion', [
        (5, raises(TypeError), 'Int Type Eror'),
    ]
)
def test_exception(args, result, assertion):
    with raises(TypeError):
        assert split(args) == result, assertion
