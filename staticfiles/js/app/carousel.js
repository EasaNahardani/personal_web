$(function() {


  link2slider = function(link){
    var link_el = $(link);
    const target = link_el.data('target');
    var bullets = link_el.parent();
    bullets.siblings('s.current').removeClass('current');
    bullets.siblings(`#${target}`).addClass('current');
  }


});
