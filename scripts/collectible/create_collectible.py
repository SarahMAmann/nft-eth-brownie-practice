from brownie import Collectible, accounts, config
import time

STATIC_SEED = 123

# it might be cleaner to break out these scripts more

def get_breed(breed_number):
    switch = {0: 'GIANT', 1: 'RED', 2: 'AILURUS'}
    return switch[breed_number]


def main():
    dev = accounts.add(config['wallets']['from_key'])
    collectible = Collectible[len(Collectible) -1]
    transaction = collectible.createCollectible(STATIC_SEED, "None" {"from": dev})
    transaction.wait(1)
    requestId = transaction.events['requestedCollectible']['requestId']
    token_id = collectible.requestIdToTokenId(requestId)
    breed = get_breed(collectible.tokenIdToBreed(token_id))
    time.sleep(35)
