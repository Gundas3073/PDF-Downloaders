import urllib2

def main():
    test()
    global t
    t = 0
    print len(updated_list)
    for n in range(0,len(updated_list)):
        t = n
        download_file(r"https://www.syncfusion.com/content/downloads/ebook/" + updated_list[n])
    
        
    
        
	
        
def test():
    response = urllib2.urlopen('https://www.syncfusion.com/resources/techportal/ebooks') # Gets HTML source
    file = response.read() # Turns into string
    a = 0
    list_of_indx = []
    for n in range(1,66):
        b = a
        if a == 0:
            a = file.find("Succinctly</a>", 0, len(file)) # To find stuufff
	else:
            a = file.find("Succinctly</a>", b+1, len(file))
        list_of_indx.append(a)
    real_list = [] 
    for tester in list_of_indx:
        test = file[tester-40:tester]
        if test[len(test)-2:len(test)] != "  ":
            real_list.append(test)
    global updated_list
    updated_list = []
    for item in real_list:
        ind =  item.find(">")
        item = item[ind+1:]
        if item[0] == " ":
            item = item[1:]
        item = item.replace(" ", "_")
        item = item.replace("#", "_Sharp")
        updated_list.append( item + "Succinctly")        

def download_file(download_url):
	try:
		# Used to make sure no errors w/ HTTP request (AKA 404 Error trolls)		
		response = urllib2.urlopen(download_url)
		file = open(updated_list[t] + ".pdf", 'wb')
		file.write(response.read())
		file.close()
		print("Completed")
	except:
		print updated_list[t] + " is not present"

if __name__ == "__main__":
    main()
