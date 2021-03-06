Quiniela.Views.Semis = Backbone.View.extend({

	el : $("#semis-content"),

	events : {
		"click .btnquiniela" : "quinielaHandler",
		"click #group-list" : "groupHandler",
		"click .btn-save" : "saveSemiHandler",
		"click .btn-eliminatoria" : "showEliminatoriaHandler"
	},


	initialize : function(){
		this.render();
		//console.log($('#myModal'))
		//$(".new-quiniela").hide();

		var currentCodqnl = localStorage.getItem("codigoqnl");
		var progressQnl = new Quiniela.Models.ProgressQnl();

		progressQnl.urlRoot = "/api/quiniela/cuartos/progress?codigo="+currentCodqnl;


		progressQnl.fetch({
			success : function(progress){
				if(progress.attributes.cant < 8){
					$(".alert-warning").text("Para ver esta ronda debes completar los Cuartos de Final");
					$(".alert-warning").fadeIn("slow").delay(5000).fadeOut("fast");
				}

				if(progress.attributes.cant === 8){

					$("#eliminatorias-body").fadeIn("slow");

					var semis  = new Quiniela.Models.Semifinal();
					semis.urlRoot = "/api/quiniela/semis?codigoqnl="+currentCodqnl;

					semis.fetch({
						success : function(semis){
							console.log(semis)
							$.each(semis.attributes,function(c,v){
								var ruta = "";
								switch(v.equipo){
									case "BRA":
										ruta = "/static/img/flags/brasil/brasil.png";
										break;
									case "CHI":
										ruta = "/static/img/flags/chile/chile.png";
										break;
									case "CMR":
										ruta = "/static/img/flags/camerun/camerun.png";
										break;
									case "CRO":
										ruta = "/static/img/flags/croacia/croacia.png";
										break;
									case "URU":
										ruta = "/static/img/flags/uruguay/uruguay.png";
										break;
									case "HOL":
										ruta = "/static/img/flags/holanda/holanda.png";
										break;
									case "AUS":
										ruta = "/static/img/flags/australia/australia.png";
										break;
									case "COL":
										ruta = "/static/img/flags/colombia/colombia.png";
										break;
									case "IRN":
										ruta = "/static/img/flags/iran/iran.png";
										break;
									case "JAP":
										ruta = "/static/img/flags/japon/japon.png";
										break
									case "GRE":
										ruta = "/static/img/flags/grecia/grecia.png";
										break
									case "CVA":
										ruta = "/static/img/flags/costamarfil/costamarfil.png";
										break
									case "ITA":
										ruta = "/static/img/flags/italia/italia.png";
										break
									case "CRC":
										ruta = "/static/img/flags/costarica/costarica.png";
										break
									case "ING":
										ruta = "/static/img/flags/inglaterra/inglaterra.png";
										break
									case "SUI":
										ruta = "/static/img/flags/suiza/suiza.png";
										break
									case "HON":
										ruta = "/static/img/flags/honduras/honduras.png";
										break
									case "ECU":
										ruta = "/static/img/flags/ecuador/ecuador.png";
										break
									case "NIG":
										ruta = "/static/img/flags/nigeria/nigeria.png";
										break
									case "BIH":
										ruta = "/static/img/flags/bosnia/bosnia.png";
										break
									case "ALE":
										ruta = "/static/img/flags/alemania/alemania.png";
										break
									case "ARG":
										ruta = "/static/img/flags/argentina/argentina.png";
										break
									case "GHA":
										ruta = "/static/img/flags/ghana/ghana.png";
										break
									case "USA":
										ruta = "/static/img/flags/usa/usa.png";
										break
									case "POR":
										ruta = "/static/img/flags/portugal/portugal.png";
										break
									case "BEL":
										ruta = "/static/img/flags/belgica/belgica.png";
										break
									case "RUS":
										ruta = "/static/img/flags/rusia/rusia.png";
										break
									case "KOR":
										ruta = "/static/img/flags/korea/korea.png";
										break
									case "AGL":
										ruta = "/static/img/flags/argelia/argelia.png";
										break
									case "ESP":
										ruta = "/static/img/flags/espana/espana.png";
										break
									case "FRA":
										ruta = "/static/img/flags/francia/francia.png";
										break
									case "MEX":
										ruta = "/static/img/flags/mexico/mexico.png";
										break

								}
								var strqnl = "<li id='"+v.cod_juego+"'><div class='qnl_octavos_juego'>"+
											"<span class='title-estadio'>Juego</span>"+
											"<span class='name-estadio'>"+v.codjuego+"</span>"+
										"</div>"+
										"<div class='qnl_clasificado'>"+
											"<span class='title-fecha'>Clasificado</span>"+
											"<span class='fecha'>"+v.cod_juego+"</span>"+
										"</div>"+
										"<img src='"+ruta+"' alt=''>"+
										"<span class='team-a'>"+v.equipo+"</span>"+
										"<input type='number' name='team-a' class='team_input team_input_a' max='9' min='0' value='0'/>"+
										"</li>";
								$(".list-matches").append(strqnl);
							})
						},
						error : function(err){
							console.log(err)
						}
					})
				}
			},
			error : function(err){
				$(".error-middle").text("Se ha producido un error intenta iniciar nuevamente");
				$(".success-middle").fadeIn("slow").delay(5000).fadeOut("fast");
			}
		})
		
	},

	render : function(){
		this.$el.html(_.template($("#semis-template").html()));
	},

	saveSemiHandler : function(e){

		$(".loader-semis").show();

		if($("#4A").children("input.team_input_a").val() === $("#4B").children("input.team_input_a").val() || 
			$("#4C").children("input.team_input_a").val() === $("#4D").children("input.team_input_a").val() 
			){
			$(".loader-semis").hide();
			$(".alert-warning").text("Debes elegir un ganador, tendras puntos solo por el acierto de tu equipo")
			$(".alert-warning").fadeIn("slow").delay(3000).fadeOut("slow")
		}else{
			var currentCodqnl = localStorage.getItem("codigoqnl");

			var listMatch = [];
			var objMatch = {};
			var mainMatch = {};

			$.each($(".list-matches li"), function(c,v){
				objMatch = {
					goles : $(v).children("input.team_input_a").val(),
					partido : $(v).attr("id"),
					progress : true
				}

				listMatch.push(objMatch);
			})

			mainMatch.data = listMatch

			console.log(mainMatch);

			var updateSemiQnl = new Quiniela.Models.QuinielaUpdate();

			updateSemiQnl.urlRoot = "/api/quiniela/semis/update?codigoqnl="+currentCodqnl;

			updateSemiQnl.save(mainMatch,{
				success :function(response){
					$(".loader-semis").hide();
					$(".alert-success").text("Su Progreso en Semifinales se ha almacenado");
					$(".alert-success").fadeIn("slow").delay(1000).fadeOut("fast");

				},
				error: function(err){
					console.log("error en el servidor")
					console.log(err);
				}
			})
		}


	}
})
