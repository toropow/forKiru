import pytest

@pytest.fixture(scope='class')
def fix_my_test():
    print('HELLO')

@pytest.yield_fixture()
def fix_my_fixture():
    print('Priver Kiru')
    yield
    print('Poka Kiru')