from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
import logging
import random
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
class ShopAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://practice.automationtesting.in/shop/")
#scenario1
    def apply_price_filter(self):
        # Apply filter for price between 200 to 400
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='woocommerce_price_filter-2']")))

        #slider max and min point sliders
        min_slider = self.driver.find_element(By.XPATH, "//*[@id='woocommerce_price_filter-2']/form/div/div[1]/span[1]")
        max_slider = self.driver.find_element(By.XPATH, "//*[@id='woocommerce_price_filter-2']/form/div/div[1]/span[2]")
        #ActionChains to perform slider
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(min_slider, 29, 0).perform()
        action.drag_and_drop_by_offset(max_slider, -57, 0).perform()
        self.driver.find_element(By.XPATH, "//*[@id='woocommerce_price_filter-2']/form/div/div[2]/button").click()
        #verifying either it is filtered or not--- by checking the price values
        updatedPrice = self.driver.find_element(By.XPATH, "//*[@id='woocommerce_price_filter-2']/form/div/div[2]/div[1]").text

        #Removing "Price: ₹", " — ", "₹"
        updatedPrice = updatedPrice.replace("Price: ₹", "")
        price_range = updatedPrice.split(" — ")

        min_Price = int(price_range[0].replace("₹", "").strip())
        max_Price = int(price_range[1].replace("₹", "").strip())
        if 200 <= min_Price and 400 >= max_Price:
            logging.info("Filetered from the range of ₹200 to ₹405")
            self.driver.find_element(By.XPATH, "//*[@id='woocommerce_price_filter-2']/form/div/div[2]/button").click()

        else:
            logging.warning("Not filtered as per the expected")
#scenario2
    def select_item_and_add_to_cart(self):
        # Iterate through the search results and selecting an item
        items = self.driver.find_elements(By.XPATH, "//*[@id='content']/ul/li")

        for _ in items:
            if len(items) > 0: # Check if items are present
 # Re-fetch items to avoid stale reference after DOM changes
                items = driver.find_elements(By.XPATH, "//*[@id='content']/ul/li")
 
                random_item = random.choice(items) 
                random_item.click() # Click the random item
                time.sleep(3) 
                
 # Print the current page title
                logging.info("Current Page Title: %s", {self.driver.title})

 # Break after handling one item
                break
            else:
                print("No items found on the page.")

#scenarioe3
    def update_cart_and_checkout(self):
        # Go to the cart
        cart_Btn = WebDriverWait(self.driver, 10).until(
 EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to basket']"))
)
        cart_Btn.click() # Click cart button
        time.sleep(2)
        # Increase quantity
        quantity_box = self.driver.find_element(By.XPATH, "//input[@title='Qty']")
        quantity_box.clear()
        quantity_box.send_keys(3)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Add to basket']").click() #updating the cart by clicking cart button
        cart_value = self.driver.find_element(By.XPATH, "//span[@class='cartcontents']")
        cart_value_text = cart_value.text
        if "0" in cart_value_text:
            logging.info("Cart is empty") 
        else:
            logging.warning("Items are added to the cart")
        # Proceed to checkout
        cart_value = self.driver.find_element(By.XPATH, "//span[@class='cartcontents']")
        cart_value.click() # Click cart button
        checkout_Btn = WebDriverWait(self.driver,10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Proceed to Checkout']")))
        checkout_Btn.click()
        time.sleep(2)
        
#Scenario4
    def fill_billing_details_and_payment(self):
        # Fill billing details (dummy data)
        self.driver.find_element(By.ID, "billing_first_name").send_keys("priya")
        self.driver.find_element(By.ID, "billing_last_name").send_keys("D")
        self.driver.find_element(By.ID, "billing_email").send_keys("priya.d@gmail.com")
        self.driver.find_element(By.ID, "billing_phone").send_keys("9234567890")
        self.driver.find_element(By.ID, "billing_address_1").send_keys("123 Main St")
        self.driver.find_element(By.ID, "billing_city").send_keys("hyderabad")
        self.driver.find_element(By.ID, "billing_postcode").send_keys("523232")
        
        # Select payment method (dummy payment)
        self.driver.find_element(By.ID, "payment_method_cod").click()  # COD (Cash on Delivery) for dummy payment
        self.driver.find_element(By.ID, "place_order").click()
        logging.info("Payment Details entered successfully...")
        time.sleep(2)

    def capture_success_message(self):
        # Capture the success message
        success_message = self.driver.find_element(By.CLASS_NAME, "woocommerce-thankyou-order-received").text
        logging.info("Order Success Message: %s", {success_message})


# Running the script

if __name__ == "__main__":
    # Initialize the WebDriver (Assuming Chrome is used here)
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        shop = ShopAutomation(driver)
        shop.apply_price_filter()
        shop.select_item_and_add_to_cart()
        shop.update_cart_and_checkout()
        shop.fill_billing_details_and_payment()
        shop.capture_success_message()
    finally:
        driver.quit()
