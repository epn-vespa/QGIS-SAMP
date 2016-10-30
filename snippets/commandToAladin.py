from astropy.vo.samp import SAMPIntegratedClient
client = SAMPIntegratedClient()

def commandAladin(AlCommand): # define a function, so as not to forget disconnecting
    client.connect()
    client.notify_all({"samp.mtype":"script.aladin.send", "samp.params":{"script":AlCommand}})
    client.disconnect()
    print "command sent"

### TapHandle-style command:
AlCommand="Polygon ICRS 326.517 23.1 326.431 23.097 326.347 23.088 326.261 23.086 326.181 23.079 326.185 23.021 326.188 22.99 326.275 22.998 326.451 23.008 326.533 23.014 326.526 23.052 326.52 23.091;sync; 326.357000 23.045000;sync; zoom 0.7040000000000646 deg;"
### Minimal command:
AlCommand="draw polygon(10,10,12,11,11,12)"
### For more commands see Aladin {Ctrl+F5} (Tool > Script Console)
commandAladin(AlCommand)
