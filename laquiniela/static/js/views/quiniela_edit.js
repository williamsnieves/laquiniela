Quiniela.Views.EditQuinielas = Backbone.View.extend({

	el : $("#quiniela-content"),

	events : {
		"click .btnquiniela" : "quinielaHandler",
		"click #group-list" : "groupHandler",
		"click .btn-save" : "saveQnlHandler",
		"click .btn-eliminatoria" : "showEliminatoriaHandler"
	},

	initialize : function(){
		this.render();
		//console.log($('#myModal'))
		//$(".new-quiniela").hide();
		currentCodqnl = localStorage.getItem("codigoqnl");
		var defaultQnl = new Quiniela.Models.QuinielaList()
		defaultQnl.urlRoot = "/api/quinielas/?group=A&codqnl="+currentCodqnl;

		sessionStorage.setItem("grupo","A");

		defaultQnl.fetch({
			success : function(quiniela){
				$.each(quiniela.attributes,function(c,v){
					var fecha = new Date(v.date_qnl);
				    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1))
					var strqnl = "<li id='"+v.order_qnl+"'><div class='qnl_stadium'>"+
									"<span class='title-estadio'>Sede</span>"+
									"<span class='name-estadio'>"+v.city_match+"</span>"+
								"</div>"+
								"<div class='qnl_date'>"+
									"<span class='title-fecha'>Fecha</span>"+
									"<span class='fecha'>"+formato+"</span>"+
								"</div>"+
								"<img src='"+v.flag_a_qnl+"' alt=''>"+
								"<span class='team-a'>"+v.team_a_qnl+"</span>"+
								"<input type='number' name='team-a' class='team_input team_input_a' value='"+v.goals_a_qnl+"' max='9' min='0' placeholder='0'/>"+
								"<img src='"+v.flag_b_qnl+"' alt=''>"+
								"<span class='team-b'>"+v.team_b_qnl+"</span>"+
								"<input type='number' name='team-b' class='team_input team_input_b' value='"+v.goals_b_qnl+"' max='9' min='0' placeholder='0'/>"+
								"</li>";
					$(".list-matches").append(strqnl);
				})

				var positionTable = new Quiniela.Models.PositionQnl()

				positionTable.urlRoot = "/api/positions/qnlgroup/?group=A&codigoqnl="+currentCodqnl;

				positionTable.fetch({
					success:function(table){
						console.log(table)

						var headerGroup = table.attributes[0].group;
						$(".header-posiciones h3").text("GRUPO "+headerGroup);

						$.each(table.attributes,function(k,val){
							console.log(val);

							var strTable = "<tr>"+
						 						"<td>"+val.team+"</td>"+
						 						"<td>"+val.jj+"</td>"+
						 						"<td>"+val.jg+"</td>"+
						 						"<td>"+val.je+"</td>"+
						 						"<td>"+val.jp+"</td>"+
						 						"<td>"+val.gf+"</td>"+
						 						"<td>"+val.gc+"</td>"+
						 						"<td>"+val.dif+"</td>"+
						 						"<td>"+val.pts+"</td>"+
		 									"</tr>";

		 					$(".body-posiciones table tbody").append(strTable);
						})

						$(".new-quiniela").slideUp("slow");
						$("#team-container").fadeIn("slow");
						$("#quiniela-body").fadeIn("slow");
					},
					error : function(err){
						console.log(err)
					}
				})						


			},
			error:function(err){
				console.log("traigo errores");
				console.log(err)
			}	
		})
		$("#quiniela-body").show();

		
	},

	render : function(){
		this.$el.html(_.template($("#quiniela-template").html()));
	},

	groupHandler : function(e){
		var choosedGroup = e.target.innerText;
		var currentCodqnl = localStorage.getItem("codigoqnl");

		$(".btn-save").attr("data-type",choosedGroup);

		sessionStorage.setItem("grupo",choosedGroup)

		$(".list-matches").html("");

		var defaultQnl = new Quiniela.Models.QuinielaList()
		defaultQnl.urlRoot = "/api/quinielas/?group="+choosedGroup+"&codqnl="+currentCodqnl;

		defaultQnl.fetch({
			success : function(quiniela){
				console.log(quiniela)

				$.each(quiniela.attributes,function(c,v){
					console.log(v);
					var fecha = new Date(v.date_qnl);
				    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1))
					var strqnl = "<li id='"+v.order_qnl+"'><div class='qnl_stadium'>"+
									"<span class='title-estadio'>Sede</span>"+
									"<span class='name-estadio'>"+v.city_match+"</span>"+
								"</div>"+
								"<div class='qnl_date'>"+
									"<span class='title-fecha'>Fecha</span>"+
									"<span class='fecha'>"+formato+"</span>"+
								"</div>"+
								"<img src='"+v.flag_a_qnl+"' alt=''>"+
								"<span class='team-a'>"+v.team_a_qnl+"</span>"+
								"<input type='number' name='team-a' class='team_input team_input_a' value='"+v.goals_a_qnl+"' max='9' min='0' value='0'/>"+
								"<img src='"+v.flag_b_qnl+"' alt=''>"+
								"<span class='team-b'>"+v.team_b_qnl+"</span>"+
								"<input type='number' name='team-b' class='team_input team_input_b' value='"+v.goals_b_qnl+"' max='9' min='0' value='0'/>"+
								"</li>";
					$(".list-matches").append(strqnl);
				})


				var positionTable = new Quiniela.Models.PositionQnl()

				positionTable.urlRoot = "/api/positions/qnlgroup/?group="+choosedGroup+"&codigoqnl="+currentCodqnl;

				positionTable.fetch({
					success:function(table){
						console.log(table)
						$(".body-posiciones table tbody").html("");

						var headerGroup = table.attributes[0].group;
						$(".header-posiciones h3").text("GRUPO "+headerGroup);

						$.each(table.attributes,function(k,val){
							console.log(val);

							var strTable = "<tr>"+
						 						"<td>"+val.team+"</td>"+
						 						"<td>"+val.jj+"</td>"+
						 						"<td>"+val.jg+"</td>"+
						 						"<td>"+val.je+"</td>"+
						 						"<td>"+val.jp+"</td>"+
						 						"<td>"+val.gf+"</td>"+
						 						"<td>"+val.gc+"</td>"+
						 						"<td>"+val.dif+"</td>"+
						 						"<td>"+val.pts+"</td>"+
		 									"</tr>";

		 					$(".body-posiciones table tbody").append(strTable);
						})

					},
					error : function(err){
						console.log(err)
					}
				})
			},

			error: function(error){
				console.log(error)
			}
		})



	},

	saveQnlHandler : function(e){

		$(".loader-quiniela").show();
		
		var currentGroup = sessionStorage.getItem("grupo");
		
		var currentCodqnl = localStorage.getItem("codigoqnl");

		var listMatch = [];
		var objMatch = {};
		var mainMatch = {};

		$.each($(".list-matches li"), function(c,v){
			objMatch = {
				goles_a : $(v).children("input.team_input_a").val(),
				goles_b : $(v).children("input.team_input_b").val(),
				partido : $(v).attr("id"),
				progress : true
			}

			listMatch.push(objMatch);
		})

		mainMatch.data = listMatch

		console.log(mainMatch);

		var updateQnl = new Quiniela.Models.QuinielaUpdate();

		updateQnl.urlRoot = "/api/quiniela/?grupo="+currentGroup+"&codigo="+currentCodqnl;

		updateQnl.save(mainMatch,{
			success :function(response){
				$(".loader-quiniela").hide();
				$(".success-middle").text("Su Progreso en el grupo "+currentGroup+" se ha almacenado");
				$(".success-middle").fadeIn("slow").delay(1000).fadeOut("fast");

				var positionTable = new Quiniela.Models.PositionQnl()

				positionTable.urlRoot = "/api/positions/qnlgroup/?group="+currentGroup+"&codigoqnl="+currentCodqnl;

				positionTable.fetch({
					success:function(table){
						console.log(table)
						$(".body-posiciones table tbody").html("");

						var headerGroup = table.attributes[0].group;
						$(".header-posiciones h3").text("GRUPO "+headerGroup);

						$.each(table.attributes,function(k,val){
							console.log(val);

							var strTable = "<tr>"+
						 						"<td>"+val.team+"</td>"+
						 						"<td>"+val.jj+"</td>"+
						 						"<td>"+val.jg+"</td>"+
						 						"<td>"+val.je+"</td>"+
						 						"<td>"+val.jp+"</td>"+
						 						"<td>"+val.gf+"</td>"+
						 						"<td>"+val.gc+"</td>"+
						 						"<td>"+val.dif+"</td>"+
						 						"<td>"+val.pts+"</td>"+
		 									"</tr>";

		 					$(".body-posiciones table tbody").append(strTable);
						})

					},
					error : function(err){
						console.log(err)
					}
				})
				console.log(response);
			},
			error: function(err){
				console.log("error en el servidor")
				console.log(err);
			}
		})


	},

	showEliminatoriaHandler :function(e){
		var currentCodqnl = localStorage.getItem("codigoqnl");
		var progressQnl = new Quiniela.Models.ProgressQnl();

		progressQnl.urlRoot = "/api/quiniela/progress?codigo="+currentCodqnl;


		progressQnl.fetch({
			success : function(progress){
				if(progress.attributes.cant < 48){
					$(".warning-middle").text("Para ir a la siguiente ronda debes completar la fase de grupos");
					$(".warning-middle").fadeIn("slow").delay(5000).fadeOut("fast");
				}

				if(progress.attributes.cant === 48){
					$(".success-middle").text("Fase de eliminatoria activa");
					$(".success-middle").fadeIn("slow").delay(5000).fadeOut("fast");
				}
			},
			error : function(err){
				$(".error-middle").text("Se ha producido un error intenta iniciar nuevamente");
				$(".success-middle").fadeIn("slow").delay(5000).fadeOut("fast");
			}
		})


	}
})
