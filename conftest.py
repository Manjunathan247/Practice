import pytest

credentials = [('user1', 'pwd1'), ('user2', 'pwd2'), ('user3', 'pwd3'), ('user4', 'pwd4')]


@pytest.fixture(params=credentials)
def data_paramerization(request):
    return request.param

#https://stackoverflow.com/questions/43355469/why-use-find-elementby-instead-of-find-element-by
#https://selenium-python.readthedocs.io/locating-elements.html#
#https://www.geeksforgeeks.org/private-methods-in-python/
# https://docs.pytest.org/en/3.0.7/builtin.html
# The request object that can be used from fixture functions.

# class FixtureRequest
# A request for a fixture from a test or fixture function.
# A request object gives access to the requesting test context
# and has an optional param attribute in case the fixture is
# parametrized indirectly.
