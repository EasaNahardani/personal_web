

  $(document).ready(function(){
    // $(window).load event is not supported by JQuery 3.x
    // use $(document).ready() instead of it

    function opent_envelope() {
      const error_inputes = $('.latter-control.error');
      if (error_inputes.length) {
        $('.envelope').addClass('open');
      }
    }

    setTimeout(function() {
      opent_envelope();
    }, 50)

  });
