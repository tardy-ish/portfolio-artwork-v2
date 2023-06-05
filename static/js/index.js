let navlinks = document.getElementsByClassName('nav-link pt-3 px-5') ;

[...navlinks].forEach((navlink)=>{
    navlink.addEventListener( 'click', function() {
        navlink.classList.toggle('active');
    });
});