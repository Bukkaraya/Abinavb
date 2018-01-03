$( document ).ready(function() {
    $('.navbar-burger').click(function() {
        $(this).toggleClass('is-active');
        $('#navbarMenuHeroA').toggleClass('is-active');
    });
});