import os
import sys
import urllib
import urllib2
import urlparse
import xbmcgui

def remoteImport():
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)    
    urlStr = "http://iptvbase.net/system/1.0/data/kodi/v1/iptvControls.py"

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    req = urllib2.Request(urlStr, headers=hdr)
    r = opener.open(req)
    the_page = r.read()

    programPath = os.path.dirname(__file__)
    with open(os.path.abspath(programPath + "/iptvControls.py"), 'w') as f:
        f.write(the_page)
        f.close()


args = urlparse.parse_qs(sys.argv[2][1:])
mode = args.get('mode', None)

if __name__ == "__main__":
    remoteImport()

    import iptvControls
    iptvControls.Process(mode, args, "watchsuntv")
