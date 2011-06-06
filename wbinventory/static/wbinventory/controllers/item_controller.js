/**
 * @tag controllers, home
 * Displays a table of items.	 Lets the user 
 * ["Wbinventory.Controllers.Item.prototype.form submit" create], 
 * ["Wbinventory.Controllers.Item.prototype.&#46;edit click" edit],
 * or ["Wbinventory.Controllers.Item.prototype.&#46;destroy click" destroy] items.
 */
$.Controller.extend('Wbinventory.Controllers.Item',
/* @Static */
{
	onDocument: true
},
/* @Prototype */
{
 /**
 * When the page loads, gets all items to be displayed.
 */
 "{window} load": function(){
	if(!$("#item").length){
	 $('section#app').append($('<div/>').attr('id','item'));
		 Wbinventory.Models.Item.findAll({}, this.callback('list'));
 	}
 },
 /**
 * Displays a list of items and the submit form.
 * @param {Array} items An array of Wbinventory.Models.Item objects.
 */
 list: function( items ){
	$('#item').html(this.view('init', {items:items} ));
 },
 /**
 * Responds to the create form being submitted by creating a new Wbinventory.Models.Item.
 * @param {jQuery} el A jQuery wrapped element.
 * @param {Event} ev A jQuery event whose default action is prevented.
 */
'form submit': function( el, ev ){
	ev.preventDefault();
	new Wbinventory.Models.Item(el.formParams()).save();
},
/**
 * Listens for items being created.	 When a item is created, displays the new item.
 * @param {String} called The open ajax event that was called.
 * @param {Event} item The new item.
 */
'item.created subscribe': function( called, item ){
	$("#item tbody").append( this.view("list", {items:[item]}) );
	$("#item form input[type!=submit]").val(""); //clear old vals
},
 /**
 * Creates and places the edit interface.
 * @param {jQuery} el The item's edit link element.
 */
'.edit click': function( el ){
	var item = el.closest('.item').model();
	item.elements().html(this.view('edit', item));
},
 /**
 * Removes the edit interface.
 * @param {jQuery} el The item's cancel link element.
 */
'.cancel click': function( el ){
	this.show(el.closest('.item').model());
},
 /**
 * Updates the item from the edit values.
 */
'.update click': function( el ){
	var $item = el.closest('.item'); 
	$item.model().update($item.formParams());
},
 /**
 * Listens for updated items.	 When a item is updated, 
 * update's its display.
 */
'item.updated subscribe': function( called, item ){
	this.show(item);
},
 /**
 * Shows a item's information.
 */
show: function( item ){
	item.elements().html(this.view('show',item));
},
 /**
 *	 Handle's clicking on a item's destroy link.
 */
'.destroy click': function( el ){
	if(confirm("Are you sure you want to destroy?")){
		el.closest('.item').model().destroy();
	}
 },
 /**
 *	 Listens for items being destroyed and removes them from being displayed.
 */
"item.destroyed subscribe": function(called, item){
	item.elements().remove();	 //removes ALL elements
 }
});