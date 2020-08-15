from pages.GiftcardPage.giftcardpage import GiftcardPage

class TestsGiftcard(object):

    def __init__(self,driver):
        self.obj_GiftCard = GiftcardPage(driver=driver)

    def test_ValidGiftCard(self):
        self.obj_GiftCard.giftcards()