module("Model: Wbinventory.Models.Item")

asyncTest("findAll", function(){
	stop(2000);
	Wbinventory.Models.Item.findAll({}, function(items){
		ok(items)
        ok(items.length)
        ok(items[0].name)
        ok(items[0].description)
		start()
	});
	
})

asyncTest("create", function(){
	stop(2000);
	new Wbinventory.Models.Item({name: "dry cleaning", description: "take to street corner"}).save(function(item){
		ok(item);
        ok(item.id);
        equals(item.name,"dry cleaning")
        item.destroy()
		start();
	})
})
asyncTest("update" , function(){
	stop();
	new Wbinventory.Models.Item({name: "cook dinner", description: "chicken"}).
            save(function(item){
            	equals(item.description,"chicken");
        		item.update({description: "steak"},function(item){
        			equals(item.description,"steak");
        			item.destroy();
        			start()
        		})
            })

});
asyncTest("destroy", function(){
	stop(2000);
	new Wbinventory.Models.Item({name: "mow grass", description: "use riding mower"}).
            destroy(function(item){
            	ok( true ,"Destroy called" )
            	start();
            })
})