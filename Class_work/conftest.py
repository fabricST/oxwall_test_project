import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    base_url = 'http://localhost:8888/oxwall/'
    dr = webdriver.Chrome(executable_path=r"/Users/fabric/PycharmProjects/chromedriver")
    dr.maximize_window()
    dr.get(base_url)
    return dr


