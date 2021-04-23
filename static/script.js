let buy = document.querySelector('.al');
let sell = document.querySelector('.sat');


let stock_buy = document.querySelector('.buy');
let stock_sell = document.querySelector('.sell');

function scrollWin() {
    window.scrollTo(0, 500);
  }


buy.addEventListener('click',function(){
    stock_buy.style.display = "block";
    stock_sell.style.display = "none";
    scrollWin();
});

sell.addEventListener('click',function(){
    stock_buy.style.display = "none";
    stock_sell.style.display = "block";
    scrollWin();
});