$(function() {

const category_button = $('.category-wrapper .category');
const project = $('.wrapper .proj .card-body');


const language_code = location.pathname.substring(1, 3);

if (language_code == 'fa') {
  const carousel_number_link = $('.wrapper .proj .CSSgal .bullets a');
  const e2p = s => s.replace(/\d/g, d => '۰۱۲۳۴۵۶۷۸۹'[d]);
  carousel_number_link.each(function(index, element){
    var image_number = $(element).text();
    image_number = e2p(image_number);
    $(element).text(image_number);
  })
}


category_button.click(change_category);
project.click(goToProject)


function change_category(){
  const category = $(this).data('category');
  if (category == 'application') {
    // location.href : http://www.example.com:8000/path?param=foo
    // location.origin : http://www.example.com:8000
    // location.pathname : /path/
    location = location.pathname;
  }else {
    location = location.pathname + '?category=' + category;
  }
}


function goToProject() {
  const project_url = $(this).data('url');
  if (project_url) {
    window.location = project_url;
  }
}




});
