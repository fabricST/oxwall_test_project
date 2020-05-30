import time
from oxwall_home_work.oxwall_helper import OxwallHelper


def test_add_comment(driver):
    app = OxwallHelper(driver)
    app.login(username='fabric', password='pass')
    app.create_post(text='dsfsd')
    time.sleep(2)
    app.add_comment(text="comment from param")
    time.sleep(2)
    app.logout()
