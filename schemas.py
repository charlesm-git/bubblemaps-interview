from pydantic import BaseModel

from typing import List, Optional


class TokenInfo(BaseModel):
    address: Optional[str] = None
    name: Optional[str] = None
    symbol: Optional[str] = None


class Txns(BaseModel):
    buys: Optional[int] = None
    sells: Optional[int] = None


class DexscreenerTxns(BaseModel):
    m5: Optional[Txns] = None
    h1: Optional[Txns] = None
    h6: Optional[Txns] = None
    h24: Optional[Txns] = None


class Volume(BaseModel):
    h24: Optional[float] = None
    h6: Optional[float] = None
    h1: Optional[float] = None
    m5: Optional[float] = None


class PriceChange(BaseModel):
    h1: Optional[float] = None
    h6: Optional[float] = None
    h24: Optional[float] = None


class Liquidity(BaseModel):
    usd: Optional[float] = None
    base: Optional[float] = None
    quote: Optional[float] = None


class Social(BaseModel):
    type: Optional[str] = None
    url: Optional[str] = None


class Website(BaseModel):
    label: Optional[str] = None
    url: Optional[str] = None


class Info(BaseModel):
    imageUrl: Optional[str] = None
    header: Optional[str] = None
    openGraph: Optional[str] = None
    websites: Optional[List[Website]] = None
    socials: Optional[List[Social]] = None


class DexResponse(BaseModel):
    chainId: Optional[str] = None
    dexId: Optional[str] = None
    url: Optional[str] = None
    pairAddress: Optional[str] = None
    labels: Optional[List[str]] = None
    baseToken: Optional[TokenInfo] = None
    quoteToken: Optional[TokenInfo] = None
    priceNative: Optional[str] = None
    priceUsd: Optional[str] = None
    txns: Optional[DexscreenerTxns] = None
    volume: Optional[Volume] = None
    priceChange: Optional[PriceChange] = None
    liquidity: Optional[Liquidity] = None
    fdv: Optional[int] = None
    marketCap: Optional[int] = None
    pairCreatedAt: Optional[int] = None
    info: Optional[Info] = None


class PoolInfo(BaseModel):
    largest_pool: DexResponse
    aggregated_liquidity: float
    pool_number: int
