import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
#Scenario 1
class Textbox:
    def handle_text_box(self, driver):
        driver.find_element(By.ID, "fname").send_keys("Entering random Text")
        time.sleep(5)
        logging.info("Text entered successfully in the textbox.")
#Scenario 2
class Submit:
    def Button_size(self, driver):
        Submit_Btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
        width=Submit_Btn.size['width']
        height=Submit_Btn.size['height']
        logging.info(f"Button size - Width: {width}, Height: {height}")
        time.sleep(5)

#Scenario 3
class DoubleClick:
    def DoubleClickAlert(self, driver):
        doubleClickBtn = driver.find_element(By.ID, "dblClkBtn")
        DoubleClickAction = ActionChains(driver)
        DoubleClickAction.double_click(doubleClickBtn).perform()
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("Alert Message: " + alert_text)#printing the text of alert message
        time.sleep(5)
        alert.accept()  #accepting the alert

#Scenario 4 
class DropdownAndCheckBox:
    def drpDownAndCheckBox(self, driver):
        driver.find_element(By.XPATH, "//input[@type='radio' and @id='male']").click() #selecting radio Button - Male
        #Handling checkboxes
        checkboxes = driver.find_elements(By.XPATH, "//*[@type = 'checkbox']")
        for checkbox in checkboxes:
            checkbox.click()
        time.sleep(5)
        logging.info("Selected all dropdown values and checkboxes")
#Scenario 5
class DropDownIteration:
    def handle_dropdown_Checkboxes(self, driver):
        #Handling Dropdown
        Testing_dropDown  = driver.find_element(By.ID, "testingDropdown")
        dropDown = Select(Testing_dropDown)
        all_options = dropDown.options
         # get list of options available
        print("All the Drop Down Option: ")
        for options in all_options:
            print(options.text)  
        time.sleep(3)
        dropDown.select_by_visible_text("Manual Testing")
        

#Scenario6
class CancelAndPrintText:
    def cancelBtn_PrintText(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]").click()
        alert = driver.switch_to.alert
        alert.dismiss()
        canceled_text = driver.find_element(By.XPATH, "//p[@id='demo']")
        print(canceled_text.text) #printing the text of canceled message
        logging.info("Canceled message is Printed successfully")

#scenario7
class DragAndDrop:
    def dragAndDrop(self, driver):
        logo_path = driver.find_element(By.XPATH, "//img[@id='myImage']")
        target_loc=driver.find_element(By.XPATH, "//div[@id='targetDiv']")
        action = ActionChains(driver)
        time.sleep(2)
        action.drag_and_drop(logo_path, target_loc).perform()
        time.sleep(2)
        logging.info("Drag and Drop action performed successfully")


# Main Class Inheriting All Scenarios
class MainClass(Textbox, Submit, DoubleClick, DropdownAndCheckBox, DropDownIteration, CancelAndPrintText, DragAndDrop):
    def execute_all(self):
        driver = webdriver.Chrome()  
        driver.get("https://artoftesting.com/samplesiteforselenium")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        try:
            wait.until(EC.presence_of_element_located(By.XPATH, "//a[text()='ArtOfTesting']"))
            logging.info("Page launched successfully")
        except Exception as e:
            logging.error("Page launch Failed: {str(e)}")

        try:
            self.handle_text_box(driver)
            self.Button_size(driver)
            self.DoubleClickAlert(driver)
            self.drpDownAndCheckBox(driver)
            self.handle_dropdown_Checkboxes(driver)
            self.handle_dropdown_Checkboxes(driver)
            self.cancelBtn_PrintText(driver)
            self.dragAndDrop(driver)
        except Exception as e:
            logging.error("Failed to Perform the action: {str(e)}")
        finally:
            driver.quit()
            print("All tasks completed and browser closed")

# Run the Main Class
if __name__ == "__main__":
    main = MainClass()
    main.execute_all()

