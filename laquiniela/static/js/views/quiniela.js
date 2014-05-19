Quiniela.Views.Quinielas = Backbone.View.extend({

	el : $("#quiniela-content"),

	events : {
		"click .btnquiniela" : "quinielaHandler",
		"click #group-list" : "groupHandler"
	},

	template: _.template($("#quiniela-template").html()),

	initialize : function(){
		this.render();
		//console.log($('#myModal'))
		$(".new-quiniela").fadeIn("slow");
	},

	render : function(){
		var html = this.template()
		this.$el.html(html);
	},

	quinielaHandler : function(e){
		$(".loader").show();

		var quiniela =  new Quiniela.Models.QuinielaNueva()

		quiniela.fetch({
			success : function(response){
				$(".list-matches").html("");
				var currentCodqnl = response.attributes.codqnl;
				localStorage["codigoqnl"] = currentCodqnl;
				var defaultQnl = new Quiniela.Models.QuinielaUpdate()
				defaultQnl.urlRoot = "/api/quinielas/?group=A&codqnl="+currentCodqnl;



				defaultQnl.fetch({
					success : function(quiniela){
						console.log("traigo lo que muestro de la quiniela");
						console.log(quiniela)

						$.each(quiniela.attributes,function(c,v){
							console.log(v);
							var fecha = new Date(v.date_qnl);
						    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1))
							var strqnl = "<li><div class='qnl_stadium'>"+
											"<span class='title-estadio'>Sede</span>"+
											"<span class='name-estadio'>"+v.city_match+"</span>"+
										"</div>"+
										"<div class='qnl_date'>"+
											"<span class='title-fecha'>Fecha</span>"+
											"<span class='fecha'>"+formato+"</span>"+
										"</div>"+
										"<img src='"+v.flag_a_qnl+"' alt=''>"+
										"<span class='team-a'>"+v.team_a_qnl+"</span>"+
										"<input type='text' name='team' class='team_input' value='0'/>"+
										"<img src='"+v.flag_b_qnl+"' alt=''>"+
										"<span class='team-b'>"+v.team_b_qnl+"</span>"+
										"<input type='text' name='team' class='team_input'  value='0'/>"+
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
				$(".loader").hide();
				/*$(".new-quiniela").slideUp("slow");
				$("#team-container").fadeIn("slow");
				$("#quiniela-body").fadeIn("slow");*/
				console.log("entre en el success");
				console.log(response)
			},
			error:function(err){
				console.log("entre en el error");
				console.log(response)
			}
		})

		/*$(".new-quiniela").slideUp("slow");
		$("#team-container").fadeIn("slow");
		$("#quiniela-body").fadeIn("slow");*/
	},

	groupHandler : function(e){
		var choosedGroup = e.target.innerText;
		alert(choosedGroup)

		var currentCodqnl = localStorage.getItem("codigoqnl");

		$(".list-matches").html("");

		var defaultQnl = new Quiniela.Models.QuinielaUpdate()
		defaultQnl.urlRoot = "/api/quinielas/?group="+choosedGroup+"&codqnl="+currentCodqnl;

		defaultQnl.fetch({
			success : function(quiniela){
				console.log(quiniela)

				$.each(quiniela.attributes,function(c,v){
					console.log(v);
					var fecha = new Date(v.date_qnl);
				    var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1))
					var strqnl = "<li><div class='qnl_stadium'>"+
									"<span class='title-estadio'>Sede</span>"+
									"<span class='name-estadio'>"+v.city_match+"</span>"+
								"</div>"+
								"<div class='qnl_date'>"+
									"<span class='title-fecha'>Fecha</span>"+
									"<span class='fecha'>"+formato+"</span>"+
								"</div>"+
								"<img src='"+v.flag_a_qnl+"' alt=''>"+
								"<span class='team-a'>"+v.team_a_qnl+"</span>"+
								"<input type='text' name='team' class='team_input' value='0'/>"+
								"<img src='"+v.flag_b_qnl+"' alt=''>"+
								"<span class='team-b'>"+v.team_b_qnl+"</span>"+
								"<input type='text' name='team' class='team_input'  value='0'/>"+
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



	}
})
