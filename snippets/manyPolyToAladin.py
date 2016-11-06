#when pasting into ipython, type %paste, then enter

from astropy.vo.samp import SAMPIntegratedClient
from astropy.table import Table
client = SAMPIntegratedClient()

def commandAladin(AlCommand): # define a function, so as not to forget disconnecting
    client.connect()
    client.notify_all({"samp.mtype":"script.aladin.send", "samp.params":{"script":AlCommand}})
    client.disconnect()
    print "command sent"

def captureTbl():
    client.connect()
    class Receiver(object):
        def __init__(self, client):
            self.client = client
            self.received = False
        def receive_call(self, private_key, sender_id, msg_id, mtype, params, extra):
            self.params = params
            self.received = True
            self.client.reply(msg_id, {"samp.status": "samp.ok", "samp.result": {}})
        def receive_notification(self, private_key, sender_id, mtype, params, extra):
            self.params = params
            self.received = True
    r = Receiver(client)
    client.bind_receive_call("table.load.votable", r.receive_call)
    client.bind_receive_notification("table.load.votable", r.receive_notification)
    while not r.received:
        pass
    print "Table recieved"
    client.disconnect()
    return Table.read(r.params['url'])

# now polygons can be recieved using 
# t['s_region'][1]
# convert it using 
# q=t['s_region'].tolist()
# next step would be to convert polygon strings to aladin commands
# obtain a string sample using q[0]
# it is more efficient to join polygon list into a single command, use
# w=';'.join(q);w=w+';sync;'

t=captureTbl() ## SEND TABLE NOW

commandAladin(';'.join(t['s_region'].tolist())+';sync;')
