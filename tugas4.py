from selenium import webdriver

# List of website
browser = ['https://tiket.com', 
           'https://www.tokopedia.com', 
           'https://www.orangsiber.com',
           'https://www.idejongkok.com',
           'https://www.kelasotomesyen.com']

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=option)
driver.minimize_window()

# Looping to get the URL and Title of the website
for i in browser:
    driver.get(i)
    get_url = driver.current_url
    get_title = driver.title
    print(f'{get_url} - Title: {get_title} \n')

# Close the browser
driver.close()