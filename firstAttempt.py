from hashlib import sha256
# from itertools import chain
# import re
# from sqlite3 import Timestamp
# from tabnanny import check
import time

class Block:
    def __init__(self,timeStamp,data,previousHash=''):
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.force = 0
        self.hash = self.calculate() 

    def calculate(self):
        while True:
            self.force = self.force + 1
            summary = sha256((str(self.timeStamp)+str(self.data)+str(self.previousHash)+str(self.force)).encode()).hexdigest()
            if summary[0:2] == "00":
                break
        return summary
            
class BlockChain:
    def __init__(self):
        self.chain = [self.createGenesis()]

    def createGenesis(self):
        return Block(time.ctime(),"to try data"," ")

    def addBlock(self,data):
        node = Block(time.ctime(),data,self.chain[-1].hash)
        self.chain.append(node)

    def checks(self):
        for i in range(len(self.chain)):
            if i != 0:
                first = self.chain[i-1].hash
                now = self.chain[i].previousHash
                if first != now:
                    return "the chain is broken"
                if  sha256((str(self.chain[i].timeStamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].force)).encode()).hexdigest() != self.chain[i].hash:
                    return "the chain is broken"
        return "Solid"

    def listing(self):
        print("BlockChain = \n")
        for i in range(len(self.chain)):
            print("Block =>" , i , "\nHash =>" , str(self.chain[i].hash) , "\nTimeStamp =>" , str(self.chain[i].timeStamp), "\nData =>" , str(self.chain[i].data), "\Force =>" , str(self.chain[i].force), "\npreviousHash =>" , str(self.chain[i].previousHash))

    
YouMakeSpaceChain = BlockChain()
    
while True:

    print("Make your choice \n Press 1 to add block \n Press 2 to see blocks \n Press 3 to chech chain \n Press 4 to exit")
    data = input()
    if data == "1":
        print("enter the amount sent")
        amount = input()
        YouMakeSpaceChain.addBlock(amount)
    elif data == "2":
        YouMakeSpaceChain.listing()
    elif data == "3":
        print(YouMakeSpaceChain.checks())
    elif data == "4":
        break

