from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class TataElxsi:
    def __init__(self, driver): 
        self.driver = driver
        self.driver.get("https://www.tataelxsi.com/")
        
    def check_logo_functionality(self):
        # Check left and right logos in the header
                driver.find_element(By.CLASS_NAME, "cookesalow").click()
                logos = [
            {"name": "Left Logo", "xpath": "//div[@class='logo']", },
            {"name": "Right Logo", "xpath": "//div[@class='tatal']", }
        ]
        #header
                for logo in logos:
                        try:
                                logo_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, logo["xpath"])))
                
                                if logo_element.is_displayed() and logo_element.is_enabled():
                                        print(f"{logo['name']} is clickable...")
                                else:
                                        print(f"{logo['name']} is not clickable...")
                        except Exception as e:
                                print(f"Error with {logo['name']}: {str(e)}")
                #footer
                footer_logo_xpath = driver.find_element(By.XPATH, "//div[@class='flogo1 hdani1']//a")
                driver.execute_script("arguments[0].scrollIntoView();",footer_logo_xpath)
                time.sleep(5)
                if footer_logo_xpath.is_displayed() and footer_logo_xpath.is_enabled():
                        print("footer is clickable")
                else:
                        print("footer is not clickable...")
                
    def check_select_language_dropdown(self):
        driver.find_element(By.XPATH, "//*[@id='content']/div[3]/a/div/img").click()
        time.sleep(5)
        # Click on the 'Select Language' dropdown and check the options
        language_dropdown = self.driver.find_element(By.XPATH, "//select[@class='goog-te-combo']")
        dropdown_selection =Select(language_dropdown)
        all_options =dropdown_selection.options
        for all_option_avail in all_options:
             print(all_option_avail.text)
        time.sleep(2)
        
    def click_ai_menu_and_display_title(self):
        # Click on the "AI" submenu under "Design Digital"
        menu = self.driver.find_element(By.XPATH, "//a[text()='menu']")
        menu.click()
        time.sleep(1)
        
        ai_submenu = self.driver.find_element(By.XPATH, "//div[@class='dmnud2']//div[1]//ul[1]//li[4]//a[1]")
        ai_submenu.click()
        time.sleep(2)
        
        # Print the page title
        print(f"Page title after clicking AI: {self.driver.title}")
        
    def check_social_icons(self):
        # Check if all social media icons are clickable
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        social_icons = self.driver.find_elements(By.XPATH, "//ul[@class='socials lani1']//a")
        print(f"Total social icons: {len(social_icons)}")
        
        for icon in social_icons:
            try:
                if icon.is_displayed() and icon.is_enabled():
                    icon.click()
                    time.sleep(2)
                    print(f"Clicked social icon with URL: {self.driver.current_url}")
                    self.driver.back()  # Go back to homepage
                    time.sleep(2)
            except Exception as e:
                print(f"Error with social icon: {str(e)}")
                
    def validate_footer_links(self):
    # Validate if footer links are clickable
        footer_links = self.driver.find_elements(By.XPATH, "//footer//a")
        for link in footer_links:
                try:
                        if link.is_displayed() and link.is_enabled():
                                print(f"Link '{link.text}' is clickable.")
                        else:
                                print(f"Link '{link.text}' is not clickable.")
                except Exception as e:
                        print(f"Error with footer link '{link.text}': {str(e)}")

                
    def click_get_in_touch_button(self):
        # Click on the "GET IN TOUCH" floating button
        get_in_touch_button = self.driver.find_element(By.XPATH, "//*[@class='chatmsg9 desks9']")
        get_in_touch_button.click()
        time.sleep(2)
        
        # Print section title and sub-text
        section_title = self.driver.find_element(By.XPATH, "//h1[text()='Get in touch']").text
        sub_text = self.driver.find_element(By.XPATH, "//p[contains(text(),'contact you')]").text
        print(f"Section Title: {section_title}")
        print(f"Sub Text: {sub_text}")
        
    def validate_search_functionality(self):
        # Validate search functionality
        search_box = self.driver.find_element(By.XPATH, "//input[@class='srchtxt']")
        search_box.click()
        search_box.send_keys("Text")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        
        # Check if results are displaying
        results = self.driver.find_elements(By.XPATH, "//div[@class='srch-rslts']")
        if results:
            print(f"Found {len(results)} search result(s).")
        else:
            print("No search results found.")
        
    def validate_broken_links(self):
    # Validate broken links on the homepage
        self.driver.find_element(By.XPATH, "//div[@class='logo']").click()
        time.sleep(2)
        links = self.driver.find_elements(By.XPATH, "//a[@href]")  # Re-fetching the links after the action
        broken_links = []
    
        for link in links:
                try:
                # Re-locate each link element before interacting with it
                        url = link.get_attribute("href")
                        if url and url.startswith("http"):
                                try:
                                        self.driver.get(url)
                                        time.sleep(2)
                                        if "404" in self.driver.title:
                                                broken_links.append(url)
                                except Exception as e:
                                        broken_links.append(url)
                except Exception as e:
                        print(f"Error with link: {str(e)}")
        
        if broken_links:
                print(f"Broken links found: {broken_links}")
        else:
                print("No broken links found.")
        
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        TE = TataElxsi(driver)
        
        # Execute each scenario
        TE.check_logo_functionality()
        TE.check_select_language_dropdown()
        TE.click_ai_menu_and_display_title()
        TE.check_social_icons()
        TE.validate_footer_links()
        TE.click_get_in_touch_button()
        TE.validate_search_functionality()
        TE.validate_broken_links()
        
    finally:
        driver.quit()
