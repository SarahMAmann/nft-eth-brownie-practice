from brownie import Collectible, network

def main():
    print("Working on" + network.show_active())
    collectible = Collectible[len(Collectible) -1]
    number_of_tokens = collectible.tokenCounter()


def write_metadata(number_of_tokens, nft_contract):
    for token_id in range(number_of_tokens):
        collectible_metadata = sample_metadata.metadata_template
        breed = get_breed
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active()) + str(token_id)
            + "-" + breed + ".json"
        )

# need to do more here but tired of python 😬🙄
# link to my ipfs metadata json file: https://ipfs.io/ipfs/QmTdZsiKZXMiYh1B4hATNHUe1DcDVA5CxRJNyaBWsiWch1?filename=panda.json