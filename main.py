# Alex Cheung s
# web scraper using selenium webdriver
from selenium import webdriver

# time sleep 
# or import time; time.sleep(5)
from time import sleep


# https://stackoverflow.com/questions/69418411/how-to-get-rid-of-response-messages-initiating-google-chrome-using-chromedriver
#from selenium.webdriver.chrome.options import Options
# for getting rid of print statements from machine to help clear my debugs
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])



# my laptop chromedriver path to use
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH, options=options)


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
#driver.get("https://www.boxlunch.com/product/funko-pop-animation-demon-slayer-kimetsu-no-yaiba-tanjiro-kamado-water-breathing-glow-in-the-dark-vinyl-figure---boxlunch-exclusive/13399920.html")

#driver.get("https://www.hottopic.com/product/funko-dc-comics-pop-heroes-two-face-vinyl-figure-2021-l.a.-comic-con-exclusive/15925194.html?cgid=funko#cm_sp=Homepage-_-Hero-_-LACCFunko&start=1")


# box lunch tanjiro dragon
# driver.get("https://www.boxlunch.com/product/funko-pop-animation-demon-slayer-kimetsu-no-yaiba-tanjiro-kamado-water-breathing-glow-in-the-dark-vinyl-figure---boxlunch-exclusive/13399920.html")
# hot topic tanjiro training
driver.get("https://www.hottopic.com/product/funko-demon-slayer-kimetsu-no-yaiba-pop-animation-tanjiro-with-mask-vinyl-figure-hot-topic-exclusive/13412216.html")


try:
    in_stock = driver.find_element_by_class_name('color-green')
    print("DEBUG:", in_stock.text)
except:
    print("DEBUG: no color-green class")

counter = 1
while (counter != 0):
    print("DEBUG: counter:", counter)
    # box lunch tanjiro dragon
    driver.get("https://www.boxlunch.com/product/funko-pop-animation-demon-slayer-kimetsu-no-yaiba-tanjiro-kamado-water-breathing-glow-in-the-dark-vinyl-figure---boxlunch-exclusive/13399920.html")
    try: 
        add_to_cart = driver.find_element_by_id('add-to-cart')
        print("DEBUG: IN STOCK")
        print("DEBUG: ADD TO CART ID:", add_to_cart.text)
    except:
        print("DEBUG: NO ADD TO CART ID")

    # hot topic tanjiro training
    driver.get("https://www.hottopic.com/product/funko-demon-slayer-kimetsu-no-yaiba-pop-animation-tanjiro-with-mask-vinyl-figure-hot-topic-exclusive/13412216.html")
    try: 
        add_to_cart = driver.find_element_by_id('add-to-cart')
        print("DEBUG: IN STOCK")
        print("DEBUG: ADD TO CART ID:", add_to_cart.text)
    except:
        print("DEBUG: NO ADD TO CART ID")

    counter -= 1
    sleep(5)

'''
try: 
    add_to_cart = driver.find_element_by_id('add-to-cart')
    print("DEBUG: ADD TO CART ID:", add_to_cart)
except:
    print("DEBUG: NO ADD TO CART ID")
'''

print("\nDEBUG: DONE WITH PROGRAM")

#driver.get("https://www.hottopic.com/product/funko-demon-slayer-kimetsu-no-yaiba-pop-animation-tanjiro-with-mask-vinyl-figure-hot-topic-exclusive/13412216.html")

# sleep 5 seconds
# sleep(5)

# close tab
#driver.close()
# close window and end process
driver.quit()