import urllib as URLOpener
import re as REGEX



class Host:

    TDELEMENTREGEX=REGEX.compile("<td[^>]*>|</td>")

    def __init__(self):
        self.hostName=""
        self.status=""
        self.uptime=""
        self.usercount=0
        self.load=0.0

    def addHostInfo(self,hostinfo):
        unparsedData = self.TDELEMENTREGEX.split(hostinfo)
        remove_new_lines(unparsedData)
        remove_blank_lines(unparsedData)
        self.hostName=unparsedData[0]
        self.status=unparsedData[1]
        if (self.status=="up"):
            self.uptime=unparsedData[2][:len(unparsedData[2])-1] #removes , at end
            self.usercount=int(unparsedData[3])
            self.load=float(unparsedData[4])
        else:
            self.load=100000000.0
            self.uptime="0+00:00"
    def is_down(self):
        return self.status=="down"

    def __str__(self):
        return self.hostName + " " + self.status + " " + self.uptime + " " + \
        str(self.usercount) + " " + str(self.load)

    def __eq__(self,other):
        return self.name == other.name

    def get_name(self):
        return self.hostName

def remove_extra_table_tag(l):
    for item in l:
        if(item.find("</table>")):
            l.remove(item)

def remove_new_lines(l):
    for item in l:
        if(item == "\n"):
            l.remove(item)

def remove_blank_lines(l):
    for item in l:
        if(item == ""):
            l.remove(item)

def host_cmp(h1,h2):
    c = int((h1.load-h2.load)*100)
    if(c == 0):
        c = h1.usercount-h2.usercount
    return c

url = URLOpener.urlopen('https://apps.cs.utexas.edu/unixlabstatus/').read()

PARAGRAPHSREGEX = REGEX.compile("<p>|</p>")
PARAGRAPHS = PARAGRAPHSREGEX.split(url)

#Get table of hosts
hostsTable = PARAGRAPHS[3]

TRELEMENTREGEX = REGEX.compile("<tr>|</tr>")
TRELEMENTS = TRELEMENTREGEX.split(hostsTable)[6:]

remove_extra_table_tag(TRELEMENTS)
remove_new_lines(TRELEMENTS)

# for item in TRELEMENTS:
#     if(item.find("</table>") or item == "\n"):
#         TRELEMENTS.remove(item)



hosts = []
finish = len(TRELEMENTS)
for i in range(0, finish):
    host = Host()
    host.addHostInfo(TRELEMENTS[i])
    hosts.append(host)
    #print i, hosts[i]

hosts = sorted(hosts, cmp=host_cmp)
# for host in hosts:
#     print host

print hosts[0].get_name()
# for data in url.split("<table width=100%% cellspacing=0>"):
#     print data
#     print "Separated\n" #parser.feed(data)
# parser.close()

#print parser.table
