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
# options for getting rid of response messages
driver = webdriver.Chrome(executable_path=PATH, options=options)

# open google.com website
#driver.get("https://google.com")

# driver title, url, window id
# print(driver.title)
# print(driver.current_url)
#print(driver.current_window_handle)

# box lunch tanjiro dragon
# driver.get("https://www.boxlunch.com/product/funko-pop-animation-demon-slayer-kimetsu-no-yaiba-tanjiro-kamado-water-breathing-glow-in-the-dark-vinyl-figure---boxlunch-exclusive/13399920.html")
# hot topic tanjiro training
# driver.get("https://www.hottopic.com/product/funko-demon-slayer-kimetsu-no-yaiba-pop-animation-tanjiro-with-mask-vinyl-figure-hot-topic-exclusive/13412216.html")

'''
try:
    in_stock = driver.find_element_by_class_name('color-green')
    print("DEBUG:", in_stock.text)
except:
    print("DEBUG: no color-green class")
'''

# Wishlist check in stock orders instead of individual websites: can check all at once
# hot topic and box lunch have essentially the same websites (sister companies)
# In stock: "is-in-stock"
# Presale: "on-order"
# Out of stock: "notavailable"


counter = 5
while (counter != 0):
    print("DEBUG: counter:", counter)
    # hot topic wishlist
    driver.get("https://www.hottopic.com/showotherwishlist?WishListID=aeff70bb93d57f2d850769dc99")
    try: 
        # in stock 
        can_buy = driver.find_element_by_class_name('is-in-stock')
        print("DEBUG: HT IN STOCK!")
    except:
        # presale
        try: 
            can_buy = driver.find_element_by_class_name('on-order')
            print("DEBUG: HT CAN PRESALE!")
        except:
            print("DEBUG: HT no stock")

    # box lunch wishlist
    driver.get("https://www.boxlunch.com/showotherwishlist?WishListID=a9eb980965a10adbfc6edb0556")
    try: 
        # in stock
        can_buy = driver.find_element_by_class_name('is-in-stock')
        print("DEBUG: BL IN STOCK!")
    except:
        # presale
        try: 
            can_buy = driver.find_element_by_class_name('on-order')
            print("DEBUG: BL CAN PRESALE")
        except:
            print("DEBUG: BL no stock")

    counter -= 1
    sleep(0)



'''
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

'''
try: 
    add_to_cart = driver.find_element_by_id('add-to-cart')
    print("DEBUG: ADD TO CART ID:", add_to_cart)
except:
    print("DEBUG: NO ADD TO CART ID")
'''

print("\nDEBUG: DONE WITH PROGRAM")


# sleep 5 seconds
# sleep(5)

# close tab
#driver.close()

# close window and end process
driver.quit()

# end of program