import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Class_work.custom_waits import presence_of_elements
from oxwall_home_work.oxwall_helper import OxwallHelper


def test_add_comment(driver):
    app = OxwallHelper(driver)
    app.login(username='fabric', password='pass')
    app.create_post(text='dsfsd')
    time.sleep(2)
    app.add_comment(text="comment from param")
    time.sleep(2)
    app.logout()