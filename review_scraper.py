import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from mail_parser import get_email_code
import traceback

driver = uc.Chrome()

try:
    driver.get('https://seller.ozon.ru/app/registration/signin?auth=1')
    driver.set_window_size(width=1080, height=1080)
    wait = WebDriverWait(driver, 15)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layoutPage"]/div[1]/div/div[2]/div[1]/section/div/div/div/div/div[4]/div[3]/button')))
    button.click()
    email_input = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
    email_input.send_keys('karimov445@yandex.ru')
    button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layoutPage"]/div[1]/div/div[2]/div[1]/section/div/div/div/div/div[4]/button')))
    button.click()
    sleep(15)
    code_input = driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div/div[2]/div[1]/section/div/div/div/div/div[3]/div[1]/label/div/div/input')
    code = get_email_code()
    code_input.send_keys(code)


    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='3907528_1199077']")))
    button.click()

    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/div/div[2]/div/div/div[5]/button[2]')))
    button.click()

    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Отзывы")))
    link.click()

    sleep(1)

    link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[2]/button[2]')))
    link.click()

    sleep(1)

    # driver.quit()

    while True:
        sleep(0.3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        try:
            show_more_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/button')))
            show_more_button.click()
        except:
            traceback.print_exc()
            break

    sleep(2)
    num_of_reviews = int(driver.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[2]/button[2]/div/div[2]/div').text)
    print(f'Number of reviews: {num_of_reviews}')
    with open('reviews.txt', 'w', encoding='utf-8') as file:
        for i in range(num_of_reviews):
            driver.execute_script(f"window.scrollBy(0, 10);")
            sleep(0.05)
            grade = driver.find_element(By.XPATH, f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[7]').text
            review = driver.find_element(By.XPATH, f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[6]').text
            comment_text = f"{review} Оценка: {grade}"
            print(comment_text)
            file.write(comment_text + '\n***\n')
except:
    traceback.print_exc()
    print("Too many request, or cloudfare alert, please try again")
    exit()
    
finally:
    driver.quit()