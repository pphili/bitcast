import kivy
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.properties import ObjectProperty

from conversion import mess_to_add

import cc
import cryptos

from kivy.config import Config
Config.set('graphics', 'width', '1300')
Config.set('graphics', 'height', '1300')

AA = 'n3S7n3pyERLsfaei3z4fRYQP14wA9AWnLM'
private = 'd5fdd592f9864ea171c63fdc946e7b9bae5c45cf870d2f92187ee1de8abb0b2f'



class InputLayout(BoxLayout):
    address = ObjectProperty(None)    
    net = ObjectProperty(None)
    labelnet = ObjectProperty(None)
    coins = ObjectProperty(None)
    message = ObjectProperty(None)
    amount = ObjectProperty(None)
    outaddress = ObjectProperty(None)

    #intitialize global account variable
    in_account = 0
     # Functions attached to buttons
    def SubAddress(self):

        #store the input address
        addr = self.address.text

        if self.net.active:
            # don't want to spend real BTC right now..
            #in_account = cc.Account(addr, Bitcoin(testnet = False))
            print('switch is active')
        else:
            # create an account with the input address
            self.in_account = cc.Account(addr)
            #debug
            print(self.in_account.totval)
            x = 13
            self.coins.text = str(self.in_account.totval)


    def Sub_message(self):
        M = self.message.text
        out_address = mess_to_add(M)
        
        #test
        print(out_address)
        self.outaddress.text = out_address
        print(self.in_account)

    def send_transaction(self):
        maximum = float(self.coins.text)
        if float(self.amount.text) > maximum:
            print('error: you do not own enough')
        else:
            priv = self.priv.text
            #check 
            print(priv)
            print(self.outaddress.text)
            print(float(self.amount.text))
            self.in_account.net.send(priv, self.outaddress.text, int(self.amount.text))
            print('success')
        

class BTCMessageApp(App):
    def build(self):
        self.title = 'BTC Message App'
        return InputLayout()

if __name__ == '__main__':
    
    BTCMessageApp().run()

