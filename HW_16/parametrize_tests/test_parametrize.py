import pytest


@pytest.mark.param
@pytest.mark.parametrize('lang', ['python', 'java', 'c#', 'c++'])
def test_solo_value(lang, function_fixture):
    print(f'\nLanguage {lang}')
    assert True


@pytest.mark.param
@pytest.mark.parametrize('country, capital', [('Ukraine', 'Kyiv'), ('Poland', 'Wrozlaw'), ('Germany', 'Berlin')])
def test_pairs_value(country, capital, function_fixture):
    print(f'\n{capital} is the capital of {country}')
    assert True


@pytest.mark.param
@pytest.mark.parametrize('val1, val2', [(1, ['a', 'b', 'c']), (1, 1.453), ({'a', 'b', 'c'}, True)],
                         ids=['int and list', 'int and float', 'set and bool'])
def test_info(val1, val2, function_fixture):
    assert True
