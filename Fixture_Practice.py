import pytest


@pytest.fixture
def setup():
    print("Open browser")
    yield
    print("Close browser")


def test_loginpage(setup):
    print("Login Page")
