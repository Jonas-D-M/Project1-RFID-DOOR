const IP = location.hostname + ':5000';
const api = 'http://' + IP + '/api/users';

const showUsers = function(json) {
  console.log(json);
  let list = '';
  let aantal = 0;
  for (let user of json) {
    list += `<div class="c-user__info u-1-of-2">
    <img class="c-user__image" src="img/${user.gender}.jpg" alt="${user.gender}">
    <label class="c-user__name">${user.first_name} </br>${user.last_name}</label>
    </div>`;
    aantal++;
  }
  console.log(list);
  document.querySelector('.c-users').innerHTML = list;
};

document.addEventListener('DOMContentLoaded', function() {
  console.info('DOM LOADED');
  handleData(api, showUsers);
});
