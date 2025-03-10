import pytest
from selenium import webdriver
from pages.create_account_pages import CreateAccount
from pages.eco_friendly_pages import EcoFriendlyPage
from pages.sale_pages import SalePage
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(10)


@pytest.fixture()
def create_acc_page(driver):
    return CreateAccount(driver)

@pytest.fixture()
def create_eco_friendly_page(driver):
    return EcoFriendlyPage(driver)

@pytest.fixture()
def create_sale_page(driver):
    return SalePage(driver)