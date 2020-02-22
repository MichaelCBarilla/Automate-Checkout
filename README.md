# Automate-Checkout
Automation of checkout process when given a product name in Json format. For the website 'Feature'.

Use https://feature.com/products.json to find a list of the most recent 30 products added to the online store.

Copy a title from one of the 30 products and put as a string into the availabilityCheck function as a parameter.

If 'not avaiable' is output, then the product string as not matched any of the 30 products on the product.json page

if found, chromium will open up and commence the automation until all the information is typed into the payment information page.
The console will output 'bought' if successfull. For safety, the clicking of the checkout button is not pressed so as not to accidently
buy something, this project was done for educational reasons.
