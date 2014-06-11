Quiniela.Views.Oficiales = Backbone.View.extend({

	el : $("#posiciones-content"),

	events: {
		"click #group-list" : "groupHandler"
	},

	initialize : function(){
		this.render();

		var oficiales = new Quiniela.Models.Position()

		oficiales.urlRoot = "/api/position/A";

		oficiales.fetch({
			success :function(oficiales){
				var headerGroup = oficiales.attributes[0].group;
				$(".header-oficial h3").text("GRUPO "+headerGroup);

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

 					$(".body-oficial table tbody").append(strTable);
				})
			},

			error: function(error){
				console.log(error)
			}
		})
	},

	render : function(){
		this.$el.html(_.template($("#posiciones-template").html()));
	},

	groupHandler : function(e){
		var choosedGroup = e.target.innerText;
		$(".body-oficial table tbody").html("")

		var oficiales = new Quiniela.Models.Position()

		oficiales.urlRoot = "/api/position/"+choosedGroup;

		oficiales.fetch({
			success :function(oficiales){
				var headerGroup = oficiales.attributes[0].group;
				$(".header-oficial h3").text("GRUPO "+headerGroup);

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

 					$(".body-oficial table tbody").append(strTable);
				})
			},

			error: function(error){
				console.log(error)
			}
		})
	}

	
})
