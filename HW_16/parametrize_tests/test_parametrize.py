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
@pytest.mark.parametrize('name, age, phone', [('Mark', 30, '1234567890'), ('Mishel', 17, '096564523423'),
                                              ('Bob', 54, '14353448345')])
def test_info(name, age, phone, function_fixture):
    print(f'Name: {name}\nAge: {age},\nPhone: {phone}')
    assert True
