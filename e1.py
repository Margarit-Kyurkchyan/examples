from __future__ import annotations
from typing import List
import asyncio
from pydantic import BaseModel, Field, validator
import random
import contextlib

# --- Data Models ---
class Trade(BaseModel):
    symbol: str
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)

    @property
    def value(self) -> float:
        return self.quantity * self.price


class Portfolio(BaseModel):
    owner: str
    trades: List[Trade] = []

    @property
    def total_value(self) -> float:
        return sum(t.value for t in self.trades)


# --- Service Layer ---
class MarketAPI:
    """Fake async market API that fetches prices."""

    async def get_price(self, symbol: str) -> float:
        await asyncio.sleep(0.2)  # simulate latency
        return round(random.uniform(100, 300), 2)


class TradeExecutor:
    def __init__(self, market: MarketAPI):
        self.market = market

    async def buy(self, portfolio: Portfolio, symbol: str, qty: int) -> Trade:
        price = await self.market.get_price(symbol)
        trade = Trade(symbol=symbol, quantity=qty, price=price)
        portfolio.trades.append(trade)
        return trade


# --- Context Manager Example ---
@contextlib.asynccontextmanager
async def trading_session(owner: str):
    portfolio = Portfolio(owner=owner)
    print(f"🔑 Opening trading session for {owner}")
    yield portfolio
    print(f"📊 Closing session. Final portfolio value: ${portfolio.total_value:.2f}")


# --- Demo Run ---
async def main():
    market = MarketAPI()
    executor = TradeExecutor(market)

    async with trading_session("Bianca") as pf:
        await executor.buy(pf, "AAPL", 5)
        await executor.buy(pf, "TSLA", 2)
        await executor.buy(pf, "MSFT", 10)

        for trade in pf.trades:
            print(f"✅ {trade.quantity} {trade.symbol} @ ${trade.price} = ${trade.value}")

# Run it
if __name__ == "__main__":
    asyncio.run(main())
