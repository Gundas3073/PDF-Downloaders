import urllib2
from collections import OrderedDict
def main():
    global t
    t = 0
    search_list = FSRL('http://www.freeclassicebooks.com/',".htm\">","<a href=\"", 35 )
    print "Done"
    for testURL in search_list:
        list = []
        list = FSRL('http://www.freeclassicebooks.com/'+testURL+".htm",".pdf\">pdf</a>] ","[<a href=\"", 120 )
        list = [term.replace('_','%20') for term in list]
        global j
        for n in list:
            t = t+1
            n = n[1:]
            l = n
            j = change(n)
            download_file(r"http://www.freeclassicebooks.com/" + l + ".pdf") 
            
    
        
    
def change(name):
    for num in range(1,5):
        a = name.find("\\", 0 , len(name))
        if a != -1:
            name = name[a+1:]
            name = name.replace("%20", "_")
        else:
            name = name.replace("%20", "_")
    for num in range(1,5):
        a = name.find("/", 0 , len(name))
        if a != -1:
            name = name[a+1:]
            name = name.replace(" ", "_")
        else:
            name = name.replace(" ", "_")
    return name
	
        
def FSRL(url, beg, beg2, testlength): # Finds String from HTML, Returns List
    try:
        response = urllib2.urlopen(url) # Gets HTML source
        file = response.read() # Turns into string
        a = 0
        list_of_indx = []
        for n in range(1,68): # pt. 1
            b = a
            if a == 0:
                a = file.find(beg, 0, len(file)) # To find stuufff
	    else:
                a = file.find(beg, b+1, len(file))
            list_of_indx.append(a)
        real_list = [] 
        for tester in list_of_indx:# pt. 2
            test = file[tester-testlength:tester]
            if test[len(test)-2:len(test)] != "  ":
                real_list.append(test)
        updated_list = []
        for item in real_list :# pt. 3
            ind =  item.find(beg2)
            item = item[ind+9:]
            if item[0] == " ":
                item = item[1:]
            item = item.replace("%20", "_")
            item = item.lower()
            if len(item) != 1:
                updated_list.append( item + "")
        updated_list = list(OrderedDict.fromkeys(updated_list))
    except:
        print " "
        file = " "
        updated_list = []
    return updated_list
      

def download_file(download_url):
	try:
		# Used to make sure no errors w/ HTTP request (AKA 404 Error trolls)		
		response = urllib2.urlopen(download_url)
		file = open(j + " .pdf", 'wb')
		file.write(response.read())
		file.close()
	except:
		print j + " is not present"
if __name__ == "__main__":
    main()
