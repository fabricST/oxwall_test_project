class presence_of_elements:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        print("new try")
        els = driver.find_elements(*self.locator)
        if len(els) == self.number:
            return els


class presence_of_elements_more_then:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        print("new try")
        els = driver.find_elements(*self.locator)
        if len(els) > self.number:
            return els

