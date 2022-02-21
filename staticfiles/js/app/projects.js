$(function() {

const category_button = $('.category-wrapper .category');

category_button.click(change_category);

function change_category(){
  const category = $(this).data('category');
  if (category == 'application') {
    location = location.origin +  '/projects';
  }else {
    location = location.origin + '/projects?category=' + category;
  }
}


});
