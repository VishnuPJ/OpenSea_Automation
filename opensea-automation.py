import itertools
import os
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ExpectedConditions

def signIntoMeta(driver, wait, isrinkeby, mnemonicString, walletPwd):
    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[0])
    time.sleep(0.5)
    # driver.close()
    # driver.switch_to.window(tabs2[0])
    button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/div/button')
    button.click()
    print('meta clicked')
    time.sleep(1)
    button = driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button')
    button.click()
    button = driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[3]/div/div/div/div[5]/div[1]/footer/button[1]')
    button.click()
    time.sleep(1)
    mnemonicInput = driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input')
    mnemonicInput.send_keys(mnemonicString)
    pwd1Input = driver.find_element_by_xpath('//*[@id="password"]')
    pwd1Input.send_keys(walletPwd)
    pwd2Input = driver.find_element_by_xpath('//*[@id="confirm-password"]')
    pwd2Input.send_keys(walletPwd)
    checkbox = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div')
    checkbox.click()
    submit = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/button')
    submit.click()
    time.sleep(1.5)
    alldone = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button')
    alldone.click()
    time.sleep(1)
    xmodal = driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button')
    xmodal.click()
    time.sleep(0.1)
    if isrinkeby:
        network = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div')
        network.click()
        time.sleep(0.1)
        networkRinkeby = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/li[4]')
        networkRinkeby.click()
    driver.switch_to.window(tabs2[1])
    time.sleep(0.1)
 
    # oswalleticon = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/nav/ul/div[2]/li/button')

    oswalleticon = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div[2]/ul/li[1]/button')
    oswalleticon.click()
    time.sleep(2)

    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[2])
    print(tabs2)

    # metaicon = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/aside/div[2]/div/div[2]/ul/li[1]/button')
    metaicon = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]')
    metaicon.click()
    time.sleep(2)

    # tabs2 = driver.window_handles
    # driver.switch_to.window(tabs2[2])
    # print(tabs2)
    # connectnext = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]')
    connectnext = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]')
    connectnext.click()
    time.sleep(5)

    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[2])
    print(tabs2)

    # connect = driver.find_element_by_xpath(
    #     '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]')

    connect = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]')
    connect.click()
    time.sleep(2)

    print('sign into meta completed')

def uploadFiles(imagePath,nm,collName):
    tabs2 = driver.window_handles
    print('switch tab started')
    driver.switch_to.window(tabs2[1])
    print('switch tab completed')
    time.sleep(2)

    wait.until(ExpectedConditions.presence_of_element_located(
        (By.XPATH, '//*[@id="media"]')))
    imageUpload = driver.find_element_by_xpath('//*[@id="media"]')
    # imageUpload = driver.find_element('// *[ @ id = "main"]/div[2]/div/section/div/form/div[1]/div/div[2]')
    # imagePath = r"D:\NFT\videos\images\unnamed.png"
    imageUpload.send_keys(imagePath)

    name = driver.find_element_by_xpath('//*[@id="name"]')
    name.send_keys(nm)
    description = driver.find_element_by_xpath('//*[@id="description"]')
    description.send_keys("NFT description")
    time.sleep(0.2)

    
    # collectionName = driver.find_element_by_xpath(
    #         '//*[@id="__next"]/div[1]/main/div/div/section/div/form/section[5]/div/input')
    collectionName = driver.find_element_by_xpath('//*[@id="collection"]')
    collectionName.send_keys(collName)
    collectionButtonFromListName = '//button[normalize-space()="{}"]'.format(collName)
    wait.until(ExpectedConditions.presence_of_element_located(
        (By.XPATH, collectionButtonFromListName)))
    collectionButtonFromList = driver.find_element_by_xpath(collectionButtonFromListName)
    collectionButtonFromList.click()
    time.sleep(0.1)


    # propertiesPlusButton = driver.find_element_by_xpath(
        # '//*[@id="main"]/div[2]/div/section/div/form/section/div[1]/div/div[2]/button')
    propertiesPlusButton = driver.find_element_by_xpath('//*[@id="main"]/div/div/section/div/form/section/div[1]/div/div[2]/button/div/i')
    propertiesPlusButton.click()
    print('starting properties population')
    time.sleep(1.6)

    for i in range(1,7):  # Modify this part accordingly
        wait.until(ExpectedConditions.presence_of_element_located(
            (By.XPATH, '//button[normalize-space()="Add more"]')))
        collectionAddPropButton = driver.find_element_by_xpath('//button[normalize-space()="Add more"]')
        collectionAddPropButton.click()

        type_string = '/html/body/div[2]/div/div/div/section/table/tbody/tr[{}]/td[1]/div/div/input'.format(str(i))
        type = driver.find_element_by_xpath(type_string)
        type.send_keys("test type {}".format(str(i)))
        name_string = '/html/body/div[2]/div/div/div/section/table/tbody/tr[{}]/td[2]/div/div/input'.format(str(i))
        name = driver.find_element_by_xpath(name_string)
        name.send_keys("test name {}".format(str(i)))

    save_btn = '//button[normalize-space()="{}"]'.format("Save")
    save = driver.find_element_by_xpath(save_btn)
    save.click()


    blockchain_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div/form/div[7]/div/div[2]')
    blockchain_button.click()

    # blockchain_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div/form/div[8]/div/div[2]/div[2]/i')
    # blockchain_button.click()   

    # blockchain_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div/form/div[8]/div/div[2]')
    # blockchain_button.click()

    polygon_button_location = '//span[normalize-space() = "Polygon"]'
    wait.until(ExpectedConditions.presence_of_element_located(
        (By.XPATH, polygon_button_location)))
    polygon_button = driver.find_element(
        By.XPATH, polygon_button_location)
    polygon_button.click()

    createNFT = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/main/div/div/section/div/form/div/div[1]/span/button')
    createNFT.click()
    wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, "i[aria-label='Close']")))
    cross = driver.find_element_by_css_selector("i[aria-label='Close']")
    cross.click()
    time.sleep(1)


def create_page():
    url = 'https://opensea.io/asset/create'
    driver.get(url)
    time.sleep(0.5)
    wait = WebDriverWait(driver, 60)
    return wait

def sell_nft():
    main_page = driver.current_window_handle
    wait.until(ExpectedConditions.presence_of_element_located(
            (By.XPATH,'//*[@id="__next"]/div[1]/main/div/div/div[1]/div/span[2]/a')))
    sell = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[1]/div/span[2]/a')
    sell.click()


    wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Amount']")))
    amount = driver.find_element_by_css_selector("input[placeholder='Amount']")
    amount.send_keys(str(0.555))

    wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    listing = driver.find_element_by_css_selector("button[type='submit']")
    listing.click()
    time.sleep(5)


    wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, "button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb fzwDgL']")))
    sell_sign = driver.find_element_by_css_selector("button[class='Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb fzwDgL']")
    sell_sign.click()
    time.sleep(2)

    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[2])
    print(tabs2)

    sign_meta = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]')
    sign_meta.click()
    time.sleep(2)

    tabs2 = driver.window_handles
    print('switch tab started')
    driver.switch_to.window(tabs2[1])
    print('switch tab completed')
    time.sleep(2)


chop = webdriver.ChromeOptions()

chop.add_extension("MetaMask.crx")
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chop)
mnemonicString = "wallet keyphrase "
walletPwd = "metamsk password"
wait = create_page()
signIntoMeta(driver, wait, False, mnemonicString, walletPwd)
collName = "Bad mouthing punks v1"
img_pth = r".\images\\"
files = os.listdir(img_pth)
for file in files:

    uploadFiles(img_pth+file,file) #upload
    # time.sleep(10)
    sell_nft()                       #sell
    wait = create_page()             #new
 
