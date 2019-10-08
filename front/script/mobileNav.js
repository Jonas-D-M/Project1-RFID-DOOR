function toggleNav() {
  let toggleTrigger = document.querySelectorAll('.js-toggle-nav');
  for (let i = 0; i < toggleTrigger.length; i++) {
    toggleTrigger[i].addEventListener('click', function() {
      console.log('ei');
      document.querySelector('body').classList.toggle('has-mobile-nav');
    });
  }
}
document.addEventListener('DOMContentLoaded', function() {
  toggleNav();
});
