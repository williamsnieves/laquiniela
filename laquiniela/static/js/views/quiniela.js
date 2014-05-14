Quiniela.Views.Quinielas = Backbone.View.extend({

	el : $("#quiniela-content"),


	template: _.template($("#quiniela-template").html()),

	initialize : function(){
		this.render();
	},

	events : {
		"click #sedes-list li" : "stadiumClickHandler"
	},

	render : function(){
		var html = this.template()
		this.$el.html(html);

	}
})
