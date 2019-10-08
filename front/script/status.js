'use strict';
const IP = location.hostname + ':5000';
const api = 'http://' + IP + '/api/status';

const showStatus = function(json) {
  console.log(json);
  let currentStatus = '';
  for (let status of json) {
    console.log(status.locked);
    if (status.locked === 1) {
      currentStatus = 'Closed';
    } else {
      currentStatus = 'Open';
    }
    console.log(currentStatus);
    document.getElementById('figure').innerHTML = `<img src="img/svg/${currentStatus}.svg" alt="${currentStatus} lock" />`;
    document.querySelector('p').innerHTML = `<p>${currentStatus}</p>`;
  }
};

document.addEventListener('DOMContentLoaded', function() {
  console.info('DOM geladen');
  handleData(api, showStatus);
});
