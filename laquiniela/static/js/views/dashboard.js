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

		this.options = attr;
		//console.log(this.options._id)
		//$(".titulo-team span").text(this.options._id)

		if(this.options._id !== null){
			$(".content-puntos").fadeIn("fast");
			$("#container-team-quiniela h3.titulo-team").fadeIn("fast");
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

		var dashboardQnl = new Quiniela.Models.QuinielaList()
		dashboardQnl.urlRoot = "/api/quinielas/?group="+choosedGroup+"&codqnl="+this.options._id;

		dashboardQnl.fetch({
		 	success : function(response){
		 		console.log(response)
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

	positionsHandler : function(e){

		var choosedGroup = e.target.innerText
		var positionTable = new Quiniela.Models.PositionQnl()

		positionTable.urlRoot = "/api/positions/qnlgroup/?group="+choosedGroup+"&codigoqnl="+this.options._id;

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
				console.log(response)
			},
			error : function(err){
				console.log(err)
			}
		})


	
	},
	closeHandler : function(e){
		$(".invitations").slideUp("slow")
	}

	
})