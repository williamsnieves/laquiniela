Quiniela.Views.Stadiums = Backbone.View.extend({

	el : $("#stadium-content"),


	template: _.template($("#stadium-template").html()),

	initialize : function(){
		this.render();
	},

	events : {
		"click #group-list li" : "groupClickHandler",
		"click #team-list li" : "teamClickHandler"
	},

	render : function(){
		var html = this.template()
		this.$el.html(html);

	}

	/*groupClickHandler : function(e){
		var chooseTeam = e.target.innerText;
		var equipo = new Quiniela.Models.Team()

		equipo.urlRoot =  "/api/equipos/?grupo="+chooseTeam;

		equipo.fetch({
			success : function(equipo){				

				var equipos = [];
				var obj = {};
				var names = {};

				$("#team-list").html(""); 

				$.each(equipo.attributes,function(c,v){
					
					names = {
						name : v.country_team,
						prefijo : v.name_team
					}
					equipos.push(names);
				})

				obj.teams = equipos; 
				console.log(obj)
				
				$.each(obj.teams,function(k,val){
					$("#team-list").append("<li data-prefijo ="+val.prefijo+">"+val.name+"</li>");
				})
				
			},
			error : function(error){
				console.log(error)
			}
		})
	}*/
})
