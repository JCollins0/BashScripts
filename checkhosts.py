import urllib as URLOpener
import re as REGEX
import sys as System

class Chart:

    NO_COLOR="\033[00m"
    
    def show_chart(self, host):
    	title = host.hostName
    	aVal = int(host.load * 100)
    	spacing = 47//2-len(title)//2
    	tspacing = 45-spacing-len(title)
    	color = "\033[93m" if (aVal > 100) else "\033[32m"
    	color = "\033[31m" if host.is_down() else color

    	ucolor = "\033[93m" if (host.usercount > 20) else "\033[32m"
        ucolor = "\033[31m" if host.is_down() else ucolor
    	unumToDraw= 1 if host.usercount == 0 else host.usercount+1
    	numToDraw=0
    	if (aVal > 100000):
    	    numToDraw=48
    	elif (aVal > 10000):
    	    numToDraw=38+(aVal//10000)
    	elif (aVal > 1000):
    	    numToDraw=29+(aVal//1000)
    	elif (aVal > 100):
    	    numToDraw=20+(aVal//100)
    	elif (aVal > 10):
    	    numToDraw=11+(aVal//10)
    	elif (aVal > 1):
    	    numToDraw=1+aVal
    	else:
    	    numToDraw=1

    	print "                                                    "
    	print "                                                   4"
    	print "     0"+" "*spacing+title+" "*tspacing+"7"
    	print "     -----------------------------------------------"
    	print "user "+ucolor+"+"*unumToDraw+self.NO_COLOR
    	print "load "+color+"+"*numToDraw+self.NO_COLOR
    	print "     -----------------------------------------------"
    	print "     0         .        1        1        1        1"
    	print "               1                 0        0        0"
    	print "                                          0        0"
    	print "                                                   0"


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
            self.load=10000
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
    if(h1.is_down() and not h2.is_down()):
	return 1
    elif(h2.is_down() and not h1.is_down()):
	return -1
    c = int((h1.load-h2.load)*100)
    if(c == 0):
        c = h1.usercount-h2.usercount
    return c

def get_host_by_name(hosts, name):
    for host in hosts:
        if(host.hostName == name):
           return host
    return None

url = URLOpener.urlopen('https://apps.cs.utexas.edu/unixlabstatus/')
rcode = url.getcode()
url = url.read()

if(rcode == 200): #Response OK

    PARAGRAPHSREGEX = REGEX.compile("<p>|</p>")
    PARAGRAPHS = PARAGRAPHSREGEX.split(url)

    #Get table of hosts
    hostsTable = PARAGRAPHS[3]

    TRELEMENTREGEX = REGEX.compile("<tr>|</tr>")
    TRELEMENTS = TRELEMENTREGEX.split(hostsTable)[6:]

    remove_extra_table_tag(TRELEMENTS)
    remove_new_lines(TRELEMENTS)


    hosts = []
    finish = len(TRELEMENTS)
    for i in range(0, finish):
        host = Host()
        host.addHostInfo(TRELEMENTS[i])
        hosts.append(host)

    hosts = sorted(hosts, cmp=host_cmp)
    #for host in hosts:
    #     print host

    if (len(System.argv) > 1):
        chart = Chart()
        lim = len(System.argv)
        # print System.argv[1]
        if(System.argv[1] == 'all'):
            for host in hosts:
                chart.show_chart(host)
        else:
            for i in range(1, lim):
                cHost = get_host_by_name(hosts, System.argv[i])
                if (cHost != None):
                    chart.show_chart(cHost)
    else:
        print hosts[0].get_name()

else:
    print "Cannot reach host"
    exit(1)
