$(function(){
	Quiniela.app = new Quiniela.Router();

	Backbone.history.start({
		pushState : true,
		root : "/"
	})

})