from brownie import AdvancedCollectible, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed
from pathlib import Path
import os
import requests


def main():
    print("Working on" + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_tokens = advanced_collectible.tokenCounter()
    print("The number of tokens you've deployed is {}".format(number_of_tokens))
    write_metadata(number_of_tokens, advanced_collectible)


def write_metadata(number_of_tokens, nft_contract):
    for token_id in range(number_of_tokens):
        collectible_metadata = sample_metadata.metadata_template
        breed = get_breed(nft_contract.tokenIdToBreed(token_id))
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            + str(token_id)
            + "-"
            + breed
            + ".json"
        )
        # ./metadata/rinkeby/0-SHIBA_INU.json
        if Path(metadata_file_name).exists():
            print("{} already found!".format(metadata_file_name))
        else:
            print("Creating Metadata File {}".format(metadata_file_name))
            collectible_metadata["name"] = get_breed(
                nft_contract.tokenIdToBreed(token_id)
            )
            collectible_metadata["description"] = "An adorable {} pup!".format(
                collectible_metadata["name"]
            )

            image_to_upload = None
            # ipfs에 업로드하기 위한 이미지 파일 선택
            if os.getenv("UPLOAD_IPFS") == "true":
                image_path = "./img/{}.png".format(breed.lower().replace("_", "-"))
                image_to_upload = upload_to_ipfs(image_path)


# http://127.0.0.1:5001
# curl -X POST -F file=@img/pug.png http://localhost:5001/api/v0/add


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://localhost:5001"
        response = requests.post(ipfs_url + "/api/v0/add", files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        print(filename)
