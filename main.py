# Alex Cheung s
# web scraper using selenium webdriver
from selenium import webdriver

# time sleep 
# or import time; time.sleep(5)
from time import sleep

# my laptop chromedriver path to use
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# open google.com website
#driver.get("https://google.com")

# driver title, url, window id
# print(driver.title)
# print(driver.current_url)
#print(driver.current_window_handle)


# nezuko in stock
#driver.get("https://www.hottopic.com/product/funko-demon-slayer-kimetsu-no-yaiba-pop-animation-nezuko-kamado-vinyl-figure/13407577.html?cgid=funko")
# tanjiro ht out of stock
#driver.get("https://www.hottopic.com/product/funko-demon-slayer-kimetsu-no-yaiba-pop-animation-tanjiro-with-mask-vinyl-figure-hot-topic-exclusive/13412216.html")

# itachi out of stock
#driver.get("https://www.boxlunch.com/product/funko-pop-animation-naruto-shippuden-itachi-with-crows-vinyl-figure---boxlunch-exclusive/14417283.html?cjevent=53bbe92847ce11ec81d7ab2b0a1c0e0c&cm_mmc=AFF-_-CJN-_-Akademickie+Inkubatory+Technologiczne-_-8800748-_-12695057")
# tanjiro bl out of stock
driver.get("https://www.boxlunch.com/product/funko-pop-animation-demon-slayer-kimetsu-no-yaiba-tanjiro-kamado-water-breathing-glow-in-the-dark-vinyl-figure---boxlunch-exclusive/13399920.html")

counter = 5
while (counter != 0):
    counter -= 1
    driver.get("https://www.boxlunch.com/product/funko-pop-animation-demon-slayer-kimetsu-no-yaiba-tanjiro-kamado-water-breathing-glow-in-the-dark-vinyl-figure---boxlunch-exclusive/13399920.html")
    try: 
        add_to_cart = driver.find_element_by_id('add-to-cart')
        print("DEBUG: IN STOCK")
        #print("DEBUG: ADD TO CART ID:", add_to_cart)
    except:
        print("DEBUG: NO ADD TO CART ID")

    sleep(60)

try: 
    add_to_cart = driver.find_element_by_id('add-to-cart')
    print("DEBUG: ADD TO CART ID:", add_to_cart)
except:
    print("DEBUG: NO ADD TO CART ID")
print("DEBUG: DONE WITH PROGRAM")

#driver.get("https://www.hottopic.com/product/funko-demon-slayer-kimetsu-no-yaiba-pop-animation-tanjiro-with-mask-vinyl-figure-hot-topic-exclusive/13412216.html")

# sleep 5 seconds
# sleep(5)

# close tab
#driver.close()
# close window and end process
driver.quit()