//darkmode.js
//credits: https://codyhouse.co/blog/post/dark-light-switch-css-javascript

const DarkTheme = document.getElementById('DarkTheme');
window.addEventListener('load', () => {
  if (DarkTheme) {
    //if theme selected initialize it! 
    Initialize(); 
    DarkTheme.addEventListener('change', () => {
    //otherwise reset theme
    Reset();
    });
  }
});

function Initialize() {
  const themeSelected =
    localStorage.getItem('DarkTheme') !== null &&
    localStorage.getItem('DarkTheme') === 'dark';
    //update checkbox
    DarkTheme.checked = themeSelected;
    //update body
    themeSelected ? document.body.setAttribute('data-theme', 'dark') :
    document.body.removeAttribute('data-theme');
}

function Reset() {
  if (DarkTheme.checked) {
    document.body.setAttribute('data-theme', 'dark');
    //store settings in localstorage
    localStorage.setItem('DarkTheme', 'dark');
  } else {
    document.body.removeAttribute('data-theme');
    localStorage.removeItem('DarkTheme');
  }
}
