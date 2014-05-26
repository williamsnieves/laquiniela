Quiniela.Views.Eliminatorias = Backbone.View.extend({

	el : $("#eliminatoria-content"),

	template: _.template($("#eliminatoria-template").html()),

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
		var html = this.template()
		this.$el.html(html);
	}

	
})
