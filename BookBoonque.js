function getDownload() {
   var elem = bookLink.document.getElementsByClassName("submit");
   try {
       elem[0].click();
       //bookLink.window.setTimeout(getDownload, 5000);
   } 
   catch(err) {
   }
}
//Get all possible links
var links = [];
for( var i = 0 ; i < document.links.length ; i++ ) {
   links.push(document.links[i].href);
}
//End
for( i = 1; i < document.links.length ; i++ ) {
   var bookLink = window.open(links[i],'_blank','javascript:getDownload()');
   bookLink.onload = getDownload();
   bookLink.close();
}
