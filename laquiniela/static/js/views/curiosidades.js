Quiniela.Views.Curiosidades = Backbone.View.extend({

	el : $("#curiosidad-content"),

	initialize : function(){
		this.render();
	},

	events : {
		"click #sedes-list li" : "anosClickHandler"
	},

	render : function(){
		this.$el.html(_.template($("#curiosidad-template").html()));

	},

	anosClickHandler : function(e){

		var chooseAno = $(e.target).attr("data-stadium");

	}
})
