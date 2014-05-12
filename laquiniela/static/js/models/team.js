Quiniela.Models.Team = Backbone.Model.extend({

	urlRoot : "/api/equipos/"

});

/*Quiniela.Models.Team = Backbone.Model.extend({
	urlRoot : "/api/equipos/"
});

var equipo = new Quiniela.Models.Team();

//var grupo = 'A'

equipo.urlRoot = "/api/equipos/?grupo=A"

//console.log(equipo)

equipo.fetch({
	success :function(response){
		console.log(response.toJSON());
	}
})*/