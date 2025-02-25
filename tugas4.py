from selenium import webdriver

browser = ['https://tiket.com', 
           'https://www.tokopedia.com', 
           'https://www.orangsiber.com',
           'https://www.idejongkok.com',
           'https://www.kelasotomesyen.com']

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=option)
driver.minimize_window()

for i in browser:
    driver.get(i)
    get_url = driver.current_url
    get_title = driver.title
    print(f'{get_url} - Title: {get_title} \n')

driver.close()