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

						$(".new-quiniela").slideUp("slow");
						$("#team-container").fadeIn("slow");
						$("#quiniela-body").fadeIn("slow");


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
	}
})
