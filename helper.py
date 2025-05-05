from fastapi import HTTPException
import requests

MAIN_URL = "https://api.dexscreener.com/"


def get_url(chainId, token_address):
    """
    Call the Dexscanner API. Raise an error if the API call fails.
    parameter:
    - chainId: ID of the chain
    - token_address: address of a specific token of this chain
    :return: the Dexscanner API response parsed as a json format
    """
    url = f"{MAIN_URL}/token-pairs/v1/{chainId}/{token_address}"
    response = requests.get(url=url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="External API error: {response.text}",
        )
    return response.json()


def data_extraction(data):
    """
    Extract the data of interest for a certain token:
    - detail of the largest pool
    - aggregated liquidity over all of the pools
    - total number of pools
    :return: Dictionary containing all the data of interest
    """
    largest_pool = data[0]
    aggregated_liquidity = 0.0
    pool_number = len(data)

    for item in data:
        aggregated_liquidity += item["liquidity"]["usd"]
        if item["liquidity"]["usd"] >= largest_pool["liquidity"]["usd"]:
            largest_pool = item

    aggregated_liquidity = round(aggregated_liquidity, 2)

    return {
        "largest_pool": largest_pool,
        "aggregated_liquidity": aggregated_liquidity,
        "pool_number": pool_number,
    }
