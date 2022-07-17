from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Объект вебдрайвера
drv = webdriver.Chrome('chromedriver.exe')
# 1. Открыть страницу http://google.com/ncr
drv.get("http://google.com/ncr")
# 2. Выполнить поиск слова “selenide”
# .//input[contains(@class, "gLFyf gsfi")]
drv.find_element(By.XPATH, './/input[contains(@class, "gLFyf gsfi")]').send_keys('selenide')
drv.find_element(By.XPATH, './/input[contains(@class, "gLFyf gsfi")]').send_keys(Keys.ENTER)

# 3. Проверить, что первый результат – ссылка на сайт selenide.org.
# //*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite
assert 'selenide.org' in drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite').text

# 4. Перейти в раздел поиска изображений
# //*[@id="hdtb-msb"]/div[1]/div/div[2]/a
drv.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
# 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
# //*[@id="islrg"]/div[1]/div[1]/a[2]/div
print(drv.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text)
assert "selenide.org" in drv.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text

# 6. Вернуться в раздел поиска Все
# //*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]
drv.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
# 7. Проверить, что первый результат такой же, как и на шаге 3.
assert 'selenide.org' in drv.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite').text
drv.close()