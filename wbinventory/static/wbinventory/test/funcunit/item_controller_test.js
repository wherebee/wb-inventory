/*global module: true, ok: true, equals: true, S: true, test: true */
module("item", {
	setup: function () {
		// open the page
		S.open("//wbinventory/wbinventory.html");

		//make sure there's at least one item on the page before running a test
		S('.item').exists();
	},
	//a helper function that creates a item
	create: function () {
		S("[name=name]").type("Ice");
		S("[name=description]").type("Cold Water");
		S("[type=submit]").click();
		S('.item:nth-child(2)').exists();
	}
});

test("items present", function () {
	ok(S('.item').size() >= 1, "There is at least one item");
});

test("create items", function () {

	this.create();

	S(function () {
		ok(S('.item:nth-child(2) td:first').text().match(/Ice/), "Typed Ice");
	});
});

test("edit items", function () {

	this.create();

	S('.item:nth-child(2) a.edit').click();
	S(".item input[name=name]").type(" Water");
	S(".item input[name=description]").type("\b\b\b\b\bTap Water");
	S(".update").click();
	S('.item:nth-child(2) .edit').exists(function () {

		ok(S('.item:nth-child(2) td:first').text().match(/Ice Water/), "Typed Ice Water");

		ok(S('.item:nth-child(2) td:nth-child(2)').text().match(/Cold Tap Water/), "Typed Cold Tap Water");
	});
});

test("destroy", function () {

	this.create();

	S(".item:nth-child(2) .destroy").click();

	//makes the next confirmation return true
	S.confirm(true);

	S('.item:nth-child(2)').missing(function () {
		ok("destroyed");
	});

});