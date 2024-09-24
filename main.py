import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from traceback import print_exc
from utils.mail_parser import get_email_code
from utils.response_to_reviews_gpt import pure_magic
from database_handler import save_review

MIN_GRADE = 0


def answer_reviews():
    try:
        driver = uc.Chrome()

        driver.get('https://seller.ozon.ru/app/registration/signin?auth=1')
        driver.set_window_size(width=1080, height=1080)
        wait = WebDriverWait(driver, 15)
        sleep(10)
        try:
            button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                            '/html/body/div[1]/div/div[1]/div/div[2]/div[1]/section/div/div/div/div/div[4]/div[4]/button/div')))
        except:
            button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                            '/html/body/div[1]/div/div[1]/div/div[2]/div[1]/section/div/div/div/div/div[4]/div[3]/button/div')))
        button.click()
        email_input = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        email_input.send_keys('karimov445@yandex.ru')
        button = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="layoutPage"]/div[1]/div/div[2]/div[1]/section/div/div/div/div/div[4]/button')))
        button.click()
        sleep(20)
        code_input = driver.find_element(By.XPATH,
                                         '//*[@id="layoutPage"]/div[1]/div/div[2]/div[1]/section/div/div/div/div/div[3]/div[1]/label/div/div/input')
        code = get_email_code()
        print('Code:' + str(code))
        code_input.send_keys(code)

        sleep(1)
        # button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='3907528_1199077']")))
        # button.click()

        input('Нажмите Enter для продолжения [Enter]: ')

        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[3]/button[2]/div")))
        button.click()

        # "/html/body/div[1]/main/div[1]/div[1]/div/div/div/div[4]/div/div/div[1]/a"

        sleep(5)

        try:
            company = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/div/span').text
        except Exception as e:
            # print(e)
            company = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[2]/div/div[1]/div/div/div[1]/div/span').text

        print('Company Name: ' + company)

        # link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[1]/div[1]/div/div/div/div[4]/div/div/div[1]/a")))
        link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Отзывы")))
        link.click()

        sleep(1)
        try:
            result = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/main/div[1]/div[1]/div/div/div[2]/div[2]/button[2]/div/div[2]/div')
            print(result.text)
            sleep(2)
        except Exception as e:
            print('Button Not Found')

        new_reviews = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[1]/div[1]/div/div/div[2]/div[2]/button[2]/div/div[1]/div/div')))
        new_reviews.click()

        sleep(1)

        # scores = wait.until(
        #     EC.element_to_be_clickable((By.XPATH,
        #                                 '/html/body/div[1]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div/div/button')))
        # scores.click()
        #
        # sleep(1)
        #
        # score_five = wait.until(
        #     EC.element_to_be_clickable((By.XPATH,
        #                                 '/html/body/div[4]/div/div/div/div/div/div/div[1]')))
        # score_five.click()

        # sleep(1)

        pages = 1
        all_pages_loaded = False
        while all_pages_loaded == False:
            sleep(5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            try:
                show_more_button = wait.until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "index_showMoreBtn_1gCQz")))
                show_more_button.click()
                pages += 1
                # driver.execute_script("window.scrollBy(0, 50);")
            except Exception as e:
                print('No more pages')
                all_pages_loaded = True

        try:
            result_text = result.text
            if result_text == '999+':
                result = pages
            else:
                result = int(result_text)
        except:
            pages = 1


        sleep(1)
        driver.execute_script("window.scrollTo(0, 200)")

        for i in range(result):
            try:
                sleep(1)
                grade = driver.find_element(By.XPATH,
                                            f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[7]/div/div').text
                print('grade: ' + str(grade))
                try:
                    grade = int(grade)
                except:
                    sleep(15)
                if grade >= MIN_GRADE:
                    vendor_code = driver.find_element(By.XPATH,
                                                      f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[4]/div').text
                    product = driver.find_element(By.XPATH,
                                                  f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[4]/a').text
                    review = driver.find_element(By.XPATH,
                                                 f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{i + 1}]/td[6]')
                    review.click()
                    sleep(1)
                    pros = driver.find_element(By.XPATH,
                                               '//*[@id="ods-window-target-container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[10]/div[2]/div/div').text
                    print(pros)
                    cons = driver.find_element(By.XPATH,
                                               '//*[@id="ods-window-target-container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[11]/div[2]/div/div').text
                    print(cons)
                    comment = driver.find_element(By.XPATH,
                                                  '//*[@id="ods-window-target-container"]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[12]/div[2]/div/div').text
                    total_review = f"Плюсы товара: {pros if pros else 'не указаны'}, минусы товара: {cons if cons else 'не указаны'}, комментарий: {comment if comment else 'отсутствует'}, оценка: {grade}/5"

                    save_review(company, product, vendor_code, pros, cons, comment, grade)

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
                    print('Ответ оставлен.')
                    close_btn = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="ods-window-target-container"]/div/div[2]/div/button')))
                    close_btn.click()
                    # driver.execute_script("window.scrollBy(0, 50);")
            except Exception as e:
                sleep(2)
                print(e)
                try:
                    close_btn = wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, '//*[@id="ods-window-target-container"]/div/div[2]/div/button')))
                    close_btn.click()
                except Exception as er:
                    print(er)

                print_exc()
        driver.quit()
        input('Нажмите Enter для закрытия [Enter]: ')
        exit()

    except Exception as e:
        print(e)
        print_exc()
    finally:
        driver.quit()
        input('Нажмите Enter для закрытия [Enter]: ')


if __name__ == '__main__':
    answer_reviews()