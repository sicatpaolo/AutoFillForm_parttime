#!usr/bin/python
from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r'D:\Work\Python\chromedriver_win32\chromedriver.exe')
driver.get("https://website.co.uk/#/")

# Create functions

# logging in 

def login(barrier1, email, password, submit):
    time.sleep(5)
    driver.find_element_by_xpath(barrier1).click()
    time.sleep(5)
    driver.find_element_by_xpath(email).send_keys("J.A.Sicat@greenwich.ac.uk")
    driver.find_element_by_xpath(password).send_keys("J.A.Sicat@greenwich.ac.uk")
    driver.find_element_by_xpath(submit).click()
    time.sleep(5)
    
# Fill up general

def auto_general(FertilizerName, Manufacturer, State, pH, Density, NumberofH, BaseDressing):
    time.sleep(5)
    # Textboxes
    driver.find_element_by_xpath(general_Name).send_keys(FertilizerName)

    if Manufacturer != 'Null':
        driver.find_element_by_xpath(general_Manufacturer).send_keys(Manufacturer)

    if pH != 'NULL' or pH == '0':
        driver.find_element_by_xpath(general_pH).send_keys(pH)

    if Density != 'NULL' or Density == '0':
        driver.find_element_by_xpath(general_Density).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(general_Density).send_keys(Density)

    if NumberofH != 'NULL' or NumberofH == '0':
        driver.find_element_by_xpath(general_NumberofH).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(general_NumberofH).send_keys(NumberofH)

    time.sleep(5)

    # Dropdown
    if State == 'SOLID':
        driver.find_element_by_xpath(general_Manufacturer).send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath(general_Solid).click()
    elif State == 'SOLIDCHELATE':
        driver.find_element_by_xpath(general_Manufacturer).send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath(general_SolidChelate).click()
    elif State == 'LIQUIDACID':
        driver.find_element_by_xpath(general_Manufacturer).send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath(general_LiquidAcid).click()
    elif State == 'LIQUID':
        driver.find_element_by_xpath(general_Manufacturer).send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath(general_Liquid).click()
    elif State == 'SOLIDMANURE':
        driver.find_element_by_xpath(general_Manufacturer).send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath(general_SolidManure).click()
        driver.find_element_by_xpath(general_IsManureFertilizer).click()
    elif State == 'LIQUIDMANURE':
        driver.find_element_by_xpath(general_Manufacturer).send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_xpath(general_LiquidManure).click()
        driver.find_element_by_xpath(general_IsManureFertilizer).click()

    # CheckBox
    if BaseDressing == 'TRUE':
        driver.find_element_by_xpath(general_BaseDressing).click()
    time.sleep(5)

# Auto fill solubility

def auto_solubility(sol0, sol5, sol10, sol15, sol20, sol25, sol30):
    if sol0 != 'NULL':
        driver.find_element_by_xpath(sol_0C).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(sol_0C).send_keys(sol0)
    if sol5 != 'NULL':
        driver.find_element_by_xpath(sol_5C).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(sol_5C).send_keys(sol5)
    if sol10 != 'NULL':
        driver.find_element_by_xpath(sol_10C).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(sol_10C).send_keys(sol10)
    if sol15 != 'NULL':
        driver.find_element_by_xpath(sol_15C).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(sol_15C).send_keys(sol15)
    if sol20 != 'NULL':
        driver.find_element_by_xpath(sol_20C).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(sol_20C).send_keys(sol20)
    if sol25 != 'NULL':
        driver.find_element_by_xpath(sol_25C).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(sol_25C).send_keys(sol25)
    if sol30 != 'NULL':
        driver.find_element_by_xpath(sol_30C).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(sol_30C).send_keys(sol30)

# Nutrient Content

def auto_nutrient(nut_NNO3, nut_NNH2, nut_NNH4, nut_P, nut_K, nut_Ca, nut_Mg, nut_S, nut_CO3, nut_HCO3, nut_Cl, nut_Na):
    if nut_NNO3 != 'NULL':
        driver.find_element_by_xpath(Nutrient_NNO3).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_NNO3).send_keys(nut_NNO3)
    if nut_NNH2 != 'NULL':
        driver.find_element_by_xpath(Nutrient_NNH2).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_NNH2).send_keys(nut_NNH2)
    if nut_NNH4 != 'NULL':
        driver.find_element_by_xpath(Nutrient_NNH4).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_NNH4).send_keys(nut_NNH4)
    if nut_P != 'NULL':
        driver.find_element_by_xpath(Nutrient_P).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_P).send_keys(nut_P)
    if nut_K != 'NULL':
        driver.find_element_by_xpath(Nutrient_K).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_K).send_keys(nut_K)
    if nut_Ca != 'NULL':
        driver.find_element_by_xpath(Nutrient_Ca).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_Ca).send_keys(nut_Ca)
    if nut_Mg != 'NULL':
        driver.find_element_by_xpath(Nutrient_Mg).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_Mg).send_keys(nut_Mg)
    if nut_S != 'NULL':
        driver.find_element_by_xpath(Nutrient_S).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_S).send_keys(nut_S)
    if nut_CO3 != 'NULL':
        driver.find_element_by_xpath(Nutrient_CO3).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_CO3).send_keys(nut_CO3)
    if nut_HCO3 != 'NULL':
        driver.find_element_by_xpath(Nutrient_HC03).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_HC03).send_keys(nut_HCO3)
    if nut_Cl != 'NULL':
        driver.find_element_by_xpath(Nutrient_Cl).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_Cl).send_keys(nut_Cl)
    if nut_Na != 'NULL':
        driver.find_element_by_xpath(Nutrient_Na).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Nutrient_Na).send_keys(nut_Na)

# Microelement Content

def auto_microelement(micro_B, micro_Fe, micro_Mn, micro_Zn, micro_Cu, micro_Mo, IsMicroPresent):
    if micro_B != 'NULL':
        driver.find_element_by_xpath(Microelement_B).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Microelement_B).send_keys(micro_B)
    if micro_Fe != 'NULL':
        driver.find_element_by_xpath(Microelement_Fe).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Microelement_Fe).send_keys(micro_Fe)
    if micro_Mn != 'NULL':
        driver.find_element_by_xpath(Microelement_Mn).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Microelement_Mn).send_keys(micro_Mn)
    if micro_Zn != 'NULL':
        driver.find_element_by_xpath(Microelement_Zn).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Microelement_Zn).send_keys(micro_Zn)
    if micro_Cu != 'NULL':
        driver.find_element_by_xpath(Microelement_Cu).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Microelement_Cu).send_keys(micro_Cu)
    if micro_Mo != 'NULL':
        driver.find_element_by_xpath(Microelement_Mo).send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath(Microelement_Mo).send_keys(micro_Mo)
    if IsMicroPresent == 'TRUE':
        driver.find_element_by_xpath(Microelement_Checkbox).click()


# Save Form

def save_form():
    driver.find_element_by_xpath(save_button).click()

    
##############################################################
# Set Location Variables
### Login
first_login_button = '//*[@id="content"]/h2/a'
username_input = '//*[@id="content"]/form/div[1]/div/input'
password_input = '//*[@id="content"]/form/div[2]/div/input'
login_button = '//*[@id="content"]/form/button/span[2]'
save_button = '//*[@id="main"]/div/div/button/span[2]'

### Text Boxes
general_Name = '//*[@id="main"]/div/div/div[1]/div[1]/div/div/input'
general_Manufacturer = '//*[@id="main"]/div/div/div[1]/div[2]/div/div/input'
general_pH = '//*[@id="main"]/div/div/div[1]/div[4]/div/div/input'
general_Density = '//*[@id="main"]/div/div/div[1]/div[5]/div/div/input'
general_MinTemperature = '//*[@id="main"]/div/div/div[1]/div[6]/div/div/input'
general_NumberofH = '//*[@id="main"]/div/div/div[1]/div[7]/div/div/input'

### Dropdown
general_accessState = '/html/body/div[1]/ul[1]'
general_Solid = '/html/body/div[1]/ul[1]/li[1]/button/span'
general_SolidChelate = '/html/body/div[1]/ul[1]/li[2]/button/span'
general_LiquidAcid = '/html/body/div[1]/ul[1]/li[3]/button/span'
general_Liquid = '/html/body/div[1]/ul[1]/li[4]/button/span'
general_SolidManure = '/html/body/div[1]/ul[1]/li[5]/button/span'
general_LiquidManure = '/html/body/div[1]/ul[1]/li[6]/button/span'

### CheckBox
general_BaseDressing = '//*[@id="main"]/div/div/div[2]/div[3]/div/input'
general_IsManureFertilizer = '//*[@id="main"]/div/div/div[2]/div[7]/div/input'

# Solubility
sol_0C = '//*[@id="main"]/div/div/div[3]/div[1]/div/div/input'
sol_5C = '//*[@id="main"]/div/div/div[3]/div[2]/div/div/input'
sol_10C = '//*[@id="main"]/div/div/div[3]/div[3]/div/div/input'
sol_15C = '//*[@id="main"]/div/div/div[3]/div[4]/div/div/input'
sol_20C = '//*[@id="main"]/div/div/div[3]/div[5]/div/div/input'
sol_25C = '//*[@id="main"]/div/div/div[3]/div[6]/div/div/input'
sol_30C = '//*[@id="main"]/div/div/div[3]/div[7]/div/div/input'

# Nutrient Content
Nutrient_NNO3 = '//*[@id="main"]/div/div/div[4]/div[2]/div[2]/div/input'
Nutrient_NNH2 = '//*[@id="main"]/div/div/div[4]/div[3]/div[2]/div/input'
Nutrient_NNH4 = '//*[@id="main"]/div/div/div[4]/div[4]/div[2]/div/input'
Nutrient_P = '//*[@id="main"]/div/div/div[4]/div[5]/div[2]/div/input'
Nutrient_K = '//*[@id="main"]/div/div/div[4]/div[6]/div[2]/div/input'
Nutrient_Ca = '//*[@id="main"]/div/div/div[4]/div[7]/div[2]/div/input'
Nutrient_Mg = '//*[@id="main"]/div/div/div[4]/div[8]/div[2]/div/input'
Nutrient_S = '//*[@id="main"]/div/div/div[4]/div[9]/div[2]/div/input'
Nutrient_CO3 = '//*[@id="main"]/div/div/div[4]/div[10]/div[2]/div/input'
Nutrient_HC03 = '//*[@id="main"]/div/div/div[4]/div[11]/div[2]/div/input'
Nutrient_Cl = '//*[@id="main"]/div/div/div[4]/div[12]/div[2]/div/input'
Nutrient_Na = '//*[@id="main"]/div/div/div[4]/div[13]/div[2]/div/input'

# Microelement
Microelement_Checkbox = '//*[@id="main"]/div/div/div[6]/div/div/input'
Microelement_B = '//*[@id="main"]/div/div/div[7]/div[1]/div/div/input'
Microelement_Fe = '//*[@id="main"]/div/div/div[7]/div[2]/div/div/input'
Microelement_Mn = '//*[@id="main"]/div/div/div[7]/div[3]/div/div/input'
Microelement_Zn = '//*[@id="main"]/div/div/div[7]/div[4]/div/div/input'
Microelement_Cu = '//*[@id="main"]/div/div/div[7]/div[5]/div/div/input'
Microelement_Mo = '//*[@id="main"]/div/div/div[7]/div[6]/div/div/input'

# Login locations
first_login_button = '//*[@id="content"]/h2/a'
username_input = '//*[@id="content"]/form/div[1]/div/input'
password_input = '//*[@id="content"]/form/div[2]/div/input'
login_button = '//*[@id="content"]/form/button/span[2]'
save_button = '//*[@id="main"]/div/div/button/span[2]'
###################################################
# Run commands
# Prep Work
login(first_login_button, username_input, password_input, login_button)
driver.get("https://website.co.uk/#/dashboard/fertilizers/add")

# Loop
with open('701-1000.txt') as tsvfile: # Reminder dont forget Salvatore prefers - to NULL
   fertilizer_file = csv.reader(tsvfile, delimiter='\t')
   for items in fertilizer_file:
       print(items[35])
       auto_general(items[0],items[3],items[1],items[5],items[7],items[6],items[4])
       auto_solubility(items[8], items[9], items[10], items[11], items[12], items[13], items[14])
       auto_nutrient(items[16], items[17], items[18], items[19], items[20], items[21], items[22], items[23], items[24], items[25], items[26], items[27])
       auto_microelement(items[28], items[29], items[30], items[31], items[32], items[33], items[34])
       time.sleep(15) #In case you want to double check. Reduce to 1 after confirmation during trial
       save_form()
       driver.get("https://website.co.uk/#/dashboard/fertilizers/add")
       time.sleep(1)
