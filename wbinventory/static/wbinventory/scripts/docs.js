//js wbinventory/scripts/doc.js

load('steal/rhino/steal.js');
steal.plugins("documentjs").then(function(){
	DocumentJS('wbinventory/wbinventory.html');
});