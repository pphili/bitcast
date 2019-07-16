import cryptos as cry

class Account:
    
    def __init__(self, address, network = cry.Bitcoin(testnet = True)):
        self.net = network
        self.addr = address
        

    @property
    def values(self):
        UTXOs = self.net.unspent(self.addr)
        v = [UTXO['value'] for UTXO in UTXOs]
        return v

    @property
    def outputs(self):
        UTXOs = self.net.unspent(self.addr)
        out = [UTXO['output'].split(':') for UTXO in UTXOs]
        return out

    @property
    def totval(self):
        return sum(self.values)
    
        

if __name__ == '__main__':
    a = Account("n3S7n3pyERLsfaei3z4fRYQP14wA9AWnLM")
    print(a.outputs)
    print(a.values)
    print(a.totval)
    
