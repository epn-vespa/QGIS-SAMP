'''
This script will listen for a table url sent from TOPCAT, 
then load it in memory as astropy.table,
then display it in a browser window.
'''
from astropy.vo.samp import SAMPIntegratedClient
from astropy.table import Table
client = SAMPIntegratedClient()
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


### BROADCAST TABLE FROM TOPCAT

client.disconnect()
print r.received ## should return True

## Read table
t = Table.read(r.params['url'])
t.show_in_browser(jsviewer=True) #should open table in a browser
