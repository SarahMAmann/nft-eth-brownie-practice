from brownie import AdvancedCollectible, accounts, network, config

def main():
   dev = accounts.add(config['wallets']['from_key'])
   print(network.show_active())
   publish_source = False
   Collectible = Collectible.deploy(
    config['networks'][network.show_actice()]['vrf_coordinator'],
    config['networks'][network.show_active()]['link_token'],
    config['networks'][networks.show_active()]['keyhash'],
    {"from": dev},
    publish_source=publish_source
   )
   fund_collectible(collectible)
   return collectible
