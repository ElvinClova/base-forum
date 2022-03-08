////////////////////////////
/// JavaScript for post page
////////////////////////////

$(function() {
    //exhacute when js-menu-icon is clicked
    $('.js-menu-icon').click(function(){
        // $(this) = js-menu-icon
        // next = the next item = menu
        // if you don't know what toggle means look it up
        $(this).next().toggle();
    })
    
})