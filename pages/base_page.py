class BasePage:
    
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(10)
        
        
    def open(self):
        self.driver.get(self.url)