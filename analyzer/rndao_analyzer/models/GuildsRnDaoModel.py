#!/usr/bin/env python3
import logging

from typing import TypedDict
from models.BaseModel import BaseModel

class GuildsRnDaoModel(BaseModel):
    def __init__(self, database=None):
        if database is None:
            logging.exception("Database does not exist.")
            raise Exception("Database should not be None")
        super().__init__(
            collection_name="guilds",
            database=database)
        print(self.database[self.collection_name].find_one())

    def get_connected_guilds(self):
        """
        Returns the list of the connected guilds
        """
        guilds = self.database[self.collection_name].find({"isDisconnected":False},{"guildId":1})
        return [x["guildId"] for x in guilds ]
