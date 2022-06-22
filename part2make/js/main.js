const backToTop = document.getElementById('backtotop');

function checkScroll() {
  // 웹 페이지가 수직으로 얼마나 스크롤되어 있는지.
  /*
      웹페이지가 수직으로 얼마나 스크롤되었는지를 확인하는 값(픽셀 단위로 반환)
      https://developer.mozilla.org/ko/docs/Web/API/Window/pageYOffset
    */
  let pageYoffset = window.pageYOffset;
  if (pageYoffset !== 0) {
    backToTop.classList.add('show');
  } else {
    backToTop.classList.remove('show');
  }
}

function moveBackToTop() {
  if (window.pageYOffset > 0) {
    /*
        smooth 하게 스크롤하기
        https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTo
        */
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}
window.addEventListener('scroll', checkScroll);
backToTop.addEventListener('click', moveBackToTop);

// ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
function transformNext(event) {
  const slideNext = event.target;
  const slidePrev = slideNext.previousElementSibling;

  const classList = slideNext.parentElement.parentElement.nextElementSibling;
  let activeLi = classList.getAttribute('data-position');
  const liList = classList.getElementsByTagName('li');

  // 하나의 카드라도 왼쪽으로 이동했다면, 오른쪽으로 갈 수 있음
  if (Number(activeLi) < 0) {
    activeLi = Number(activeLi) + 260;

    // 왼쪽에 있던 카드가 오른쪽으로 갔다면, 다시 왼쪽으로 갈 수 있으므로 PREV 버튼 활성화
    slidePrev.style.color = '#2f3059';
    slidePrev.classList.add('slide-prev-hover');
    slidePrev.addEventListener('click', transformPrev);

    // 맨 왼쪽에 현재 보이는 카드가, 맨 첫번째 카드라면, 오른쪽 즉, NEXT 로 갈 수 없으므로 NEXT 버튼 비활성화
    if (Number(activeLi) === 0) {
      slideNext.style.color = '#cfd8dc';
      slideNext.classList.remove('slide-next-hover');
      slideNext.removeEventListener('click', transformNext);
    }
  }

  classList.style.transition = 'transform 1s';
  classList.style.transform = 'translateX(' + String(activeLi) + 'px)';
  classList.setAttribute('data-position', activeLi);
}

function transformPrev(event) {
  const slidePrev = event.target;
  const slideNext = slidePrev.nextElementSibling;
  // ul 태그 선택
  const classList = slidePrev.parentElement.parentElement.nextElementSibling;
  let activeLi = classList.getAttribute('data-position');
  const liList = classList.getElementsByTagName('li');
  // classList.clientWidth는 ul 태그의 실질적인 너비
  // liList.length * 260 에서 260은 각 li 요소의 실질 너비 (margin 포함)
  // activeLi 는 data-position 에 있는 현재 위치
  // 즉, liList.length * 260 + Number(activeLi)는 현재 위치부터 오른쪽으로 나열되야 하는 나머지 카드들의 너비

  // classList.clientWidth < (liList.length * 260 + Number(activeLi)) 의미는
  // 오른쪽으로 나열된 카드들이 넘친 상태이므로, 왼쪽으로 이동이 가능함
  if (classList.clientWidth < liList.length * 260 + Number(activeLi)) {
    // 위치를 왼쪽으로 260 이동 (-260px)
    activeLi = Number(activeLi) - 260;
    // 위치를 왼쪽으로 260 이동 (-260px)
    // 해당 위치는 변경된 activeLi 값이 적용된 liList.length * 260 + Number(activeLi) 값임
    // 이 값보다, classList.clientWidth (ul 태그의 너비) 가 크다는 것은
    // 넘치는 li가 없다는 뜻으로 Next버튼을 활성화되면 안됨
    if (classList.clientWidth > liList.length * 260 + Number(activeLi)) {
      slidePrev.style.color = '#cfd8dc';
      slidePrev.classList.remove('slide-prev-hover');
      slidePrev.removeEventListener('click', transformPrev);
    }
    slideNext.style.color = '#2f3059';
    slideNext.classList.add('slide-next-hover');
    slideNext.addEventListener('click', transformNext);
  }
  classList.style.transition = 'transform 1s';
  classList.style.transform = 'translateX(' + String(activeLi) + 'px)';
  classList.setAttribute('data-position', activeLi);
}

const slidePrevList = document.getElementsByClassName('slide-prev');

for (let i = 0; i < slidePrevList.length; i++) {
  // ul태그 선택
  let classList = slidePrevList[i].parentElement.parentElement.nextElementSibling;
  let liList = classList.getElementsByTagName('li');
  // 카드가 ul 태그 너비보다 넘치면, 왼쪽(Prev)버튼을 활성화, 오른쪽(Next)는 현재 맨 첫카드 위치이므로 비활성화
  if (classList.clientWidth < liList.length * 260) {
    slidePrevList[i].classList.add('slide-prev-hover');
    slidePrevList[i].addEventListener('click', transformPrev);
  } else {
    // 태그 삭제시, 부모 요소에서 removeChild 를 통해 삭제해야함.
    // 따라서 , 1. 먼저 부모 요소를 찾아서,
    // 2. 부모 요소의 자식 요소에 있는 PREV와 NEXT 요소를 삭제함
    const slideContainer = slidePrevList[i].parentNode;
    slideContainer.removeChild(slidePrevList[i].nextElementSibling); // 오른쪽 버튼
    slideContainer.removeChild(slidePrevList[i]);
  }
}
