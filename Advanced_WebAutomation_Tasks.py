from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

# Scenario 1: Single Frame
class SingleFrame:
    def handle_single_frame(self, driver):
        driver.get("https://demo.automationtesting.in/Frames.html")
        driver.switch_to.frame(driver.find_element(By.ID, "singleframe"))
        text_field = driver.find_element(By.XPATH, "//input[@type='text']")
        text_field.send_keys("Testing Single Frame")
        print("Entered text in single frame successfully")
        driver.switch_to.default_content()

# Scenario 2: Nested Frames
class NestedFrames:
    def handle_nested_frames(self, driver):
        driver.get("https://demo.automationtesting.in/Frames.html")
        driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']"))
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))
        text_field = driver.find_element(By.XPATH, "//input[@type='text']")
        text_field.send_keys("Testing Nested Frame")
        print("Entered text in nested frame successfully")
        driver.switch_to.default_content()

# Scenario 3: File Upload
class FileUpload:
    def handle_file_upload(self, driver):
        driver.get("https://demo.automationtesting.in/FileUpload.html")
        Upload_file = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div[1]/div[3]")             
        file_path = r"C:/Users/27269/Desktop/gitbash.jpg"
        time.sleep(5)
        Upload_file.send_keys(file_path)
        

# Scenario 4: Register Form
class RegisterForm:
    def handle_register_form(self, driver):
        driver.get("https://demo.automationtesting.in/Register.html")
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("priyaa")
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Doe")
        driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys("Main Bazar")
        driver.find_element(By.XPATH, "//*[@type='email']").send_keys("suma.b@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("9876543210")
        driver.find_element(By.XPATH, "//input[@value='FeMale']").click()
        driver.find_element(By.ID, 'checkbox2').click()
        driver.find_element(By.ID, 'checkbox3').click()

        #language drop down
        driver.find_element(By.XPATH, "//div[@id='msdd']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='English']").click()

        #skills dropDown
        skill_drpDown = driver.find_element(By.XPATH, "//select[@id='Skills']")
        drpDown = Select(skill_drpDown)
        drpDown.select_by_visible_text("Python")

        #Country Drop down
        driver.find_element(By.XPATH, "//span[@role='combobox']").click()
        driver.find_element(By.XPATH, "//input[@type='search']").send_keys("India")
        driver.find_element(By.XPATH, "//li[@role='treeitem' and text()='India']").click()

        #DOB
        #year
        year = driver.find_element(By.ID, 'yearbox')
        yr_drpDown = Select(year)
        yr_drpDown.select_by_visible_text("1998")
        #month
        mnth = driver.find_element(By.XPATH, "//select[@placeholder='Month']")
        mnth_drpDown = Select(mnth)
        mnth_drpDown.select_by_index(12)
        #day
        day=driver.find_element(By.ID, "daybox")
        day_drpDown = Select(day)
        day_drpDown.select_by_value("15")

        driver.find_element(By.ID, "firstpassword").send_keys("Devi@9497")
        driver.find_element(By.ID, "secondpassword").send_keys("Devi@9497")
        driver.find_element(By.ID, "submitbtn").click()
        try:
        # Wait for the alert message to appear after form submission
            WebDriverWait(driver, 10).until(EC.alert_is_present())

        # Switch to the alert and capture its text
            alert = Alert(driver)
            alert_message = alert.text
            print(f"Alert Message: {alert_message}")

        # Accept the alert (click OK)
            alert.accept()

        except Exception as e:
            print("No alert found or error handling the alert:", str(e))
            print("Form fields entered successfully")

# Scenario 5: Child Window Handling
class ChildWindow:
    def handle_child_window(self, driver):
        driver.get("https://demo.automationtesting.in/Windows.html")
        driver.find_element(By.XPATH, "//button[@class='btn btn-info' and contains(text(), 'click')]").click()
        parent_window = driver.current_window_handle
        all_windows = driver.window_handles
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                print(f"Child window title: {driver.title}")
                driver.close()
        driver.switch_to.window(parent_window)
        print(f"Parent window title: {driver.title}")

# Main Class Inheriting All Scenarios
class MainClass(SingleFrame, NestedFrames, FileUpload, RegisterForm, ChildWindow):
    def execute_all(self):
        driver = webdriver.Chrome()  # Update path
        driver.maximize_window()

        try:
            self.handle_single_frame(driver)
            self.handle_nested_frames(driver)
            self.handle_file_upload(driver)
            self.handle_register_form(driver)
            self.handle_child_window(driver)
        finally:
            driver.quit()
            print("All tasks completed and browser closed")

# Run the Main Class
if __name__ == "__main__":
    main = MainClass()
    main.execute_all()
    
