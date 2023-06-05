document.addEventListener("click", function (e) {
    if (e.target.classList.contains("painting")) {
        const src = e.target.getAttribute("src");
        const title = e.target.getAttribute("data-title");
        const size = e.target.getAttribute("data-size");
        const details = e.target.getAttribute("data-details");
        document.querySelector(".modal-img").src = src;
        document.querySelector(".modal-img-title").textContent = title;
        document.querySelector(".modal-size").textContent = size;
        document.querySelector(".modal-details").textContent = details;
        const myModal = new bootstrap.Modal(document.getElementById('gallery-modal'));
        myModal.show();
    }
})