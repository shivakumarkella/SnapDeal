from pages.GiftcardPage.giftcardpage import GiftcardPage
from test_page.testData import testDatafile as TD

class TestsGiftcard(object):

    def __init__(self,driver):
        self.obj_GiftCard = GiftcardPage(driver=driver)

    def test_ValidGiftCard(self):
        self.obj_GiftCard.giftcards(rName=TD.recipientName,rEmail=TD.recipientEmail,msge=TD.message,fulnam=TD.fullname,username=TD.userid,password=TD.password)