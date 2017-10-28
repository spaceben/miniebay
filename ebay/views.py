from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
# from datetime import datetime
import time
import datetime


class WP(WaitPage):
    pass


class Auction(Page):
    pass

class Results(Page):
    pass


page_sequence = [
    WP,
    Auction,
    Results
]
