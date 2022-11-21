from block import Block

class Blockchain:
    diff = 20

    maxNonce = 2** 32
    target = 2 ** (256 - diff)
    block = Block("Genesis")
    head = block

    # This Method will add a New Block to Our Block Chain Network
    def add(self, block):
        # In These Lines we are Updating Our Variables for the Next         Iteration
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                # Updates the Nounce if it does not Finds one
                block.nonce += 1


blockchain = Blockchain()
for n in range(3):
    blockchain.mine(Block("Block " + str(n+1)))
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next