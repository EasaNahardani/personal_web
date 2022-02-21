window.init_progress = function(progress) {
  var el = progress.querySelector('.progress-text');
  var final_value = el.dataset.progress;
	var x = progress.querySelector('.progress-circle-prog');
  x.style.strokeDasharray = (final_value * 4.65) + ' 999';
  var from = 0;
	var start = new Date().getTime();

	setTimeout(function() {
	    var now = (new Date().getTime()) - start;
	    var prog = now / 700;
		  result = final_value > from ? Math.floor((final_value - from) * prog + from) : Math.floor(from - (from - final_value) * prog);
	    el.innerHTML = prog < 1 ? result+'%' : final_value+'%';
	    if (prog < 1) setTimeout(arguments.callee, 10);
	}, 10);
}

function initialize_progresses() {
  const progresses = document.querySelectorAll(".progress");
  for (let i = 0; i < progresses.length; i++) {
    window.init_progress(progresses[i]);
  }

}

setTimeout(window.initialize_progresses, 200);
