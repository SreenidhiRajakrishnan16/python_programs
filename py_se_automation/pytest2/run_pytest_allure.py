import os

os.system('pytest --alluredir=allure-report/ && allure serve allure-report/')