from channels import Group
from channels.sessions import channel_session
import random
from .models import Player, Group as OtreeGroup, Constants
import json
import time


def ws_connect(message, group_name):
    Group(group_name).add(message.reply_channel)



# Connected to websocket.receive
def ws_message(message, group_name):
    group_id = group_name[5:]
    jsonmessage = json.loads(message.content['text'])
    mygroup = OtreeGroup.objects.get(id=group_id)
    myplayer = mygroup.get_player_by_id( jsonmessage['id_in_group'] )

    if myplayer.role() == 'buyer':
        x = json.loads( mygroup.buyer )    
        print('BUYER loaded')  
    elif myplayer.role() == 'seller':
        x = json.loads( mygroup.seller )
        print('SELLER loaded')    
    else:
        print('failed')

    x.append( float( jsonmessage['value'] ) )

    # aufsteigend sortiert
    x.sort()
    
    if myplayer.role() == 'buyer':
        x.reverse()

    if myplayer.role() == 'buyer':
        mygroup.buyer = x    
    else:
        mygroup.seller = x
    
    mygroup.save()
    
    print('SELLER ', mygroup.seller)
    print('BUYER ', mygroup.buyer)

    textforgroup = json.dumps({
                                'role': myplayer.role(),
                                'value': x,
                                })
    print(textforgroup)
    Group(group_name).send({
        "text": textforgroup,
    })



# Connected to websocket.disconnect
def ws_disconnect(message, group_name):
    Group(group_name).discard(message.reply_channel)
