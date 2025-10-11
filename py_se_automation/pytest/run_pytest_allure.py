import os
os.system("pytest --alluredir=reports/ && allure serve reports/")
