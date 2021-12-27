# Alex Cheung s
# web scraper using selenium webdriver
from selenium import webdriver

# my laptop chromedriver path to use
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# open google.com website
driver.get("https://google.com")

# driver title and url
# print(driver.title)
# print(driver.current_url)


#driver.get("https://www.hottopic.com/product/funko-demon-slayer-kimetsu-no-yaiba-pop-animation-tanjiro-with-mask-vinyl-figure-hot-topic-exclusive/13412216.html")


# close tab
#driver.close()
# close window
#driver.quit()