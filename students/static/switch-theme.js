// switch-theme.js
const themeButton = document.getElementById('theme-button');
const themeStylesheet = document.getElementById('theme-stylesheet');

themeButton.addEventListener('click', () => {
  if (themeStylesheet.getAttribute('href') === '/static/styles-dark.css') {
    themeStylesheet.setAttribute('href', '/static/styles-light.css');
  } else {
    themeStylesheet.setAttribute('href', '/static/styles-dark.css');
  }
});
