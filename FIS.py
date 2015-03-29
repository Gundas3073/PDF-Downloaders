import urllib2

def main():
	global count
	count = 0
        global n	
	for n in range(0000,6000):    
		global test 
		test = n
		getName("http://www.freeinfosociety.com/media.php?id=" + str(n),"</h1>","</a>/", 30) 
		download_file("http://www.freeinfosociety.com/media/pdf/" + str(n) + ".pdf")
	print str(count)

def download_file(download_url):
	try:
		# Used to make sure no errors w/ HTTP request (AKA 404 Error trolls)		
		response = urllib2.urlopen(download_url)
		file = open(name + ".pdf", 'wb')
		file.write(response.read())
		file.close()
		print("Completed")
		count = count + 1
	except urllib2.HTTPError, e:
		print "file " + str(n) + " "  +name + " is not present or is not a pdf"
	except urllib2.URLError, e:
		print "file " + str(n) + " " + name + " is not present or is not a pdf"
	except:
		print " "
def getName(url, beg, beg2, testlength):
    try:
        reponse2 = urllib2.urlopen(url)
        file2 = reponse2.read()
     #  file2 = "".join(file2.split())
        a = file2.find(beg2, 0, len(file2))
        a = file2.find(beg2, a+6, len(file2))
        a = file2.find(beg2, a+6, len(file2))
        b = file2.find(beg, a, len(file2))
        global name
        name = file2[a+5:b]
        print name
    except:
        print " "
            
if __name__ == "__main__":
    main()
