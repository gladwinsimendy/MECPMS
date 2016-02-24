$(document).ready(function(){
   // $(".button-collapse").sideNav();
   $('.button-collapse').sideNav({
      menuWidth: 220, // Default is 240
      edge: 'left', // Choose the horizontal origin
      //closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    }
  );
   $('.collapsible').collapsible();
});