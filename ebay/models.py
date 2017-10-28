from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from django import forms
import time
import datetime
import json

doc = """
ebay auction example
"""


class Constants(BaseConstants):
    name_in_url = 'ebay'
    players_per_group = 3
    num_rounds = 1
    starting_time = 15
    extra_time = 15
    endowment = 100
    prize = 200
    num_others = players_per_group - 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for g in self.get_groups():
            g.seller = json.dumps([])
            g.buyer = json.dumps([])


class Group(BaseGroup):
    buyer = models.TextField()
    seller = models.TextField()

class Player(BasePlayer):
    def role(self):
        if self.id % 2 == 0:
            return 'buyer'
        else:
            return 'seller'
