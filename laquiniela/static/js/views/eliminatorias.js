Quiniela.Views.Eliminatorias = Backbone.View.extend({

	el : $("#eliminatoria-content"),

	initialize : function(){
		this.render();

		var eliminatoria = new Quiniela.Models.EliminatoriaOfi()

		eliminatoria.urlRoot = "/api/eliminatoria/oficial";

		eliminatoria.fetch({
			success :function(eliminatoria){
				console.log(eliminatoria)
			},

			error: function(error){
				console.log(error)
			}
		})
	},

	render : function(){
		this.$el.html(_.template($("#eliminatoria-template").html()));
	}

	
})
