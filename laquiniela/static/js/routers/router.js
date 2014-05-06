Quiniela.Router = Backbone.Router.extend({
	routes : {
		'dashboard/' : 'dashboardHandler',
		'curiosidades/' : 'curiosidadesHandler',
		'mundial/' : 'mundialHandler',
		'posiciones/' : 'posicionesHandler',
		'equipos/'  : 'equiposHandler',
		'quiniela/' : 'quinielaHandler'
	}

})

var app_router = new Quiniela.Router;

app_router.on("route : dashboardHandler",function(){
	console.log("test");
})

app_router.on("route : curiosidadesHandler",function(){
	console.log("curiosidades");
})

app_router.on("route : mundialHandler",function(){
	console.log("mundial");
})


Backbone.history.start({
	pushState : true,
	root : "/"
})