const backToTop = document.getElementById('backtotop');

function checkScroll() {
  // 웹 페이지가 수직으로 얼마나 스크롤되어 있는지.
  let pageYoffset = window.pageYOffset;
  if (pageYoffset !== 0) {
    backToTop.classList.add('show');
  } else {
    backToTop.classList.remove('show');
  }
}

function moveBackToTop() {
  if (window.pageYOffset > 0) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}
window.addEventListener('scroll', checkScroll);
backToTop.addEventListener('click', moveBackToTop);

// ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

const slidePrevList = document.getElementsByClassName('arrow-prev');

for (let i = 0; i < slidePrevList.length; i++) {
  // ul태그 선택
  let classList = slidePrevList[i].parentElement.parentElement.nextElementSibling;
  let liList = classList.getElementsByTagName('li');
  // 카드가 ul 태그 너비보다 넘치면, 왼쪽(Prev)버튼을 활성화, 오른쪽(Next)는 현재 맨 첫카드 위치이므로 비활성화
}
