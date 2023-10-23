from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/chromedriver')

def open_browser(IP): # OPEN NAVIGATOR MAXIMIZED AFTER INSERT IP
    IP = IP
    driver.get(f"http://{IP}")
    driver.maximize_window() 
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'buttonPcm'))
        ).click()

def web_0x38(): # Fixed colour FIRST ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffffff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x39(): # Fixed colour FIRST ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffffff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x3A(): # Fixed colour FIRST ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffffff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x3B():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x3C():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x3D():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x3E():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x3F():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x30(): # Fixed colour SECOND ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffc800")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x31(): # Fixed colour SECOND ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffc800")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x32(): # Fixed colour SECOND ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffc800")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x33():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x34():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x35():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x36():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x37():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x28(): # Fixed colour THIRD ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffa000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x29(): # Fixed colour THIRD ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffa000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x2A(): # Fixed colour THIRD ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ffa000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x2B():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x2C():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x2D():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x2E():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'p40o')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x2F():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x20(): # Fixed colour FOURTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ff0000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x21(): # Fixed colour FOURTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ff0000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x22(): # Fixed colour FOURTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ff0000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x23():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x24():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x25():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x26():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'p30o')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x27():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x18(): # Fixed colour FIFTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ff00ff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x19(): # Fixed colour FIFTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ff00ff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x1A(): # Fixed colour FIFTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#ff00ff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x1B():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x1C():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x1D():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x1E():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x1F():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x10(): # Fixed colour SIXTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#00ffc8")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x11(): # Fixed colour SIXTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#00ffc8")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x12(): # Fixed colour SIXTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#00ffc8")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x13():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x14():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x15():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x16():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x17():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x08(): # Fixed colour SEVENTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#0000ff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x09(): # Fixed colour SEVENTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#0000ff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x0A(): # Fixed colour SEVENTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#0000ff")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x0B():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x0C():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x0D():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x0E():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x0F():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x00(): # Fixed colour EIGHTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#08ff00")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x01(): # Fixed colour EIGHTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#08ff00")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x02(): # Fixed colour EIGHTH ROW
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#08ff00")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x03():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'p10o')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x04():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x05():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x06():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x07():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")
# The user interface buttons on the periphery below the selection buttons turn off the lights (black color)
def web_0x64(): # black color
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(0)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#000000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x65(): # black color
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(1)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#000000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")

def web_0x66(): # black color
    element1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//button[@onclick="selectSlot(2)"]'))
    )
    if element1:
        element1.click()
        print("Item found ")
    else:
        print("First item not found")
    element2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//div[@onclick=\'pC("#000000")\']'))
    )
    if element2:
        element2.click()
        print("Item found + clic")
    else:
        print("Second item not found")
# These 13 buttons (small buttons) on the periphery are mapped in the same way as the 50 pad buttons to change the recorded effect.
def web_0x67(): 
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x68():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x69():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x6A():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'p20o')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x6B():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x70():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x71():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x72():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x73():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x74():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x75():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x76():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'pXXo')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x77():
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'p50o')) #pXXo XX = number of you efect
    )
    if "XXXXX" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x7A(): # ON/OFF lights (shift button have no led ligth)
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'buttonPower'))
    )
    if "Power" in element.text: # XXXXX = name of you efect
        element.click()
        print("Item found")
    else:
        print("Item not found")

def web_0x48(fader,value): # Handling absolute brightness 0-100 (bad performance, not recommended, the communication between the midi signal and the webdriver is delayed. Just to adjust the brightness and leave it fixed.)
    print('Fader', fader, ' moved to value:', value)
    # Transform midi range (0-127) to the value to a range of 1-255 from HTML
    value = int(((value - 1) / (127 - 1)) * (255 - 1) + 1)
    move_js = 'document.getElementById("sliderBri").value = {};'.format(value)
    driver.execute_script(move_js)
    action_js = 'document.getElementById("sliderBri").onchange(); document.getElementById("sliderBri").oninput();'
    driver.execute_script(action_js)

def web_0x49(fader,value): # 4-stage brightness control 0-25-50-100
    print('Fader', fader, ' moved to value:', value)
    if value <= 32:
        value = 1
    elif value <= 64:
        value = 85
    elif value <= 96:
        value = 170
    else:
        value = 255
    move_js = 'document.getElementById("sliderBri").value = {};'.format(value)
    driver.execute_script(move_js)
    action_js = 'document.getElementById("sliderBri").onchange(); document.getElementById("sliderBri").oninput();'
    driver.execute_script(action_js)

def web_0x50(fader,value):
    print('Fader ', fader, ' moved to value:', value)

def web_0x51(fader,value):
    print('Fader ', fader, ' moved to value:', value)

def web_0x52(fader,value):
    print('Fader ', fader, ' moved to value:', value)

def web_0x53(fader,value):
    print('Fader ', fader, ' moved to value:', value)

def web_0x54(fader,value):
    print('Fader ', fader, ' moved to value:', value)

def web_0x55(fader,value):
    print('Fader ', fader, ' moved to value:', value)

def web_0x56(fader,value): # Handling all-or-nothing brightness 0-100
    print('Fader', fader, ' moved to value:', value)
    # We omit all values except MIN-MAX (to improve fader performance).
    if value <= 1:
        value = 1
    else:
        value = 200
    move_js = 'document.getElementById("sliderBri").value = {};'.format(value)
    driver.execute_script(move_js)
    action_js = 'document.getElementById("sliderBri").onchange(); document.getElementById("sliderBri").oninput();'
    driver.execute_script(action_js)

