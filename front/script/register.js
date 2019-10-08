const IP = location.hostname + ':5000';
const api = 'http://' + IP + '/api/user';

const showPW = function(jsonObject) {
  document.querySelector('.o-layout').innerHTML = `<p class="c-lead__reg o-layout__item ">This is your unique 4 digit password. Use it whenever you forget your keycard.</p>
       <div class='c-password'>${jsonObject.password}</div>
       `;
};

const insertUser = function() {
  let list = {
    first_name: document.getElementById('first_name').value,
    last_name: document.getElementById('last_name').value,
    card_id: document.getElementById('card_id').value
  };

  let radios = document.getElementsByName('gender');

  for (var i = 0, length = radios.length; i < length; i++) {
    if (radios[i].checked) {
      list.gender = radios[i].value;
      break;
    }
  }
  console.log(JSON.stringify(list));
  handleData(api, showPW, 'POST', JSON.stringify(list));
};

const caller = function(jsonObject) {
  console.log(jsonObject);
};

document.addEventListener('DOMContentLoaded', function() {
  console.info('DOM geladen');
  document.getElementById('register').addEventListener('click', insertUser);
});
