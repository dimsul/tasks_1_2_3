import pytest

from solution import strict


@strict
def squaring(a: int):
    return a * a


@strict
def mult_two(a: float, b: float):
    return a * b


@strict
def sum_four(a: int, b: int, c: float, d: float):
    return a + b + c + d


@strict
def concatenation(a: str, b: str, flip: bool):
    return a + b if not flip else b + a


input_data = ((squaring, (3,), 9),
              (squaring, (5,), 25),
              (mult_two, (4.0, 5.0), 20.0),
              (mult_two, (5.5, 7.3), 40.15),
              (sum_four, (4, 5, 6.1, 9.4), 24.5),
              (sum_four, (5, 7, 5.0, 3.0), 20.0),
              (concatenation, ('first', 'second', False), 'firstsecond'),
              (concatenation, ('first', 'second', True), 'secondfirst'),)


@pytest.mark.parametrize('func, input_, exp_res', input_data)
def test_strict(func, input_, exp_res):
    result = func(*input_)
    assert result == exp_res


input_data = ((squaring, (3.0,)),
              (squaring, (5, 5)),
              (mult_two, (4, 5.0)),
              (mult_two, (5.5, 7)),
              (mult_two, (4, 5.0, 4)),
              (mult_two, (5.5,)),
              (sum_four, (4.0, 6, 9.4),),
              (sum_four, (5.0, 7.0, 5, 3, 4)),
              (concatenation, ('first', 5, False)),
              (concatenation, ('first', 'second', True, 'abc')),)


@pytest.mark.parametrize('func, input_', input_data)
def test_strict_error(func, input_):
    with pytest.raises(TypeError):
        func(*input_)
