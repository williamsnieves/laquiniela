Quiniela.Views.Teams = Backbone.View.extend({

	el : $("#team-content"),

	initialize : function(){
		this.render();

		var equipo = new Quiniela.Models.Team()

		equipo.urlRoot =  "/api/equipos/?grupo=A";

		/*equipo.fetch({
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
		})*/

		var equipo = new Quiniela.Models.Team()

		equipo.urlRoot =  "/api/equipos/BRA";

		equipo.fetch({
			success : function(info){				

				$.each(info.attributes,function(k,val){
					console.log(val)

					$("#trapezoide2").html("<p>"+val.description+"</p>");
					$("#mundiales-content h2").text(val.mundiales);
					
					for(var i = 0; i < val.cant_titles ; i++){
						var countcopa = i+1
						$(".copas_ganadas").append("<li class='copas-activas' id='copa"+countcopa+"'><img src='../static/img/copa_activa.png' alt='' width='23' height='56'></li>")
						//$(".copas_ganadas").append("<li><img src='../static/img/copa_inactiva.png' alt='' width='23' height='56'></li>")
					}
					
					switch(val.name_team){
						case "BRA":
							$(".full-section").css("background","url(../static/img/teams/brasil/brasil.png) 100% 100%")
							break;						
					}
				})
			},
			error : function(error){
				console.log(error)
			}
		})
	},

	events : {
		"click #group-list li" : "groupClickHandler",
		"click #team-list li" : "teamClickHandler"
	},

	render : function(){
		this.$el.html(_.template($("#team-template").html()));

	},

	groupClickHandler : function(e){
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
	},

	teamClickHandler : function(e){
		var teamSelected = $(e.target).attr("data-prefijo");
		$(".copas-activas").html("");

		var equipo = new Quiniela.Models.Team()

		equipo.urlRoot =  "/api/equipos/"+teamSelected;

		equipo.fetch({
			success : function(info){				

				$.each(info.attributes,function(k,val){
					console.log(val)

					
					$("#trapezoide2").html("<p>"+val.description+"</p>");
					$("#mundiales-content h2").text(val.mundiales);
					
					for(var i = 0; i < val.cant_titles ; i++){
						var countcopa = i+1
						$(".copas_ganadas").append("<li class='copas-activas' id='copa"+countcopa+"'><img src='../static/img/copa_activa.png' alt='' width='23' height='56'></li>")
						//$(".copas_ganadas").append("<li><img src='../static/img/copa_inactiva.png' alt='' width='23' height='56'></li>")
					}
					
					switch(val.name_team){
						case "BRA":
							$(".full-section").css("background","url(../static/img/teams/brasil/brasil.png) 100% 100%")
							break;
						case "CMR":
							$(".full-section").css("background","url(../static/img/teams/camerun/camerun.jpg) 100% 100%")
							break;
						case "CRO":
							$(".full-section").css("background","url(../static/img/teams/croacia/croacia.jpg) 100% 100%")
							break;
						case "MEX":
							$(".full-section").css("background","url(../static/img/teams/mexico/mexico.jpg) 100% 100%")
							break;
						case "AUS":
							$(".full-section").css("background","url(../static/img/teams/australia/australia.jpg) 100% 100%")
							break;
						case "HOL":
							$(".full-section").css("background","url(../static/img/teams/holanda/holanda.jpg) 100% 100%")
							break;
						case "ESP":
							$(".full-section").css("background","url(../static/img/teams/espana/espana.jpg) 100% 100%")
							break;
						case "CHI":
							$(".full-section").css("background","url(../static/img/teams/chile/chile.jpg) 100% 100%")
							break;
						case "JAP":
							$(".full-section").css("background","url(../static/img/teams/japon/japon.jpg) 100% 100%")
							break;
						case "COL":
							$(".full-section").css("background","url(../static/img/teams/colombia/colombia.jpg) 100% 100%")
							break;
						case "CVA":
							$(".full-section").css("background","url(../static/img/teams/costamarfil/costamarfil.jpg) 100% 100%")
							break;
						case "GRE":
							$(".full-section").css("background","url(../static/img/teams/grecia/grecia.jpg) 100% 100%")
							break;
						case "CRC":
							$(".full-section").css("background","url(../static/img/teams/costarica/costarica.jpg) 100% 100%")
							break;
						case "ITA":
							$(".full-section").css("background","url(../static/img/teams/italia/italia.jpg) 100% 100%")
							break;
						case "ING":
							$(".full-section").css("background","url(../static/img/teams/inglaterra/inglaterra.jpg) 100% 100%")
							break;
						case "URU":
							$(".full-section").css("background","url(../static/img/teams/uruguay/uruguay.jpg) 100% 100%")
							break;
						case "SUI":
							$(".full-section").css("background","url(../static/img/teams/suiza/suiza.jpg) 100% 100%")
							break;
						case "ECU":
							$(".full-section").css("background","url(../static/img/teams/ecuador/ecuador.jpg) 100% 100%")
							break;
						case "HON":
							$(".full-section").css("background","url(../static/img/teams/honduras/honduras.jpg) 100% 100%")
							break
						case "FRA":
							$(".full-section").css("background","url(../static/img/teams/francia/francia.jpg) 100% 100%")
							break
						case "ARG":
							$(".full-section").css("background","url(../static/img/teams/argentina/argentina.jpg) 100% 100%")
							break
						case "IRN":
							$(".full-section").css("background","url(../static/img/teams/iran/iran.jpg) 100% 100%")
							break
						case "BIH":
							$(".full-section").css("background","url(../static/img/teams/bosnia/bosnia.jpg) 100% 100%")
							break
						case "NIG":
							$(".full-section").css("background","url(../static/img/teams/nigeria/nigeria.jpg) 100% 100%")
							break
						case "USA":
							$(".full-section").css("background","url(../static/img/teams/usa/usa.jpg) 100% 100%")
							break
						case "ALE":
							$(".full-section").css("background","url(../static/img/teams/alemania/alemania.jpg) 100% 100%")
							break
						case "GHA":
							$(".full-section").css("background","url(../static/img/teams/ghana/ghana.jpg) 100% 100%")
							break
						case "POR":
							$(".full-section").css("background","url(../static/img/teams/portugal/portugal.jpg) 100% 100%")
							break
						case "KOR":
							$(".full-section").css("background","url(../static/img/teams/korea/korea.jpg) 100% 100%")
							break
						case "BEL":
							$(".full-section").css("background","url(../static/img/teams/belgica/belgica.jpg) 100% 100%")
							break
						case "RUS":
							$(".full-section").css("background","url(../static/img/teams/rusia/rusia.jpg) 100% 100%")
							break
						case "AGL":
							$(".full-section").css("background","url(../static/img/teams/argelia/argelia.jpg) 100% 100%")
							break
					}
				})
			},
			error : function(error){
				console.log(error)
			}
		})

	}
	/*groupClickHandler : function(e){
		var chooseTeam = e.target.innerText;
		var result = Quiniela.listTeam.where({group_team : chooseTeam});
		var equipos = [];
		var obj = {};
		var names = {}; 


		$.each(result,function(c,v){
			//console.log(v.attributes.country_team)
			names = {
				name : v.attributes.country_team
			}
			equipos.push(names);
		})

		obj.teams = equipos; 
		
		
		var teams = new Quiniela.Views.Teams();

		teams.catchTeam(obj)


	}*/
})
