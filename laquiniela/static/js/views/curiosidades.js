Quiniela.Views.Curiosidades = Backbone.View.extend({

	el : $("#curiosidad-content"),

	initialize : function(){
		this.render();
		var curiosidad  = new Quiniela.Models.QuinielaCuriosity();
		curiosidad.urlRoot = "/api/curiosidades/?ano=1930";
		

		curiosidad.fetch({
			success : function(data){
				console.log(data)
				$(".container-description h3").html(data.attributes[0].pais_sede+"<span>"+data.attributes[0].ano_mundial+"</span>")
				$(".container-description .curiosidad-description").text(data.attributes[0].descripcion)

				$(".curiosidades-campeon h3").text(data.attributes[0].campeon)
				$(".curiosidades-subcampeon h3").text(data.attributes[0].subcampeon)

				$(".curiosidades-tercero h3").text(data.attributes[0].tercero)
				$(".curiosidades-cuarto h3").text(data.attributes[0].cuarto)

				$(".container-curiosity p").text(data.attributes[0].curiosidad)

				$(".estadisticas-mundiales .goleador p").text(data.attributes[0].copa)
				$(".estadisticas-mundiales .goles p").text(data.attributes[0].cant_equipos)
				$(".estadisticas-mundiales .balonoro p").text(data.attributes[0].cant_partidos)

				$(".wrapper-curiosity .cant-gol span").text(data.attributes[0].cant_goles)
				$(".wrapper-curiosity .pro-gol span").text(data.attributes[0].promedio_goles)
				$(".wrapper-curiosity .cant-golea span").text(data.attributes[0].max_goles)
				$(".wrapper-curiosity .golea span").text(data.attributes[0].goleadores)
			},
			error : function(err){
				console.log(err)
			}
		})
	},

	events : {
		"click #sedes-list li" : "anosClickHandler"
	},

	render : function(){
		this.$el.html(_.template($("#curiosidad-template").html()));

	},

	anosClickHandler : function(e){

		var chooseAno = $(e.target).attr("data-mundial");

		var curiosidad  = new Quiniela.Models.QuinielaCuriosity();
		curiosidad.urlRoot = "/api/curiosidades/?ano="+chooseAno;
		

		curiosidad.fetch({
			success : function(data){
				console.log(data)
				$(".container-description h3").html(data.attributes[0].pais_sede+"<span>"+data.attributes[0].ano_mundial+"</span>")
				$(".container-description .curiosidad-description").text(data.attributes[0].descripcion)

				$(".curiosidades-campeon h3").text(data.attributes[0].campeon)
				$(".curiosidades-subcampeon h3").text(data.attributes[0].subcampeon)

				$(".curiosidades-tercero h3").text(data.attributes[0].tercero)
				$(".curiosidades-cuarto h3").text(data.attributes[0].cuarto)

				$(".container-curiosity p").text(data.attributes[0].curiosidad)

				$(".estadisticas-mundiales .goleador p").text(data.attributes[0].copa)
				$(".estadisticas-mundiales .goles p").text(data.attributes[0].cant_equipos)
				$(".estadisticas-mundiales .balonoro p").text(data.attributes[0].cant_partidos)

				$(".wrapper-curiosity .cant-gol span").text(data.attributes[0].cant_goles)
				$(".wrapper-curiosity .pro-gol span").text(data.attributes[0].promedio_goles)
				$(".wrapper-curiosity .cant-golea span").text(data.attributes[0].max_goles)
				$(".wrapper-curiosity .golea span").text(data.attributes[0].goleadores)
			},
			error : function(err){
				console.log(err)
			}
		})

	}
})
