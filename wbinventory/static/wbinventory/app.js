Ext.require([
    'Ext.layout.container.Border',
    'WBI.view.Viewport'
]);

Ext.onReady(function () {
    Ext.application({
        name: 'WBI',
        paths: {
            // ...
        },
        controllers: [
            // ...
        ],
        autoCreateViewport: true
    });
});
