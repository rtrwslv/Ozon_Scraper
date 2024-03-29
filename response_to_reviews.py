import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from mail_parser import get_email_code
from selenium.webdriver.common.action_chains import ActionChains

driver = uc.Chrome()

driver.get('https://seller.ozon.ru/app/registration/signin?auth=1')
driver.maximize_window()
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ga29-a2')))
button.click()
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
sleep(1)
with open('responses.txt', 'r') as file:
    strings = file.readlines()
    strings = [string.replace('\n', '') for string in strings ]
result = []
for string in strings:
    if string:
        result.append(string)
link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "tab-module_block_9cu1q")))
link.click()
sleep(1)
reviews = driver.find_elements(By.CLASS_NAME, 'index_reviewTextWrapper_3SKIG')
sleep(1)
for i in range(len(result)):
    reviews[i].click()
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
driver.quit()