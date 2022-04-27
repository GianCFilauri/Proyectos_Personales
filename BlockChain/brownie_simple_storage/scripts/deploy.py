from turtle import update
from brownie import accounts, config, SimpleStorage, network
#import os

def deploy_simple_storage():
    
    account = get_account()
    #Con accounts de Brownie
    #account = accounts[0]
    #print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    update_stored_value = simple_storage.retrieve()
    print(update_stored_value)
    
    #Con mi cuenta privada, usando .os
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    #print(account)

    #Con seccion wallet
    #account = accounts.add(config["wallets"]["from_key"])
    #print(account)

def get_account():
    if network.show_active() == "deveploment":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])



def main():
    deploy_simple_storage()