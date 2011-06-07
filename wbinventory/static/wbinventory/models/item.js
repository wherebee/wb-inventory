/**
 * @tag models, home
 * Wraps backend item services.  Enables 
 * [Wbinventory.Models.Item.static.findAll retrieving],
 * [Wbinventory.Models.Item.static.update updating],
 * [Wbinventory.Models.Item.static.destroy destroying], and
 * [Wbinventory.Models.Item.static.create creating] items.
 */
$.Model.extend('Wbinventory.Models.Item',
/* @Static */
{
	/**
 	 * Retrieves items data from your backend services.
 	 * @param {Object} params params that might refine your results.
 	 * @param {Function} success a callback function that returns wrapped item objects.
 	 * @param {Function} error a callback function for an error in the ajax request.
 	 */
	findAll: function( params, success, error ){
		return $.ajax({
			url: '/wbinventory/api/v1/item/',
			type: 'get',
			dataType: 'json',
			data: params,
			success: this.callback(['models',success]),
			error: error,
			fixture: "//wbinventory/fixtures/items.json.get" //calculates the fixture path from the url and type.
		});
	},
	/**
	 * Updates a item's data.
	 * @param {String} id A unique id representing your item.
	 * @param {Object} attrs Data to update your item with.
	 * @param {Function} success a callback function that indicates a successful update.
 	 * @param {Function} error a callback that should be called with an object of errors.
     */
	update: function( id, attrs, success, error ){
		$.ajax({
			url: '/items/'+id,
			type: 'put',
			dataType: 'json',
			data: attrs,
			success: success,
			error: error,
			fixture: "-restUpdate" //uses $.fixture.restUpdate for response.
		});
	},
	/**
 	 * Destroys a item's data.
 	 * @param {String} id A unique id representing your item.
	 * @param {Function} success a callback function that indicates a successful destroy.
 	 * @param {Function} error a callback that should be called with an object of errors.
	 */
	destroy: function( id, success, error ){
		$.ajax({
			url: '/items/'+id,
			type: 'delete',
			dataType: 'json',
			success: success,
			error: error,
			fixture: "-restDestroy" // uses $.fixture.restDestroy for response.
		});
	},
	/**
	 * Creates a item.
	 * @param {Object} attrs A item's attributes.
	 * @param {Function} success a callback function that indicates a successful create.  The data that comes back must have an ID property.
	 * @param {Function} error a callback that should be called with an object of errors.
	 */
	create: function( attrs, success, error ){
		$.ajax({
			url: '/items',
			type: 'post',
			dataType: 'json',
			success: success,
			error: error,
			data: attrs,
			fixture: "-restCreate" //uses $.fixture.restCreate for response.
		});
	}
},
/* @Prototype */
{});