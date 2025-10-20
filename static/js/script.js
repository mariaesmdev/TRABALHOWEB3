const mobile = document.getElementById('mobile');
const navLista = document.querySelector('#nav .nav_lista');

mobile.addEventListener('click', () => {
    const isOpen = navLista.classList.toggle('active');
    mobile.classList.toggle('open', isOpen);
    mobile.setAttribute('aria-expanded', String(isOpen));
});