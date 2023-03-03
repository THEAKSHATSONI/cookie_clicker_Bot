import time
from selenium import webdriver
from selenium.webdriver.common.by import By

TIME = float(input("how much time you want to run this Bot :--- "))

driver_path = "/home/akshat/chrome-driver/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

#TODO:- Mechanicm for finding the elment which is right hand side after every "5 sec."

timeout = time.time() + TIME
for_5_min = time.time() + TIME*60

# list of items for buy
items = driver.find_elements(By.CSS_SELECTOR,"#store div")
items_list = [item.get_attribute("id") for item in items]
# print(items_list)

cps = ""

while for_5_min>time.time():

    # cookie clicker
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

    if time.time() >timeout:

        # current score
        score = driver.find_element(By.ID, "money").text
        if "," in score:
            score = int(score.replace(",", ""))
        else:
            score = int(score)
        # print(score)

        # list of values for buying
        values_list = [j.split(" - ")[1] for j in [i.text for i in driver.find_elements(By.CSS_SELECTOR, "#store div b")]
                       if (len(j.split(' - ')) == 2)]

        price_list = [][::-1]
        for i in values_list:
            if i.find(','):
                a = i.split(',')
                b = ''
                for j in a:
                    b = b+j
                price_list.append(int(b))
            else:
                price_list.append(int(i))

        # print(price_list)

        ids_dic = {}

        for i in range(len(price_list)):
            ids_dic[price_list[i]] = items_list[i]

        # print(ids_dic)

        # buying mechanism
        affordable_items = {}

        for cost,id in ids_dic.items():

            if cost >score:
                pass
            else:
                affordable_items[cost] =id

        if len(affordable_items)==0:
            pass
        else:
            maxi_it = max(affordable_items)
            driver.find_element(By.ID,affordable_items[maxi_it]).click()

        timeout += 5
        cps =  driver.find_element(By.ID, "cps").text

print(cps)
driver.quit()