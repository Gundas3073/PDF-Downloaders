import urllib2

def main():
	global count
	count = 0	
	for n in range(0,6000):    
		global test 
		test = n		
		download_file("http://www.freeinfosociety.com/media/pdf/" + str(n) + ".pdf")
	print str(count)

def download_file(download_url):
	try:
		# Used to make sure no errors w/ HTTP request (AKA 404 Error trolls)		
		response = urllib2.urlopen(download_url)
		file = open(str(test) + ".pdf", 'wb')
		file.write(response.read())
		file.close()
		print("Completed")
		count = count + 1
	except urllib2.HTTPError, e:
		print "file number " + str(test) + " is not present"
	except urllib2.URLError, e:
		print "file number " + str(test) + " is not present"
	except:
		print " "
	
if __name__ == "__main__":
    main()
