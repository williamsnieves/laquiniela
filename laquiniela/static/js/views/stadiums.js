Quiniela.Views.Stadiums = Backbone.View.extend({

	el : $("#stadium-content"),


	template: _.template($("#stadium-template").html()),

	initialize : function(){
		this.render();
		var stadium  = new Quiniela.Models.Stadium();
		stadium.urlRoot = "/api/calendario/Manaos/";
		

		stadium.fetch({
			success : function(infoStadio){	
				console.log(infoStadio);
				$(".list-partidos").html("");
				$("#image-stadium img").attr("src","/static/img/sedes/manaos/amazonia.png")

				//console.log(infoStadio.attributes[0])
				var text = infoStadio.attributes[0].description;


				$(".content-description p").text(text)



				$.each(infoStadio.attributes,function(k,val){
					console.log(val)

					var fecha = new Date(val.date_match);
					var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1)) 

					var str = "<li><div><span class='title-fecha'>fecha</span>"+
					          "<span class='fecha'> "+formato+ "</span></div><img src='"+val.flag_a_match+"' alt=''>"+
					          "<span class='team-a'>"+val.team_a_match+"</span><span class='versus'>VS</span>"+
					          "<img src='"+val.flag_b_match+"' alt=''>"+
					          "<span class='team-b'>"+val.team_b_match+"</span></li>";

					$(".list-partidos").append(str)	
				})
			},

			error : function(err){
				console.log(err)
			}
		})
	},

	events : {
		"click #sedes-list li" : "stadiumClickHandler"
	},

	render : function(){
		var html = this.template()
		this.$el.html(html);

	},

	stadiumClickHandler : function(e){

		var chooseStadium = $(e.target).attr("data-stadium");

		
		

		var stadium  = new Quiniela.Models.Stadium();
		stadium.urlRoot = "/api/calendario/"+chooseStadium;
		

		stadium.fetch({
			success : function(infoStadio){	
				$(".list-partidos").html("");
				console.log(chooseStadium)
				switch(chooseStadium){
					case "Manaos":
						$("#image-stadium img").attr("src","/static/img/sedes/manaos/amazonia.png")
						break;
					case "Fortaleza":
						$("#image-stadium img").attr("src","/static/img/sedes/fortaleza/castelao.png")
						break;
					case "Natal":
						$("#image-stadium img").attr("src","/static/img/sedes/natal/das-dunas.png")
						break;
					case "Recife":
						$("#image-stadium img").attr("src","/static/img/sedes/recife/pernambuco.png")
						break;
					case "Salvador":
						$("#image-stadium img").attr("src","/static/img/sedes/salvador/fonte-nova.png")
						break;
					case "Cuiaba":
						$("#image-stadium img").attr("src","/static/img/sedes/cuiaba/pantanal.png")
						break;
					case "Brasilia":
						$("#image-stadium img").attr("src","/static/img/sedes/brasilia/nacional.png")
						break;
					case "Rio de Janeiro":
						$("#image-stadium img").attr("src","/static/img/sedes/rio/maracana.png")
						break;
					case "Belo Horizonte":
						$("#image-stadium img").attr("src","/static/img/sedes/belo/mineirao.png")
						break;
					case "Sao Paulo":
						$("#image-stadium img").attr("src","/static/img/sedes/sao/sao.png")
						break;
					case "Curitiba":
						$("#image-stadium img").attr("src","/static/img/sedes/curitiba/baixada.png")
						break;
					case "Porto Alegre":
						$("#image-stadium img").attr("src","/static/img/sedes/porto-alegre/beira-rio.png")
						break;
				}


				//console.log(infoStadio.attributes[0])
				var text = infoStadio.attributes[0].description;


				$(".content-description p").text(text)



				$.each(infoStadio.attributes,function(k,val){
					console.log(val)

					var fecha = new Date(val.date_match);
					var formato =  ((fecha.getDate() + 1) + '/' +(fecha.getMonth() + 1)) 

					var str = "<li><div><span class='title-fecha'>fecha</span>"+
					          "<span class='fecha'> "+formato+ "</span></div><img src='"+val.flag_a_match+"' alt=''>"+
					          "<span class='team-a'>"+val.team_a_match+"</span><span class='versus'>VS</span>"+
					          "<img src='"+val.flag_b_match+"' alt=''>"+
					          "<span class='team-b'>"+val.team_b_match+"</span></li>";

					$(".list-partidos").append(str)	
				})
			},

			error : function(err){
				console.log(err)
			}
		})
	}
})
