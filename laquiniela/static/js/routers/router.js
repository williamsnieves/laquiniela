Quiniela.Router = Backbone.Router.extend({
	routes : {
		'dashboard/' : 'dashboardHandler',
		'curiosidades/' : 'curiosidadesHandler',
		'mundial/' : 'mundialHandler',
		'posiciones/' : 'posicionesHandler',
		'equipos/'  : 'equiposHandler',
		'estadios/'  : 'estadiosHandler',
		'quiniela/' : 'quinielaHandler'
	},

	equiposHandler : function(){
		var grupos = new Quiniela.Views.Teams()
		console.log(grupos)
	},

	estadiosHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var grupos = new Quiniela.Views.Stadiums()
	},

	quinielaHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var quiniela = new Quiniela.Views.Quinielas();
	}

})
