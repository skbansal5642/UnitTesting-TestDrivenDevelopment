import os
import json

class Prices:

    def __init__(self, prices_path):
        self.prices = {}

        if not os.path.exists(prices_path):
            raise Exception("no such path: {}".format(prices_path))

        with open(prices_path, "r") as prices_file:
            self.prices = json.load(prices_file)

        if len(self.prices) == 0:
            raise Exception("no prices in '{}'".format(prices_path))


    def __iter__(self):

        for s in self.prices:
            yield s, self.prices[s]


    def dump(self):
        for foo in self:
            print("  {}".format(foo))

