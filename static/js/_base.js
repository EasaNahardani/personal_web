$(document).ready(function(){
  var myStorage = localStorage;
  var delay = 16;
  var opacity = 1;
  var alert = $('.messages .alert').not('.important');
  const important_alert = $('.messages .important');
  const close_btn = $('.messages .close');
  var target_to_fading = alert;
  var block_fading = false;
  const language_switcher = $('.lang-switcher');
  const first_flag = language_switcher.children().first();



  function shift_flags() {
    var is_shifted = first_flag.hasClass('current');
    if (!is_shifted) {
      const current_flag = language_switcher.find('.current')[0];
      first_flag.before(current_flag);
    }
  }

  shift_flags();


  close_btn.click(close_alert)


  function fade_alert() {
      block_fading = true;
      setTimeout(function() {
        opacity -= 0.003;
        if (opacity < 0.15) {
          const ul = target_to_fading.parent();
          target_to_fading.remove();
          if (!ul.find('li').length) {
            ul.remove();
            alert = undefined;
          }
          block_fading = false;
          return ;
        }else {
          target_to_fading.css('opacity', opacity);
        }
        fade_alert();
      }, delay)
  }


function check_to_fading() {
  let id  = setInterval(function(){
    if (alert) {
      if (!block_fading ) {
        opacity = 1;
        target_to_fading = alert;
        fade_alert();
        clearInterval(id);
      }
    }else {
      clearInterval(id);
    }
  }, 300)
}



// all alerts except important alert
if (alert.length) {
  setTimeout(function() {
    check_to_fading();
  }, 4000)
}


var home_visits = myStorage.getItem('homeVisits');
if (!home_visits) {
  myStorage.setItem('homeVisits', 1);
}else if (!myStorage.getItem('alertClicked')) {
  important_alert.addClass('show');
}


function close_alert() {
  var target = $(this).parent().parent();
  if (target.hasClass('important')) {
    myStorage.setItem('alertClicked', true)
  }
  delay = 5;
  if (!block_fading) {
    opacity = 1;
    target_to_fading = target;
    fade_alert();
  }else {
    const ul = target.parent();
    target.remove();
    if (!ul.find('li').length) {
      ul.remove();
      block_fading = true;
      alert = undefined;
    }
  }
}





});
