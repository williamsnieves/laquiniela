Quiniela.Views.Cuartos = Backbone.View.extend({

	el : $("#cuartos-content"),

	events : {
		"click .btnquiniela" : "quinielaHandler",
		"click #group-list" : "groupHandler",
		"click .btn-save" : "saveQnlHandler",
		"click .btn-eliminatoria" : "showEliminatoriaHandler"
	},

	template: _.template($("#cuartos-template").html()),

	initialize : function(){
		this.render();
		//console.log($('#myModal'))
		//$(".new-quiniela").hide();
		
	},

	render : function(){
		var html = this.template()
		this.$el.html(html);
	}
})
