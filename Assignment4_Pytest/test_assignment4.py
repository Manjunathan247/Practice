import pytest


class Testdemo:
    def test_cognizant_demo1(self):
        print("test_cognizant_demo1")

    def test_cognizant_demo2(self):
        print("test_cognizant_demo2")

    def test_cognizant_demo3(self):
        print("test_cognizant_demo3")

    def test_method4(self):
        print("test_method4")

    @pytest.mark.smoke
    def test_method5(self):
        print("test_method5")

    @pytest.mark.smoke
    def test_method6(self):
        print("test_method6")

    @pytest.mark.skip
    def test_method7(self):
        print("test_method7")

    def test_method8(self):
        print("test_method8")

    @pytest.mark.xfail
    def test_method9(self):
        print("test_method9")

    def test_method10(self):
        print("test_method10")

# All test cases with verbose and print statements
# pytest -vs

# Test cases with marker as ‘smoke’.
# pytest -vs -m smoke

# Test cases with keyword as ‘cognizant’ in method name
# pytest -vs -k cognizant
