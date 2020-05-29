import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Class_work.custom_waits import presence_of_elements


class OxwallHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def login(self):
        # скрипт логирования пользователя
        # frame_element = dr.find_element(By.NAME, "demobody")
        # dr.switch_to.frame(frame_element)
        sing_in = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ow_signin_label')))
        sing_in.click()
        username_email_field = self.driver.find_element(By.CSS_SELECTOR, '.ow_user_name input').send_keys('fabric')
        pass_field = self.driver.find_element(By.CSS_SELECTOR, '.ow_password input').send_keys('pass')
        button_sign_in = self.driver.find_element(By.NAME, 'submit').click()

    def get_posts(self):
        return self.driver.find_elements(By.CLASS_NAME, 'ow_newsfeed_item')

    def create_post(self):
        # написания коментария
        comment_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ow_smallmargin textarea')))
        comment_field.send_keys("test comment123")
        add_comment_button = self.driver.find_element(By.CLASS_NAME, 'ow_attachment_btn input').click()

    def wait_new_post_appears(self, count_of_post):
        return self.wait.until(presence_of_elements((By.CLASS_NAME, "ow_newsfeed_item"), count_of_post),
                          message="the number of post isn't correct")

    def add_post_with_photo(self):
        # Добавить пост с фотографией
        enter_field = self.driver.find_element(By.CSS_SELECTOR, '.ow_smallmargin textarea').click()
        button_attach = self.driver.find_element(By.CSS_SELECTOR, "input.mlt_file_input").send_keys(
            '/Users/fabric/oxwall.jpg')
        self.wait.until(
            EC.invisibility_of_element((By.CSS_SELECTOR, "a.ow_photo_attachment_pic.ow_attachment_preload.loading")))
        add_comment_withphoto_button = self.driver.find_element(By.CLASS_NAME, 'ow_attachment_btn input').click()

    def logout(self):
        time.sleep(2)
        # разлогирование пользователя c ховером
        button_sign_out = self.driver.find_element(By.CSS_SELECTOR,
                                                   '.ow_console_item.ow_console_dropdown.ow_console_dropdown_hover')
        action = self.action.move_to_element(button_sign_out)
        # action
        action.perform()
        button_log_out = self.driver.find_element(By.XPATH, "//li[7]/div/a")
        button_log_out.click()
        self.driver.close()
