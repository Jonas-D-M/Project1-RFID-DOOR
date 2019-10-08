const IP = location.hostname + ':5000';
const api = 'http://' + IP + '/api/history';

const showHistory = function(json) {
  console.log(json);
  let list = '';
  let oldMonth;
  let oldDay;
  let a = new Array();
  let aantal = 0;
  for (let history of json) {
    // make date from db timestamp
    let timeStamp = new Date(history.lock_time);
    console.log(timeStamp);
    // get month from timestamp
    let monthNr = timeStamp.getMonth();

    // converts month number to written month
    const monthName = function(pMonth) {
      monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      return monthList[pMonth];
    };

    // put written month in variable
    let month = monthName(monthNr);

    // get hour of timestamp
    let hours;
    if (timeStamp.getHours() < 10) {
      hours = '0' + timeStamp.getHours();
    } else {
      hours = timeStamp.getHours();
    }

    let minutes;
    if (timeStamp.getMinutes() < 10) {
      minutes = '0' + timeStamp.getMinutes();
    } else {
      minutes = timeStamp.getMinutes();
    }

    let time = hours + ':' + minutes;
    console.log(time);

    // write if door is closed or open
    let status = '';
    if (history.locked === 1) {
      status = 'Closed';
    } else {
      status = 'Open';
    }

    // get day of month from timestamp
    let day;
    if (timeStamp.getDate() < 10) {
      day = '0' + timeStamp.getDate();
    } else {
      day = timeStamp.getDate();
    }

    // check if day or month is different than other day or month
    if (oldMonth != month || oldDay != day) {
      //set old month and day to new day
      oldMonth = month;
      oldDay = day;

      // insert div into list
      list += `<div id="${aantal}" class="c-history"></div>`;
      console.log(list);

      a[aantal] = `<div class="c-history__date">
      <div class="c-history__date-day">${day}</div>
      <div class="c-history__date-month">${month}</div>
    </div>

    <div class="c-history__feed u-1-of-2">
      <div class="c-history__feed-info">
        <img class="c-history__feed-avatar" src="img/${history.gender}.jpg" alt="${history.gender}" />
        <div class="c-history__feed-name_and_time">
          <div class="c-history__feed-name">${history.first_name} ${history.last_name}</div>
          <div class="c-history__feed-time">${time}</div>
        </div>

        <div class="c-history__feed-status">${status}</div>
      </div>`;
      aantal++;
      // insert html into historyContainer in document
      document.querySelector('.historyContainer').innerHTML = list;
    } else {
      console.log('Dit is aantal: ' + aantal);
      a[aantal - 1] += `
      <div class="c-history__line-separator"></div>
    
                <div class="c-history__feed-info">
                  <img class="c-history__feed-avatar" src="img/${history.gender}.jpg" alt="${history.gender}" />
                  <div class="c-history__feed-name_and_time">
                    <div class="c-history__feed-name">${history.first_name} ${history.last_name}</div>
                    <div class="c-history__feed-time">${time}</div>
                  </div>
                  <div class="c-history__feed-status">
                    <div>${status}</div>
                  </div>
                </div>`;
    }
  }
  let len = Object.keys(a).length;
  for (let index = 0; index <= len; index++) {
    document.getElementById(index).innerHTML = a[index];
  }
};

document.addEventListener('DOMContentLoaded', function() {
  console.info('DOM geladen');
  handleData(api, showHistory);
});
