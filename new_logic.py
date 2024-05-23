import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from mail_parser import get_email_code
from response_to_reviews_gpt import pure_magic
from database_handler import save_review
MIN_GRADE = 4

try:
    driver = uc.Chrome()

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

    result = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[2]/button[2]/div/div[2]/div')

    result = int(result.text)
    
    sleep(2)
    
    new_reviews = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[2]/button[2]')))
    new_reviews.click()

    sleep(1)
    
    while True:
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        try:
            show_more_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "index_showMoreBtn_1gCQz")))
            show_more_button.click()
        except:
            break

    sleep(1)
    driver.execute_script("window.scrollTo(0, 200)")
    
    for i in range(result):
        grade = int(driver.find_element(By.XPATH, f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[7]/div/div').text)
        if grade >= MIN_GRADE:
            vendor_code = driver.find_element(By.XPATH, f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[4]/div').text
            product = driver.find_element(By.XPATH, f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[4]/a').text
            review = driver.find_element(By.XPATH, f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[6]')
            review.click()
            sleep(1)
            pros = driver.find_element(By.XPATH, '//*[@id="ods-window-target-container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[10]/div[2]/div/div').text
            cons = driver.find_element(By.XPATH, '//*[@id="ods-window-target-container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[11]/div[2]/div/div').text
            comment = driver.find_element(By.XPATH, '//*[@id="ods-window-target-container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[12]/div[2]/div/div').text
            total_review = f"Плюсы товара: {pros if pros else 'отсутствует'}, минусы товара: {cons if cons else 'отсутствует'}, комментарий: {comment if comment else 'отсутствует'}, оценка: {grade}/5"
            
            save_review(product, vendor_code, pros, cons, comment, grade)
            
            response = pure_magic(total_review)
            
            javascript_code = f'''var textareaElement = document.querySelector('.index_textarea_1rzYd');
            var textToInsert = '{response}';
            textareaElement.value = textToInsert;
            var event = new Event('input',''' + ''' { bubbles: true });
            textareaElement.dispatchEvent(event);
            var button = document.querySelector('.custom-button_button_sTiyh');
            button.click();
            '''
            
            driver.execute_script(javascript_code)
            send_button = "var button = document.querySelector('.custom-button_button_sTiyh'); button.click();"
            driver.execute_script(send_button)
            close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ods-window-target-container"]/div/div[2]/div/button')))
            close_btn.click()
        driver.execute_script("window.scrollBy(0, 110);")
    exit()

finally:
    driver.quit()