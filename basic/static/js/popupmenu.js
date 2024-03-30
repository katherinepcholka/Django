let popupButtons = document.querySelectorAll(".popup-button");
let popupMenu = document.querySelector(".popup-menu");
let closeButton = document.querySelector(".popupmenu-closebutton");

popupButtons.forEach((elem) => {
    elem.addEventListener("click", () => showPopupMenu());
});

closeButton.addEventListener("click", () => closePopupMenu());

function showPopupMenu() {
    popupMenu.style.display = "flex";
}

function closePopupMenu() {
    popupMenu.style.display = "none";
}