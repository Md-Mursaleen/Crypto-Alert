# Crypto-Alert
This Python script will help you get E-Mail alerts following certain conditions like the price going over a threshold (Example: Price > 2000 USD --> Alert)

Befor using the file you will need to follow these steps:
* Create a Gmail Account and set it up
* Create an account cryptomarketcap.com to get an API KEY
* Entrer the above info in your main.py
* DONE !

First, create a Gmail Account and go to this link : https://shorturl.at/dySY4 . Once there, accept less secure apps !

Secondely, go to https://coinmarketcap.com/api/ . And create an Account. After you complete all verification, go to the dashboards and copy your API KEY

![Image of the dashboard](https://github.com/saadze/Crypto-Alert/blob/main/images/coinmarketKEY.PNG)

Now you are almost ready to get up  and running, the basic file will only fetch the price of a currency after a certain time and send an email, but if you want to add conditions such as thresholds you can !

Let me guide you through this (we will change variables in the beginning of the file):
1. Open main.py
2. Set the Api key that we got previously in its allocated variable
3. Add the email adress that you created + its password
4. Change the "to" variable to your main email adress (where you will receive alerts)
5. Set a subject for the E-mails and set time to the time between the requests (in seconds) !!! 333 Calls per day MAX!
6. Finally set the symbol of the currency you want to follow in the symbol variable (example: BTC,ETH,XRP,LTC,DOGE etc), At the same time you set the output currency (example: USD,EUR,CAD)

![Image of the variables to change](https://github.com/saadze/Crypto-Alert/blob/main/images/variables.PNG)

Now your code is fully working (you can execute main.py) it will send automatic e-mails :) But if you want specific conditions, you're not done yet:
* Go to the line 42, here you can add conditions

![Possibility to add conditions](https://github.com/saadze/Crypto-Alert/blob/main/images/conditions.PNG)

When the condition is true, you should execute line 44 and 45

Here is an example:

![Possibility to add conditions](https://github.com/saadze/Crypto-Alert/blob/main/images/conditionsGood.PNG)



