from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time, datetime, random, sys
from credentials import Email, User
from selenium.webdriver.common.keys import Keys
import smtplib

chromedriver_loc = "chromedriver"
chromedriver = chromedriver_loc #<------- Edit your path to where chromedriver is located
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome("/Users/kenny/Desktop/Amazon-bot/chromedriver")

# driver.get("https://www.amazon.com/")
# headlines = driver.find_elements_by_class_name("story-heading")
# for headline in headlines:
#     print(headline.text.strip())

class Product:
    """ Product class with helper functions. """
    
    def __init__(self,**kwargs):
        """ Constructor function of Product class. 
        Delay is set to random to avoid detection by amazon which
        could result in temporarily block. """

        self.amazon_credential = User()
        self.email_credential = Email()
        self.product = kwargs['p_url']

    def launch_bot(self):
        """ Initializes bot and emulates selenium browser. 
        It goes to login page first. """
        
        driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Famazonprime%3F_encoding%3DUTF8%26%252AVersion%252A%3D1%26%252Aentries%252A%3D0%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    def user_login_session(self):
        """ Enter user credentials and goto product page. """

        # driver.find_element_by_xpath\
        # ('''//*[@id="ap_email"]''').send_keys(self.amazon_credential.UNAME,Keys.RETURN)
        # time.sleep(1)
        # driver.find_element_by_xpath\
        # ('''//*[@id="ap_password"]''').send_keys(self.amazon_credential.PASSWD,Keys.RETURN)
        # time.sleep(10)
        
        """ Change this URL to add another product to cart. """
        # driver.get("https://www.amazon.com/gp/product/B0883PYCB7/ref=ox_sc_saved_title_1?smid=A1COA7PWTAABOP&psc=1/")
        driver.get("https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_1?dchild=1&keywords=ps5&qid=1606457183&rnid=2941120011&s=videogames&sr=1-1")

    def check_availability(self):
        """ This function checks product availability
        and adds it to cart when possible. """
        
        try:
        	driver.find_element_by_xpath\
            ('''//*[@id="priceblock_ourprice"]'''
            
        except:
            try:
            	driver.find_element_by_xpath\
                ('''//*[@id="priceblock_dealprice"]''')
            except:
                try:
                    driver.find_element_by_xpath\
                    ('''//*[@id="priceblock_saleprice"]''')
                except:
                    pass
                else:
                    self.add_to_cart()
            else:
                self.add_to_cart()

        else:
            self.add_to_cart()
            
        finally:
            driver.refresh()
            time.sleep(random.randint(5,10))
            print('It is not is Stock yet.')
    
    def add_to_cart(self):
        """ Helper function to add product to cart."""

        print('Item added to cart.')
        driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
        # self.email_notification()
        # driver.quit()
    
    # def email_notification(self):
    #     """ Sends email to user to alert that product have been added to cart.
    #     Server in this function is setup for Outlook.com, it'll be different for other
    #     email services. """

    #     email = '''FROM: {user}\nTO: {to}\nSUBJECT: {subject}\n\n{body}'''\
    #     .format(user = self.email_credential.EMAIL,to=self.email_credential.RECEIVER,\
    #         subject=self.email_credential.SUBJECT,body=self.email_credential.BODY)
    #     server = smtplib.SMTP('smtp-mail.outlook.com',25)
    #     server.starttls()
    #     server.login(self.email_credential.EMAIL,self.email_credential.EMAILPASSWD)
    #     server.sendmail(self.email_credential.EMAIL,self.email_credential.RECEIVER, email)
    #     server.quit()

if __name__ == '__main__':
    """ This script is executed, when you run .py file. """

    print("\nStarting up...")

    product = sys.argv[1]
    bot = Product(p_url=product)
    # bot.launch_bot()
    bot.user_login_session()
    while 1:
        bot.check_availability()
        