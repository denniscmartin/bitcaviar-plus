class Block:
    h = str()  # Block hash
    header = dict()
    transactions = []


class Header:
    version = int()
    previous_block_hash = str()
    merkle_root = str()
    timestamp = int()
    bits = int()
    nonce = int()


class Transaction:
    version = int()
    inputs = []
    outputs = []
    lock_time = int()


class TransactionInput:
    is_coinbase = False
    id = str()
    vout = int()
    script_sig = str()
    sequence = int()


class TransactionOutput:
    value = float()
    script_pub_key = str()