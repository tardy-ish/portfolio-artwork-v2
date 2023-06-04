var tiles = document.querySelectorAll('.img-hover');
var gen_links = document.querySelectorAll('.link-target');

if ("ontouchstart" in document.documentElement)
{
    [...tiles].forEach((tile)=>{
        tile.addEventListener( 'click', function() {
            tile.classList.toggle('is-clicked');
        });
    });
}
else
{
    [...tiles].forEach((tile)=>{
        tile.addEventListener( 'mouseover', function() {
            tile.classList.add('is-clicked');
        });
        tile.addEventListener( 'mouseout', function() {
            tile.classList.remove('is-clicked');
        });
    });
    [...gen_links].forEach((link)=>{
        link.addEventListener( 'mouseover', function() {
            link.classList.add('gen-hover');
        });
        link.addEventListener( 'mouseout', function() {
            link.classList.remove('gen-hover');
        });
    });
}
