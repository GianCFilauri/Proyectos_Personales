from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storege = SimpleStorage[-1]
    print(simple_storege.retrieve())

def main():
    read_contract()