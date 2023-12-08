from seleniumbase import BaseCase

class DemoTest(BaseCase):
    def test_demo_page(self):

        self.open("https://www.saucedemo.com/")
        #login
        self.send_keys('input#user-name', 'standard_user')
        self.send_keys('input#password', 'secret_sauce')
        self.click('input#login-button')
        #verify page title
        self.assert_title("Swag Labs")
        #to add to cart
        self.click("#add-to-cart-sauce-labs-backpack")
        #checking the count on pipthe cart icon
        self.assert_text("1","span[class='shopping_cart_badge']")
        #Go to shipping page
        self.click("#shopping_cart_container")
        # to verify the item in cart
        self.assert_text("Sauce Labs Backpack", ".inventory_item_name")
        # to remove from add to cart
        self.click("#remove-sauce-labs-backpack")
        # # click on the continue shopping button
        self.click("#continue-shopping")
        #click the hamburger menu
        self.click(".bm-burger-button")
        #click logout
        self.click("#logout_sidebar_link")