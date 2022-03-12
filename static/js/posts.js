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

// // ul.addEventListener('click', (event) => {
//     if(event.target.tagtame === 'a'){
//         const a = event.target; 
//         const POST = body.parentNode;
//         const post_form = POST.parentNode;
//         if(a.textContent === 'edit' ){
//         const body = POST.secondElementChild;
//         const input = document.createElement('input');
//         input.type = 'text';
//         input.value = a.textContent;
//         POST.removeChild(body);
//         a.textContent = 'save'; }
//         else if(a.textContent === 'save'){
//         const input = POST.secondElementChild;
//         const POST = document.createElement('POST');
//         POST.textContent = input.value;
//         POST.removeChild(POST);
//         a.textContent = 'edit';        
//             } 

        
//     }

// })