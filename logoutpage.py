class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.navigation_button_id = 'userNavigationLabel'
        self.logout_button_partial_link_text = 'Log Out'

    def click_navigator(self):
        self.driver.find_element_by_id(self.navigation_button_id).click()

    def click_logout(self):
        self.driver.find_element_by_partial_link_text(self.logout_button_partial_link_text).click()
