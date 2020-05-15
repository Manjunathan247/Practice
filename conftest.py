import pytest

credentials = ['user1,pwd1', 'user2,pwd2', 'user3,pwd3', 'user4,pwd4']


@pytest.fixture(params=credentials)
def data_paramerization(request):
    return request.param
