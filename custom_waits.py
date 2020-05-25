# def presence_of_elements_more_than_number(locator, number):
#     def method(driver):
#         print("new try")
#         els = driver.find_elements(*locator)
#         if len(els) > number:
#             return els
#
#     return method

class presence_of_elements_more_than_number:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        print("new try")
        els = driver.find_elements(*self.locator)
        if len(els) > self.number:
            return els


if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.expected_conditions import visibility_of_element_located

    dr = webdriver.Chrome()
    dr.get("https://demo.oxwall.com/")

    wait = WebDriverWait(dr, 10)
    results = wait.until(presence_of_elements_more_than_number((By.CLASS_NAME, "ow_newsfeed_item"), 9),
                         message="Less than 9")
    print(len(results))

    dr.save_screenshot("ddfgfd.png")
    # results[0].screenshot("dd_2.png")
    # m = visibility_of_element_located((By.CLASS_NAME, "ow_newsfeed_item"))
    # m(dr)


    # e = wait.until(visibility_of_element_located((By.CLASS_NAME, "ow_newsfeed_item")), message="")

