from fastapi import FastAPI
from schemas import DexResponse, PoolInfo
from typing import List

from helper import get_url, data_extraction

app = FastAPI()


@app.get("/pool/{chainId}/{token_address}")
def get_token(chainId: str, token_address: str) -> PoolInfo:
    """Get the pool info for one token address"""

    data = get_url(chainId=chainId, token_address=token_address)
    extracted_data = data_extraction(data=data)
    largest_pool_schema = DexResponse(**extracted_data["largest_pool"])

    return PoolInfo(
        largest_pool=largest_pool_schema,
        aggregated_liquidity=extracted_data["aggregated_liquidity"],
        pool_number=extracted_data["pool_number"],
    )


@app.get("/pools/{chainId}/{token_addresses}")
def get_token(chainId: str, token_addresses: str) -> List[PoolInfo]:
    """
    Get the pool info for several token addresses over a single chain.
    Addresses must be in a comma-separated format.
    """

    addresses = token_addresses.split(",")
    pools = []
    for address in addresses:
        data = get_url(chainId=chainId, token_address=address)
        extracted_data = data_extraction(data=data)
        largest_pool_schema = DexResponse(**extracted_data["largest_pool"])
        pools.append(
            PoolInfo(
                largest_pool=largest_pool_schema,
                aggregated_liquidity=extracted_data["aggregated_liquidity"],
                pool_number=extracted_data["pool_number"],
            )
        )
    return pools
