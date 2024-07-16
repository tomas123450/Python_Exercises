import pytest


@pytest.fixture
def setUp():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")


def testAddItemToCart(setUp):
    print("Add Item Succesful")


def testRemoveItemFromCart(setUp):
    print("Remove Item Successful")
