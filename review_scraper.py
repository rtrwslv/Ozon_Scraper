import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from mail_parser import get_email_code

driver = uc.Chrome()

driver.get('https://seller.ozon.ru/app/registration/signin?auth=1')
driver.maximize_window()
wait = WebDriverWait(driver, 10)
try:
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ga29-a2')))
    button.click()
except:
    print("Too many request, or cloudfare alert, please try again")
email_input = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
email_input.send_keys('karimov445@yandex.ru')
button = driver.find_element(By.CLASS_NAME, 'b239-a')
button.click()
sleep(15)
code_input = driver.find_element(By.CLASS_NAME, 'd216-a')
code = get_email_code()
code_input.send_keys(code)
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button-module_primary_JlYlU')))
button.click()
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button-module_primary_JlYlU')))
button.click()
link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Отзывы")))
link.click()
link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "tab-module_block_9cu1q")))
link.click()
sleep(1)
while True:
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    try:
        show_more_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "index_showMoreBtn_1gCQz")))
        show_more_button.click()
    except:
        break

sleep(2)
comments = driver.find_elements(By.CLASS_NAME, 'index_review_MIfmk')
grades = driver.find_elements(By.CLASS_NAME, 'index_ratingWrapper_1p0pa')
with open('reviews.txt', 'w') as file:
    for i in range(len(comments)):
        comment_text = f"{comments[i].text} Оценка: {grades[i].text}"
        file.write(comment_text + '\n***\n')

driver.quit()