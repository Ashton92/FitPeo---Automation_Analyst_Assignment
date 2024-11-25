import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FitPeoTestPage:
    def __init__(self, driver_path='chromedriver'):
        # Initialize the Chrome WebDriver and WebDriverWait
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def open_homepage(self, url):
        # Open the given URL and adjust initial window size and position
        self.driver.get(url)
        self.driver.set_window_size(1552, 832)
        self.driver.set_window_position(-2, 0)
        time.sleep(1)

    def navigate_to_revenue_calculator(self):
        # Navigate to the Revenue Calculator page by clicking the appropriate link
        try:
            revenue_calculator_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Calculator")))
            revenue_calculator_link.click()
            time.sleep(1)
        except Exception as e:
            print(f"Error navigating to Revenue Calculator: {e}")

    def adjust_window(self, width, height):
        # Adjust the browser window size and position
        try:
            self.driver.set_window_size(width, height)
            self.driver.set_window_position(-2, 0)
            time.sleep(1)
        except Exception as e:
            print(f"Error adjusting window: {e}")

    def scroll_to_slider(self):
        # Scroll the page to the slider section using JavaScript
        try:
            slider_section = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r0:"]')))
            self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });",
                                       slider_section)
            time.sleep(1)
        except Exception as e:
            print(f"Error scrolling to slider: {e}")

    def set_slider_value(self, value_set_to):
        # Set the slider to the desired value by calculating the pixel offset
        try:
            slider_element = self.wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 "(//span[@class='MuiSlider-root MuiSlider-colorPrimary MuiSlider-sizeMedium css-16i48op'])[1]")))
            slider_size = slider_element.size
            slider_width = slider_size['width']
            slider_value_max = 2000

            # Get the current value of the slider
            slider_current_value_element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[@type='number' and contains(@class, 'MuiInputBase-input')]")))
            current_slider_value = int(slider_current_value_element.get_attribute("value"))

            # Calculate the required pixel movement based on the desired value
            slider_set_value = value_set_to - current_slider_value
            pixel_move = (slider_width / slider_value_max) * slider_set_value

            # Move the slider's thumb using the calculated pixel offset
            slider_thumb = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                       "//span[contains(@class,'MuiSlider-thumb MuiSlider-thumbSizeMedium MuiSlider-thumbColorPrimary css-1sfugkh')]")))
            ActionChains(self.driver).drag_and_drop_by_offset(slider_thumb, pixel_move, 0).perform()
            time.sleep(1)
        except Exception as e:
            print(f"Error setting slider value: {e}")

    def input_number(self, number_value):
        # Input a number into the specified field after clearing its existing value
        try:
            input_element = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@type='number' and contains(@class, 'MuiInputBase-input')]")))
            input_element.send_keys(Keys.BACK_SPACE * 4)
            input_element.send_keys(str(number_value))
            time.sleep(1)
        except Exception as e:
            print(f"Error inputting number: {e}")

    def click_checkbox(self, cpt_code, value):
        # Click the checkbox corresponding to the specified CPT code and value
        try:
            checkbox = self.wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 f"//p[text()='{cpt_code}']/following::span[text()='{value}']/preceding::input[@type='checkbox'][1]")))
            self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });",
                                       checkbox)
            checkbox.click()
            time.sleep(1)
        except Exception as e:
            print(f"Error clicking checkbox for {cpt_code}: {e}")

    def validate_total_reimbursement(self):
        # Validate and print the total recurring reimbursement displayed on the page
        try:
            recuring_reimbursement = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//div[@class='MuiBox-root css-m1khva']//p[@class='MuiTypography-root MuiTypography-body1 inter css-12bch19']")))
            print(f"Total Recurring Reimbursement: {recuring_reimbursement.text}")
            time.sleep(1)

            # Validate and print the reimbursement value from the header
            header_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//p[position()=4]//p[position()=1]")))
            print(
                f"Header displaying 'Total Recurring Reimbursement for all Patients Per Month:' shows the value: {header_element.text}, and the expected value is $110700")
            time.sleep(1)
        except Exception as e:
            print(f"Error validating total reimbursement: {e}")

    def close_browser(self):
        # Close the browser
        self.driver.quit()


if __name__ == '__main__':
    # Create an instance of the FitPeoTestPage class and execute the test steps
    test = FitPeoTestPage()

    # Steps of the test
    test.open_homepage("https://www.fitpeo.com/")
    test.navigate_to_revenue_calculator()
    test.adjust_window(412, 915)
    test.scroll_to_slider()
    #time.sleep(2)
    test.set_slider_value(820)
    #time.sleep(2)
    test.adjust_window(1552, 832)
    test.input_number(560)
    #time.sleep(2)
    test.click_checkbox('CPT-99091', '57')
    test.click_checkbox('CPT-99453', '19.19')
    test.click_checkbox('CPT-99454', '63')
    test.click_checkbox('CPT-99474', '15')
    test.validate_total_reimbursement()
    test.close_browser()
