Quiniela.Views.Dashboard = Backbone.View.extend({

	el : $("#dashboard-content"),

	events : {
		"click #group-list" : "groupHandler",
		"click .positions-dashboard" : "positionsHandler",
		"click .btn-invite" : "inviteHandler",
		"click .btn-send" : "sendHandler",
		"click #close-invitation" : "closeHandler"
	},

	initialize : function(attr){
		this.render();
		$('#ticker1').rssfeed('http://es.fifa.com/worldcup/news/rss.xml',{}, function(e) {
			$(e).find('div.rssBody').vTicker();
		});


		var ranking = new Quiniela.Models.Ranking();

		ranking.fetch({
			success : function(response){
				$.each(response.attributes, function(c,v){
					var count = c;
					count++
					var str = "<tr>"+
					"<td><span><p>"+count+"</p></span>"+v.cod_qnl+"</td>"+
					"<td>"+v.points+"</td>";
					$("#ranking tbody").append(str)
				})
			},
			error : function(err){
				console.log(err)
			}
		})


		this.options = attr;
		//console.log(this.options._id)
		//$(".titulo-team span").text(this.options._id)

		if(this.options._id !== null){
			$(".content-puntos").fadeIn("fast");
			$("#container-team-quiniela h3.titulo-team").fadeIn("fast");

		    var positionTable = new Quiniela.Models.PositionQnl()

		
			positionTable.urlRoot = "/api/positions/qnlgroup/?group=A&codigoqnl="+this.options._id;


			positionTable.fetch({
				success:function(table){
					$(".table-positions table tbody").html("");

					var headerGroup = table.attributes[0].group;

					$.each(table.attributes,function(k,val){

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

	 					$(".table-positions table tbody").append(strTable);
					})

				},
				error : function(err){
					console.log(err)
				}
			})

		}else{
			var oficiales = new Quiniela.Models.Position()

			oficiales.urlRoot = "/api/position/A";

			oficiales.fetch({
				success :function(oficiales){

					$.each(oficiales.attributes,function(k,val){					

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

	 					$(".table-positions table tbody").append(strTable);
					})
				},

				error: function(error){
					console.log(error)
				}
			})

			var matches = new Quiniela.Models.QuinielaList()
			 matches.urlRoot = "/api/oficialsmatches/?group=A";


			 matches.fetch({
			 	success : function(response){

			 		console.log("aquii")
			 		console.log(response)
			 		for(var i = 0; i < 4 ; i++){
			 			var fecha = new Date(response.attributes[i].date_match);
					    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1));

			 			var matchstr = "<div class='item partidos-dashboard' style='border:1px solid blue'>"+
						"<div class='team-a'>"+
							"<p class='team'>"+response.attributes[i].team_a_match+"</p>"+
							"<p class='result'>"+response.attributes[i].goals_a_match+"</p>"+
						"</div>"+
						"<span>VS</span>"+
						"<div class='team-b'>"+
							"<p class='team'>"+response.attributes[i].team_b_match+"</p>"+
							"<p class='result'>"+response.attributes[i].goals_b_match+"</p>"+
						"</div>"+
						"<div class='team-place'>"+
							"<p class='city-dash'>Ciudad :"+response.attributes[i].city_match+"</p>"+
							"<p class='fecha-dash'>Fecha :"+formato+"</p>"+
							"<p class='fase-title'>Fase de Grupo</p>"+
							"<p class='fase-group'>Grupo "+response.attributes[i].group_match+"</p>"+
						"</div>"+
					"</div>";
				 		$("#content-left-dashboard .content-matches").prepend(matchstr)
			 		}
			 		
			 		$.each(response.attributes,function(c,v){
						console.log(v);
						var fecha = new Date(v.date_match);
					    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1))

						var strqnl = "<tr>"+
						      "<td><span style='display:block'>estadio</span>"+v.city_match+"</td>"+
						      "<td><span style='display:block'>fecha</span>"+formato+"</td>"+
						      "<td><img src='"+v.flag_a_match+"' alt=''></td>"+
						      "<td>"+v.team_a_match+"</td>"+
						      "<td><span class='input-read'>"+v.goals_a_match+"</span></td>"+
						      "<td><img src='"+v.flag_b_match+"' alt=''></td>"+
						      "<td>"+v.team_b_match+"</td>"+
						      "<td><span class='input-read'>"+v.goals_b_match+"</span></td>"+
						    "</tr>";

						$(".table-results table tbody").append(strqnl);
					})
			 	},
			 	error : function(err){
			 		console.log(err)
			 	}
			 })
		}

		$("#container-team-quiniela h3.titulo-team #codigo").text(this.options._id);
		var listQuinielas = new Quiniela.Models.QuinielaList();
		listQuinielas.urlRoot = "/api/quinielas/list/"
		 listQuinielas.fetch({
		 	success : function(response){
		 		console.log(response.attributes);
		 		$.each(response.attributes,function(c,v){
		 			//console.log(v.fields.cod_qnl)
		 			$("#qnl-list").append("<li><a href='"+v.fields.cod_qnl+"'><span>"+v.fields.cod_qnl+"</span></a></li>")
		 		})
	
		 	},
		 	error : function(err){

		 	}
		 })


		 var dashboardQnl = new Quiniela.Models.QuinielaList()
		 dashboardQnl.urlRoot = "/api/quinielas/?group=A&codqnl="+this.options._id;

		 dashboardQnl.fetch({
		 	success : function(response){
		 		console.log(response)
		 		for(var i = 0; i < 4 ; i++){
		 			var fecha = new Date(response.attributes[i].date_qnl);
				    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1));

		 			var matchstr = "<div class='item partidos-dashboard' style='border:1px solid blue'>"+
					"<div class='team-a'>"+
						"<p class='team'>"+response.attributes[i].team_a_qnl+"</p>"+
						"<p class='result'>"+response.attributes[i].goals_a_qnl+"</p>"+
					"</div>"+
					"<span>VS</span>"+
					"<div class='team-b'>"+
						"<p class='team'>"+response.attributes[i].team_b_qnl+"</p>"+
						"<p class='result'>"+response.attributes[i].goals_b_qnl+"</p>"+
					"</div>"+
					"<div class='team-place'>"+
						"<p class='city-dash'>Ciudad :"+response.attributes[i].city_match+"</p>"+
						"<p class='fecha-dash'>Fecha :"+formato+"</p>"+
						"<p class='fase-title'>Fase de Grupo</p>"+
						"<p class='fase-group'>Grupo "+response.attributes[i].group_qnl+"</p>"+
					"</div>"+
				"</div>";
			 		$("#content-left-dashboard .content-matches").prepend(matchstr)
	 			}
		 		$.each(response.attributes,function(c,v){
					console.log(v);
					var fecha = new Date(v.date_qnl);
				    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1))

					var strqnl = "<tr>"+
					      "<td><span style='display:block'>estadio</span>"+v.city_match+"</td>"+
					      "<td><span style='display:block'>fecha</span>"+formato+"</td>"+
					      "<td><img src='"+v.flag_a_qnl+"' alt=''></td>"+
					      "<td>"+v.team_a_qnl+"</td>"+
					      "<td><span class='input-read'>"+v.goals_a_qnl+"</span></td>"+
					      "<td><img src='"+v.flag_b_qnl+"' alt=''></td>"+
					      "<td>"+v.team_b_qnl+"</td>"+
					      "<td><span class='input-read'>"+v.goals_b_qnl+"</span></td>"+
					    "</tr>";

					$(".table-results table tbody").append(strqnl);
				})
		 	},
		 	error : function(err){
		 		console.log(err)
		 	}
		 })
	},

	render : function(){
		this.$el.html(_.template($("#dashboard-template").html()));
	},

	groupHandler : function(e){
		var choosedGroup = e.target.innerText;

		$(".table-results table tbody").html("");

		if(this.options._id !== null){
			var dashboardQnl = new Quiniela.Models.QuinielaList()
			dashboardQnl.urlRoot = "/api/quinielas/?group="+choosedGroup+"&codqnl="+this.options._id;
			$("#content-left-dashboard .content-matches").html("")
			dashboardQnl.fetch({
		 	success : function(response){
		 		console.log(response)
		 		for(var i = 0; i < 4 ; i++){
		 			var fecha = new Date(response.attributes[i].date_qnl);
				    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1));

		 			var matchstr = "<div class='item partidos-dashboard' style='border:1px solid blue'>"+
					"<div class='team-a'>"+
						"<p class='team'>"+response.attributes[i].team_a_qnl+"</p>"+
						"<p class='result'>"+response.attributes[i].goals_a_qnl+"</p>"+
					"</div>"+
					"<span>VS</span>"+
					"<div class='team-b'>"+
						"<p class='team'>"+response.attributes[i].team_b_qnl+"</p>"+
						"<p class='result'>"+response.attributes[i].goals_b_qnl+"</p>"+
					"</div>"+
					"<div class='team-place'>"+
						"<p class='city-dash'>Ciudad :"+response.attributes[i].city_match+"</p>"+
						"<p class='fecha-dash'>Fecha :"+formato+"</p>"+
						"<p class='fase-title'>Fase de Grupo</p>"+
						"<p class='fase-group'>Grupo "+response.attributes[i].group_qnl+"</p>"+
					"</div>"+
				"</div>";
			 		$("#content-left-dashboard .content-matches").prepend(matchstr)
	 			}
		 		$.each(response.attributes,function(c,v){
					console.log(v);
					var fecha = new Date(v.date_qnl);
				    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1))

					var strqnl = "<tr>"+
					      "<td><span style='display:block'>estadio</span>"+v.city_match+"</td>"+
					      "<td><span style='display:block'>fecha</span>"+formato+"</td>"+
					      "<td><img src='"+v.flag_a_qnl+"' alt=''></td>"+
					      "<td>"+v.team_a_qnl+"</td>"+
					      "<td><span class='input-read'>"+v.goals_a_qnl+"</span></td>"+
					      "<td><img src='"+v.flag_b_qnl+"' alt=''></td>"+
					      "<td>"+v.team_b_qnl+"</td>"+
					      "<td><span class='input-read'>"+v.goals_b_qnl+"</span></td>"+
					    "</tr>";

					$(".table-results table tbody").append(strqnl);
				})
		 	},
		 	error : function(err){
		 		console.log(err)
		 	}
		 })
		}else{
			var matches = new Quiniela.Models.QuinielaList()
			matches.urlRoot = "/api/oficialsmatches/?group="+choosedGroup;
			$("#content-left-dashboard .content-matches").html("")
			matches.fetch({
				 	success : function(response){
				 		console.log(response)

				 		for(var i = 0; i < 4 ; i++){
				 			var fecha = new Date(response.attributes[i].date_match);
						    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1));

				 			var matchstr = "<div class='item partidos-dashboard' style='border:1px solid blue'>"+
							"<div class='team-a'>"+
								"<p class='team'>"+response.attributes[i].team_a_match+"</p>"+
								"<p class='result'>"+response.attributes[i].goals_a_match+"</p>"+
							"</div>"+
							"<span>VS</span>"+
							"<div class='team-b'>"+
								"<p class='team'>"+response.attributes[i].team_b_match+"</p>"+
								"<p class='result'>"+response.attributes[i].goals_b_match+"</p>"+
							"</div>"+
							"<div class='team-place'>"+
								"<p class='city-dash'>Ciudad :"+response.attributes[i].city_match+"</p>"+
								"<p class='fecha-dash'>Fecha :"+formato+"</p>"+
								"<p class='fase-title'>Fase de Grupo</p>"+
								"<p class='fase-group'>Grupo "+response.attributes[i].group_match+"</p>"+
							"</div>"+
						"</div>";
					 		$("#content-left-dashboard .content-matches").prepend(matchstr)
			 			}


				 		$.each(response.attributes,function(c,v){
							console.log(v);
							var fecha = new Date(v.date_match);
						    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1))

							var strqnl = "<tr>"+
							      "<td><span style='display:block'>estadio</span>"+v.city_match+"</td>"+
							      "<td><span style='display:block'>fecha</span>"+formato+"</td>"+
							      "<td><img src='"+v.flag_a_match+"' alt=''></td>"+
							      "<td>"+v.team_a_match+"</td>"+
							      "<td><span class='input-read'>"+v.goals_a_match+"</span></td>"+
							      "<td><img src='"+v.flag_b_match+"' alt=''></td>"+
							      "<td>"+v.team_b_match+"</td>"+
							      "<td><span class='input-read'>"+v.goals_b_match+"</span></td>"+
							    "</tr>";

							$(".table-results table tbody").append(strqnl);
						})
				 	},
				 	error : function(err){
				 		console.log(err)
				 	}
				 })
		}


		

		



	},

	positionsHandler : function(e){
		//alert(e.target.innerText);
		var choosedGroup = e.target.innerText
		var positionTable = new Quiniela.Models.PositionQnl()

		if(this.options._id !== null)
			positionTable.urlRoot = "/api/positions/qnlgroup/?group="+choosedGroup+"&codigoqnl="+this.options._id;
		else
			positionTable.urlRoot = "/api/position/"+choosedGroup;

		positionTable.fetch({
			success:function(table){
				$(".table-positions table tbody").html("");

				var headerGroup = table.attributes[0].group;

				$.each(table.attributes,function(k,val){

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

 					$(".table-positions table tbody").append(strTable);
				})

			},
			error : function(err){
				console.log(err)
			}
		})

	},

	inviteHandler : function(e){
		$(".invitations").slideDown('fast');
	},

	sendHandler : function(e){
		e.preventDefault();
		$(".loader-invitation").show()
		var invitacioObj = {}
		var mailsInvitados = [];
		var temp = [];
		var tempObj = {}

		var emails = $("#email-invitation").val()

		temp = emails.split(",");

		$.each(temp, function(c,v){
			console.log(v);
			tempObj = {
				email : v
			}

			mailsInvitados.push(tempObj)

		})

		//$.each()
		invitacioObj.data = {
			invitacion : 1,
			invitados  : mailsInvitados
		}

		console.log(invitacioObj);

		var invitacion = new Quiniela.Models.QuinielaInvitation();

		invitacion.urlRoot = "/api/quiniela/invitation/save"

		invitacion.save(invitacioObj,{
			success : function(response){
				$(".loader-invitation").hide()
				console.log(response)
				$(".alert-success").text("Listo!!! Tus invitaciones fueron enviadas");
				$("#email-invitation").val("");
				$(".alert-success").fadeIn("slow").delay(3000).fadeOut("fast",function(){
					$(".invitations").slideUp("slow")
				});				
				
			},
			error : function(err){
				console.log(err)
				$(".loader-invitation").hide()
				$(".alert-danger").text("Tenemos problemas vuelve a intentar mas tardea");
				$("#email-invitation").val("");
				$(".alert-danger").fadeIn("slow").delay(3000).fadeOut("fast",function(){
				 	$(".invitations").slideUp("slow")
				});
				
			}
		})


	
	},
	closeHandler : function(e){
		$(".invitations").slideUp("slow")
	}

	
})