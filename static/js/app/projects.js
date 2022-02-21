$(function() {

const category_button = $('.category-wrapper .category');
const project = $('.wrapper .proj .card-body');

category_button.click(change_category);

project.click(goToProject)

function change_category(){
  const category = $(this).data('category');
  if (category == 'application') {
    location = location.origin +  '/projects';
  }else {
    location = location.origin + '/projects?category=' + category;
  }
}


function goToProject() {
  const project_url = $(this).data('url');
  if (project_url) {
    window.location = project_url;
  }
}




});
