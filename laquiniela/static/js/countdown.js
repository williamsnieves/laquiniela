$(function(){
	$('#clock').countdown('2014/06/12', function(event) {
     	$(this).html(event.strftime('Faltan %D días %H:%M:%S'));
	});
})