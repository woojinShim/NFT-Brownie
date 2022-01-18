from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_breed
import time

STATIC_SEED = 123


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    # 최근 배포된 컨트랙트 가져오기
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advanced_collectible.createCollectible(
        STATIC_SEED, "None", {"from": dev}
    )
    transaction.wait(1)
    requestId = transaction.events["requestedCollectible"]["requestId"]
    token_id = advanced_collectible.requestIdToTokenId(requestId)
    time.sleep(45)
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    print("Dog breed of token id: {} is {}".format(token_id, breed))
