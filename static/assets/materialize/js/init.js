// (function($){
//   $(function(){

//     $('.sidenav').sidenav();
//   }); // end of document ready
// })(jQuery); // end of jQuery name space

  // Or with jQuery

  $(document).ready(function(){
    $('.sidenav').sidenav();
  });



//   $(document).ready(function(){
//     $('.fixed-action-btn').floatingActionButton();
//   });

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {
      direction: 'left',
      hoverEnabled: true,
    //   toolbarEnabled: true
    });
  });


//   document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.carousel');
//     var instances = M.Carousel.init(elems, options);
//   });

  // Or with jQuery

  $(document).ready(function(){
    $('.carousel').carousel();
  });


//   var instance = M.Carousel.init({
//     fullWidth: true,
//     indicators: true
//   });

  // Or with jQuery

  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });
      

  $(document).ready(function(){
    $('.collapsible').collapsible();
  });


  $('.dropdown-trigger').dropdown(
      {hover: true},
      {alignment: 'left'}
  );

  $(document).ready(function(){
    $('.tap-target').tapTarget();
  });

  $(document).ready(function(){
    $('.materialboxed').materialbox();
  });

  $(document).ready(function(){
    $('.scrollspy').scrollSpy();
  });

  $(document).ready(function(){
    $('.tabs').tabs();
  });
       
  $(document).ready(function(){
    $('.tooltipped').tooltip();
  });
        
  $(document).ready(function(){
    $('.datepicker').datepicker();
  });

