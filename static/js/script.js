const mobile = 
document.getElementById('mobile');
const navLista =
document.getElementById('nav').querySelector('.nav_lista');

mobile.addEventListener('click', () => {
    navLista.classList.toggle('active');
});