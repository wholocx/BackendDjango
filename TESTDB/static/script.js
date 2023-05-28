window.onload = function() {
    document.addEventListener("click", actionsClick);

    function actionsClick(e) {
        const targetElement = e.target;
        
        if (targetElement.classList.contains('actions__buttons')) {
            document.querySelector('.popup').classList.toggle('open');
        } else if ((!targetElement.closest('.popup__wrap') && document.querySelector('.popup.open')) || targetElement.classList.contains('popup__buttons_actions')) {
            document.querySelector('.popup').classList.remove('open');
        }
    }

    function popupAdd(popup) {
        popup.classList.add('open');
    }
}