var controller;
if (Modernizr.touch) {
	var myScroll;
	$(document).ready(function () {
		// wrap for iscroll
		$(".container")
			.addClass("scrollContainer")
			.wrapInner('<div class="scrollContent"></div>');

		// add iScroll
		myScroll = new IScroll('#content-wrapper', {scrollX: false, scrollY: true, scrollbars: true, useTransform: false, useTransition: false, probeType: 3});
	
		// update container on scroll
	myScroll.on("scroll", function () {
		controller.update();
	});

	// overwrite scroll position calculation to use child's offset instead of parents scrollTop();
	controller.scrollPos(function () {
		return -myScroll.y;
	});

	// refresh height, so all is included.
	setTimeout(function () {
	    myScroll.refresh();
	}, 0);

		$(".container").on("touchend", "a", function (e) {
			// a bit dirty workaround for links not working in iscroll for some reason...
			e.preventDefault();
			window.location.href = $(this).attr("href");
		});

	// manual set hight (so height 100% is available within scroll container)
		$(document).on("orientationchange", function () {
			$("section")
				.css("min-height", $(window).height())
				.parent(".scrollmagic-pin-spacer").css("min-height", $(window).height());
		});
		$(document).trigger("orientationchange"); // trigger to init
	});
	// init the controller
	controller = new ScrollMagic({
		container: ".container",
		globalSceneOptions: {
			triggerHook: "onLeave"
		}
	});
} else {
	// init the controller
	controller = new ScrollMagic({
		globalSceneOptions: {
			triggerHook: "onLeave"
		}
	});
}