Quiniela.Router = Backbone.Router.extend({
	routes : {
		'dashboard/' : 'dashboardHandler',
		'curiosidades/' : 'curiosidadesHandler',
		'mundial/' : 'mundialHandler',
		'fase-de-grupos/' : 'posicionesHandler',
		'eliminatorias/' : 'eliminatoriasHandler',
		'equipos/'  : 'equiposHandler',
		'estadios/'  : 'estadiosHandler',
		'quiniela/fase-de-grupos' : 'quinielaHandler',
		'quiniela/octavos' : 'octavosHandler',
		'quiniela/cuartos' : 'cuartosHandler',
		'quiniela/semis' : 'semisHandler',
		'quiniela/final' : 'finalHandler',
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
	},

	octavosHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var octavos = new Quiniela.Views.Octavos();
	},

	cuartosHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var cuartos = new Quiniela.Views.Cuartos();
	},

	semisHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var semis = new Quiniela.Views.Semis();
	},

	finalHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var final = new Quiniela.Views.Final();
	},

	posicionesHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var oficial = new Quiniela.Views.Oficiales();
	},

	eliminatoriasHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var oficial = new Quiniela.Views.Eliminatorias();
	},

	curiosidadesHandler : function(){
		$(".full-section").css("background","url(../static/img/bghand.png) 100% 100%")
		var oficial = new Quiniela.Views.Curiosidades();
	}

})
