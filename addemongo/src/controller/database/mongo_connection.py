from __future__ import annotations

from typing import Any, Sequence

from motor.motor_asyncio import AsyncIOMotorClient


class MongoConnection:

    def __init__(
        self,
        host: str | Sequence[str] | None = None,
        port: int | None = None,
        **kwargs: Any,
    ) -> None:

        self.__client = AsyncIOMotorClient(host, port, **kwargs)

    def set_database(self, name: str) -> MongoConnection:
        self.database = self.__client.get_database(name=name)
        return self

    def set_collection(self, name: str) -> MongoConnection:

        if not hasattr(self, "database"):
            raise AttributeError("Database not set")

        self.collection = self.database.get_collection(name=name)
        return self
