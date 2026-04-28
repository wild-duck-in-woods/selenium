from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

options = webdriver.ChromeOptions()
# Instructs Chrome to ignore all SSL/certificate errors
options.add_argument('--ignore-certificate-errors')
# Specifically for handling SSL errors if the first flag isn't enough
options.add_argument('--ignore-ssl-errors=yes')

driver = webdriver.Chrome(options=options)

driver.get("https://www.pvkngcexams.in/IntPosting2025.aspx")

"""
AcadYear = driver.find_element(By.ID, "AcadYear")
select = Select(AcadYear)

# Select options using different methods
select.select_by_value("2025-2028")


Semester = driver.find_element(By.ID, "Semester")
select = Select(Semester)
input("Press Enter after you finish manual actions...")
# Select options using different methods
select.select_by_value("II Semester")


Semester = driver.find_element(By.ID, "Semester")
select = Select(Semester)
# Select options using different methods
select.select_by_value("II Semester")


wait = WebDriverWait(driver, 10)
Exam = wait.until(EC.presence_of_element_located((By.ID, "Examination")))
select = Select(Exam)

# Select options using different methods
select.select_by_value("UG I YEAR II SEMESTER END EXAMINATION - APRIL, 2026")
"""
input("Press Enter after you finish manual actions...")



xpath = "//input[@value='+' and contains(@onclick,'__doPostBack')]"

total = len(driver.find_elements(By.XPATH, xpath))

for i in range(total):
    element = driver.find_element(By.ID, f"GridView1_IntMid1_{i}")
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(33,39))

    element = driver.find_element(By.ID, f"GridView1_IntMid2_{i}" )
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(22,29))

    element = driver.find_element(By.ID, f"GridView1_Others_{i}")
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(22,29))

    # wait for buttons to be present
    buttons = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )

    btn = buttons[i]

    # scroll
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)

    # click using JS
    driver.execute_script("arguments[0].click();", btn)

    # 🔥 WAIT for page update (important)
    WebDriverWait(driver, 15).until(
        EC.staleness_of(btn)
    )


'''
i =0
xpath = "//input[@value='+' and contains(@onclick,'__doPostBack')]"
total = len(driver.find_elements(By.XPATH, xpath))

buttons = driver.find_elements(By.XPATH, "//input[@value='+']")
for i in range(30):
    
    
    element = driver.find_element(By.ID, f"GridView1_IntMid1_{i}")
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(33,39))

    element = driver.find_element(By.ID, f"GridView1_IntMid2_{i}" )
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(22,29))

    element = driver.find_element(By.ID, f"GridView1_Others_{i}")
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(22,29))
    
    btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"(//input[@value='+'])[ {i} ]")
        )
    )

    driver.execute_script("arguments[0].click();", btn)
'''

'''
for i in range(8):
    
    element = driver.find_element(By.ID, f"GridView1_IntMid1_{i}")
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(33,39))

    element = driver.find_element(By.ID, f"GridView1_IntMid2_{i}" )
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(22,29))

    element = driver.find_element(By.ID, f"GridView1_Others_{i}")
    element.clear()  # Optional: Removes existing text
    element.send_keys(random.randint(22,29))
    buttons = driver.find_elements(
        By.XPATH,
        "//input[@value='+' and contains(@onclick,'__doPostBack')]"
    )
    buttons[i].click()
'''
