import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MetaMask:
    def __init__(self, mnemonic_string, wallet_pwd):
        self.mnemonic_string = mnemonic_string
        self.wallet_pwd = wallet_pwd
        self.driver = None
    
    def initialize_driver(self):
        chop = webdriver.ChromeOptions()
        chop.add_extension("MetaMask.crx")
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chop)
    
    def find_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)
    
    def sign_in(self, is_rinkeby):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(0.5)
        
        self.find_element('//*[@id="app-content"]/div/div[3]/div/div/div/button').click()
        print('Meta clicked')
        time.sleep(1)
        
        self.find_element(
            '//*[@id="app-content"]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button').click()
        
        self.find_element(
            '//*[@id="app-content"]/div/div[3]/div/div/div/div[5]/div[1]/footer/button[1]').click()
        time.sleep(1)
        
        mnemonic_input = self.find_element(
            '//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input')
        mnemonic_input.send_keys(self.mnemonic_string)
        
        pwd1_input = self.find_element('//*[@id="password"]')
        pwd1_input.send_keys(self.wallet_pwd)
        
        pwd2_input = self.find_element('//*[@id="confirm-password"]')
        pwd2_input.send_keys(self.wallet_pwd)
        
        checkbox = self.find_element('//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div')
        checkbox.click()
        
        submit = self.find_element('//*[@id="app-content"]/div/div[3]/div/div/form/button')
        submit.click()
        time.sleep(1.5)
        
        alldone = self.find_element('//*[@id="app-content"]/div/div[3]/div/div/button')
        alldone.click()
        time.sleep(1)
        
        xmodal = self.find_element('//*[@id="popover-content"]/div/div/section/header/div/button')
        xmodal.click()
        time.sleep(0.1)
        
        if is_rinkeby:
            network = self.find_element('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div')
            network.click()
            time.sleep(0.1)
            
            network_rinkeby = self.find_element('//*[@id="app-content"]/div/div[3]/div/li[4]')
            network_rinkeby.click()
    
    def close(self):
        self.driver.quit()


class OpenSea:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def initialize_driver(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)
    
    def find_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)
    
    def create_page(self):
        url = 'https://opensea.io/asset/create'
        self.driver.get(url)
        time.sleep(0.5)
    
    def upload_files(self, image_path, nm, coll_name):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="media"]')))
        image_upload = self.find_element('//*[@id="media"]')
        image_upload.send_keys(image_path)
        
        name = self.find_element('//*[@id="name"]')
        name.send_keys(nm)
        
        description = self.find_element('//*[@id="description"]')
        description.send_keys("NFT description")
        
        time.sleep(0.2)
        
        collection_name = self.find_element('//*[@id="collection"]')
        collection_name.send_keys(coll_name)
        
        collection_button_from_list_name = '//button[normalize-space()="{}"]'.format(coll_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, collection_button_from_list_name)))
        collection_button_from_list = self.find_element(collection_button_from_list_name)
        collection_button_from_list.click()
        
        time.sleep(0.1)
        
        properties_plus_button = self.find_element(
            '//*[@id="main"]/div/div/section/div/form/section/div[1]/div/div[2]/button/div/i')
        properties_plus_button.click()
        print('Starting properties population')
        time.sleep(1.6)
        
        for i in range(1, 7):  # Modify this part accordingly
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add more"]')))
            collection_add_prop_button = self.find_element('//button[normalize-space()="Add more"]')
            collection_add_prop_button.click()
            
            type_string = '/html/body/div[2]/div/div/div/section/table/tbody/tr[{}]/td[1]/div/div/input'.format(str(i))
            n_type = self.find_element(type_string)
            n_type.send_keys("test type {}".format(str(i)))
            
            name_string = '/html/body/div[2]/div/div/div/section/table/tbody/tr[{}]/td[2]/div/div/input'.format(str(i))
            n_name = self.find_element(name_string)
            n_name.send_keys("test name {}".format(str(i)))
        
        save_btn = '//button[normalize-space()="{}"]'.format("Save")
        save = self.find_element(save_btn)
        save.click()
        
        blockchain_button = self.find_element(
            '//*[@id="__next"]/div[1]/main/div/div/section/div/form/div[7]/div/div[2]')
        blockchain_button.click()
        
        polygon_button_location = '//span[normalize-space() = "Polygon"]'
        self.wait.until(EC.presence_of_element_located((By.XPATH, polygon_button_location)))
        polygon_button = self.find_element(By.XPATH, polygon_button_location)
        polygon_button.click()
        
        create_nft = self.find_element(
            '//*[@id="__next"]/div[1]/main/div/div/section/div/form/div/div[1]/span/button')
        create_nft.click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "i[aria-label='Close']")))
        cross = self.find_element_by_css_selector("i[aria-label='Close']")
        cross.click()
        time.sleep(1)
    
    def sell_nft(self):
        main_page = self.driver.current_window_handle
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div[1]/div/span[2]/a')))
        sell = self.find_element('//*[@id="__next"]/div[1]/main/div/div/div[1]/div/span[2]/a')
        sell.click()
        
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Amount']")))
        amount = self.find_element_by_css_selector("input[placeholder='Amount']")
        amount.send_keys(str(0.555))
        
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        listing = self.find_element_by_css_selector("button[type='submit']")
        listing.click()
        time.sleep(5)
        
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb fzwDgL']")))
        sell_sign = self.find_element_by_css_selector(
            "button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb fzwDgL']")
        sell_sign.click()
        time.sleep(2)
        
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[2])
        print(tabs)
        
        sign_meta = self.find_element('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]')
        sign_meta.click()
        time.sleep(2)
        
        self.driver.switch_to.window(tabs[1])
        time.sleep(2)
    
    def close(self):
        self.driver.quit()


def main():
    mnemonic_string = "wallet keyphrase"
    wallet_pwd = "metamask password"
    coll_name = "Bad mouthing punks v1"
    img_path = r".\images\\"
    
    meta_mask = MetaMask(mnemonic_string, wallet_pwd)
    meta_mask.initialize_driver()
    meta_mask.sign_in(False)
    
    open_sea = OpenSea()
    open_sea.initialize_driver()
    
    open_sea.create_page()
    
    files = os.listdir(img_path)
    for file in files:
        open_sea.upload_files(img_path + file, file, coll_name)
        open_sea.sell_nft()
        open_sea.create_page()
    
    open_sea.close()
    meta_mask.close()


if __name__ == "__main__":
    main()
