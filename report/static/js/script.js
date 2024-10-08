const menuBtn = document.querySelector('.menu img');
const menuItems = document.querySelector('.menu-items');

menuBtn.addEventListener('click', () => {
  menuItems.classList.toggle('show');
});

document.addEventListener('click', (event) => {
  if (!event.target.closest('.menu')) {
    menuItems.classList.remove('show');
  }
});