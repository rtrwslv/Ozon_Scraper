import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from mail_parser import get_email_code
from selenium.webdriver.common.action_chains import ActionChains
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

    link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[2]/button[2]')))
    link.click()

    with open('responses.txt', 'r') as file:
        strings = file.readlines()
        strings = [string.replace('\n', '') for string in strings ]
    result = []
    for string in strings:
        if string:
            result.append(string)

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
    reviews = driver.find_elements(By.CLASS_NAME, 'index_reviewTextWrapper_3SKIG')
    sleep(5)

    for i in range(len(result)):
        review = driver.find_element(By.XPATH, f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[6]')
        review.click()
        sleep(1)
        javascript_code = f'''var textareaElement = document.querySelector('.index_textarea_1rzYd');
            var textToInsert = '{result[i]}';
            textareaElement.value = textToInsert;
            var event = new Event('input',''' + ''' { bubbles: true });
            textareaElement.dispatchEvent(event);
            var button = document.querySelector('.custom-button_button_sTiyh');
            button.click();
            '''
        driver.execute_script(javascript_code)
        send_button = "var button = document.querySelector('.custom-button_button_sTiyh'); button.click();"
        driver.execute_script(send_button)
        close_btn = "var button = document.querySelector('.window-module_closeIcon_P6SGd'); button.click();"
        driver.execute_script(close_btn)
        driver.execute_script("window.scrollBy(0, 100);")

    sleep(10)
except:
    print("Too many request, or cloudfare alert, please try again")
    exit()

finally:
    driver.quit()