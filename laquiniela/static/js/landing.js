$(function(){
	var numeros = $(".numbers-quiniela img");
  				//var elements = $(".hand-vacia img");
  				var quiniela_llena = $(".hand-llena img");
  				var jugador = $(".jugador-quiniela img");
  				var pelota_jugador = $(".ball-jugador-quiniela img");
  				var numero1_jugador = $(".numero1-quiniela img");
  				var numero2_jugador = $(".numero2-quiniela img");

  				var portero = $(".portero-quiniela img");
  				var pelota_portero = $(".ball-portero-quiniela img");
  				var numero1_portero = $(".numero1-portero-quiniela img");
  				var numero2_portero = $(".numero2-portero-quiniela img");

  				var sceneOptions = {duration: 200, offset: -100};
  				var sceneJugador = {duration: 1000, offset: 0};
  				var scenePortero = {duration: 5000, offset: 0};
  				var sceneBall = {duration: 1000, offset: 0};
  				var sceneBall2 = {duration: 1000, offset: 0};

  				var anim = new TimelineMax()
					// pin move down
					.add(TweenMax.from(numeros, 1, {autoAlpha: 0}))
					.add(TweenMax.from(numeros, 1, {left: "-50%", marginLeft: -200, ease: Back.easeOut}));
					// wipe
					
				
				// fade
				new ScrollScene(sceneOptions)
					.addTo(controller)
					.triggerHook("onCenter")
					.triggerElement(numeros)
					.setTween(anim);

				

				// fade
				

				new ScrollScene(sceneOptions)
					.addTo(controller)
					.triggerHook("onCenter")
					.triggerElement(quiniela_llena)
					.setTween(TweenMax.from(quiniela_llena, 1, {autoAlpha: 0}));

				new ScrollScene(sceneJugador)
					.addTo(controller)
					.triggerHook("onCenter")
					.triggerElement(jugador)
					.setTween(TweenMax.from(jugador, 1, {left: "50px", marginLeft: 600, ease: Back.easeOut}));


			new ScrollScene(sceneBall)
				.addTo(controller)
				.triggerHook("onCenter")
				.triggerElement(pelota_jugador)
				.setTween(TweenMax.to(pelota_jugador, 1, {top:"50px", marginTop: 300, left: "50px", marginLeft: 600, ease: Back.easeOut}));

			new ScrollScene(sceneOptions)
					.addTo(controller)
					.triggerHook("onCenter")
					.triggerElement(numero1_jugador)
					.setTween(TweenMax.from(numero1_jugador, 1, {autoAlpha: 0}));


			new ScrollScene(sceneOptions)
				.addTo(controller)
				.triggerHook("onCenter")
				.triggerElement(numero2_jugador)
				.setTween(TweenMax.from(numero2_jugador, 1, {autoAlpha: 0}));


			new ScrollScene(scenePortero)
					.addTo(controller)
					.triggerHook("onCenter")
					.triggerElement(portero)
					.setTween(TweenMax.to(portero, 1, {top:"-50px", marginTop: -300, left: "50px", marginLeft: 600, ease: Back.easeOut}));


			new ScrollScene(sceneBall2)
				.addTo(controller)
				.triggerHook("onCenter")
				.triggerElement(pelota_portero)
				.setTween(TweenMax.from(pelota_portero, 1, {autoAlpha: 0}));

			new ScrollScene(sceneOptions)
					.addTo(controller)
					.triggerHook("onCenter")
					.triggerElement(numero1_portero)
					.setTween(TweenMax.from(numero1_portero, 1, {autoAlpha: 0}));


			new ScrollScene(sceneOptions)
				.addTo(controller)
				.triggerHook("onCenter")
				.triggerElement(numero2_portero)
				.setTween(TweenMax.from(numero2_portero, 1, {autoAlpha: 0}));
})