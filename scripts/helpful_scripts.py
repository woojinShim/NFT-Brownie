from brownie import AdvancedCollectible, accounts, network, config, interface


def get_breed(breed_number):
    switch = {0: "pug", 1: "SHIBA_INU", 2: "ST_BERNARD"}
    return switch[breed_number]


def fund_advanced_collectible(nft_contract):
    dev = accounts.add(config["wallets"]["from_key"])
    # 인터페이스 폴더의 링크토큰
    link_token = interface.LinkTokenInterface(
        config["networks"][network.show_active()]["link_token"]
    )
    link_token.transfer(nft_contract, 1000000000000000000, {"from": dev})
