ContactPageMap = dict(FirstNameFieldXpath  = "//input[contains(@name, 'first')]",
                      LastNameFieldXpath   = "//input[contains(@name, 'last')]",
                      EmailFieldXpath      = "(//input[contains(@id, 'input')])[3]",
                      CommentFieldXpath    = "//textarea",
                      SubmitButtonXpath    = "//span[.='Submit']",
                      ThankYouMessageXpath = "//div[contains(text(), 'Thank you')]"
)

FacebookLoginPageMap = dict(UsernameFieldID = "email",
                            PasswordFieldID = "pass",
                            LoginButtonName = "login"
)

ProductPageMap = dict(QuantityDropDownID     = "wsite-com-product-option-Quantity",
                      FacebookShareLinkXpath = "//a[@title='Share on Facebook']"
)

ShareOnFacebookPageMap = dict(ShareLinkButtonName = "share"
)

WelcomePageMap = dict(SeeCoolestPhotosButtonXpath = "(//span[@class='wsite-button-inner'])[1]",
	                  SearchFieldName             = "q",
	                  SearchSubmitButtonXpath     = "//span[@class='wsite-search-button']"

)

# SearchResultsPageMap = dict( ProductImagesXpath = "//div[@title]"
# )

SearchResultsPageMap = dict( ProductImagesXpath = "//a[@title]"
)