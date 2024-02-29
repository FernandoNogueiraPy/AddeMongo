from typing import Any

from addemongo.src.controller.database.mongo_connection import MongoConnection
from motor.motor_asyncio import AsyncIOMotorClient
from pytest_mock import MockFixture


class MongoConnectionSuite:

    def test_should_intance_async_motorclient_in_init(self, mocker: MockFixture):

        def stub_init(*arg: Any, **kwargs: Any) -> None:
            pass

        mocker.patch.object(AsyncIOMotorClient, "__init__", stub_init)
        init_spy = mocker.spy(AsyncIOMotorClient, "__init__")
        MongoConnection()
        init_spy.assert_called_once()
