
genisis_block = {
        'previous hash':'',
        'index':0,
        'transactions': []
    }
blockchain = [genisis_block]
open_transactions = []
owner = 'Boris'
# This is a set, Not a dictionary!!
participants  = {owner}

def hash_block(block):
    return ' - '.join([str(block[key]) for key in block])

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_receive = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_receive += tx[0]   
    
    return amount_receive - amount_sent
 

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# Store a new transaction

def add_transactions(recipient, sender = owner, amount = 1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount':amount
        }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


# All open transactions are added to a new block 
# that will be added to the block chain Core featuere 
# of the blcok chain
def mine_block():

     # this gives us the last element in the block 
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)
  
    # now we can get the hash of the privious block
    # index is optional
    block = {
        'previous_hash': hashed_block,
        'index':len(blockchain),
        'transactions':open_transactions
    }
    blockchain.append(block) 
    return True

def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = input ('Enter the anount:')
    return (tx_recipient, tx_amount) #This is a Tuple !!

def get_user_choice():
    user_input = input('Your Choice ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print("Outputing Block")
        print(block)
    else:
        print('-' * 20)

#this function should go through the chain
# and verify if current block contains the last block
def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        # Compared priviousle stored hash with Recalculated hash of the last block
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True



def main():
    global open_transactions
    waiting_for_input = True
    while waiting_for_input:
        print("Please choose")
        print('1 : add a new transaction value')
        print('2 : mine block')
        print('3 : output the blockchain blocks')
        print('4: Output participants')
        print('h : Manipulate the chain')
        print('q : exit')
        user_choice = get_user_choice()
        if user_choice  == '1':
            tx_data = get_transaction_value()
            recipient, amount = tx_data
            add_transactions(recipient, amount = amount)
            print(open_transactions)
        elif user_choice == '2':
            if mine_block() == True:
                open_transactions = []                
        elif user_choice == '3':
            print_blockchain_elements()
        elif user_choice == '4':
            print(participants)
        elif user_choice == 'q':
            waiting_for_input = False
        elif user_choice == 'h':
            if len(blockchain) >= 1:
                blockchain[0] = {
                'previous hash':'',
                'index':0,
                'transactions': [{'sender': 'Chris', 'recipient':'Mike','amount':100}]
                }
        else:
            print('error')

        if not verify_chain():
            print('invalid chain')
            break
        
        print(get_balance('Boris'))
    print('Done!')
 
 
if __name__ == "__main__":
    main()
