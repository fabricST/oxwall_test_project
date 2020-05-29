import time
from Class_work.oxwall_helper import OxwallHelper


def test_create_status(driver):
    app = OxwallHelper(driver)
    app.login()
    time.sleep(5)
    count_of_post = len(app.get_posts())
    app.create_post()
    results = app.wait_new_post_appears(count_of_post+1)
    app.add_post_with_photo()
    app.logout()
