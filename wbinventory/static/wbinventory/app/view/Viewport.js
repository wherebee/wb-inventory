Ext.define('WBI.view.Viewport', {
    extend: 'Ext.container.Viewport',

    requires: [

    ],

    layout: 'border',

    defaults: {
        bodyStyle: 'padding:15px'
    },

    items: [{
        region: 'north',
        height: 75,
        html: '<h1>Inventory</h1>'
    }, {
        xtype: 'panel',
        region: 'center',
        layout: 'anchor',
        items: [{
            xtype: 'panel',
            anchor: '100% 50',
            layout: 'hbox',
            items: [{
                xtype: 'textfield',
                name: 'search',
                flex: 1
            }, {
                xtype: 'button',
                text: 'Search'
            }, {
                xtype: 'button',
                text: 'New Item'
            }]
        }]
    }]
});
