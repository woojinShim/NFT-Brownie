from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_advanced_collectible


def main():
    # private key 가져오기
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    publish_source = False
    # 컨트랙 정보 가져오기
    advanced_collectible = AdvancedCollectible.deploy(
        # yaml 정보가져오기
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        # dev 계정으로 부터 정보를 가져옴
        {"from": dev},
        publish_source=publish_source,
    )
    fund_advanced_collectible(advanced_collectible)
    return advanced_collectible
