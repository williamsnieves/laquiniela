Quiniela.Collections.Teams = Backbone.Collection.extend({
	model : Quiniela.Models.Team,
	url: function(){
      return "/api/equipos/";
    }
})