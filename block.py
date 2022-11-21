# ref: https://medium.com/@harsathAI/create-a-simple-blockchain-with-python-under-60-lines-of-code-step-by-step-walkthrough-f3f7b60bb2e8

import datetime
import hashlib


class Block:  # Starting Of Out BLock Class
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    # Our Hash is a Haxa Decimal Data so we are declaring it as 0x0
    previous_hash = 0x0

    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data


    def hash(self):
        # We are Using SHA256 Algorithm(For Better Usage)
        hashVal = hashlib.sha256()
        # We have to Encode it in utf-8 Format(for Hash Computational Process)
        hashVal.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            # When Creating a New Block we Should Consider the Hash of the  Previous Block
            # Which is the Main Idea of Using BlockChain System
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return hashVal.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(
            self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"