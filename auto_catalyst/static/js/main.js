const nav = document.querySelector(".navbar");
let lastScrollY = window.scrollY;

window.addEventListener("scroll", () => {
    if (lastScrollY < window.scrollY) {
        // nav.classList.add("nav--hidden");
        nav.classList.add("navbar--moveup");
    } else {
        // nav.classList.remove("nav--hidden");
        nav.classList.remove("navbar--moveup");
    }

    lastScrollY = window.scrollY;
});

const alertElement = document.getElementById('alertDiv');
const timerElement = document.getElementById('timer');

function showAlert() {
  alertElement.style.display = 'block';
  timerElement.style.animationPlayState = 'running';

  // Store the current scroll position
  const scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

  // Scroll to the top of the page
  window.scrollTo(0, 0);

  setTimeout(() => {
    alertElement.style.display = 'none';
    timerElement.style.animationPlayState = 'paused';
    timerElement.style.width = '100%';

    // Scroll back to the original position
    window.scrollTo(0, scrollPosition);
  }, 3000);
}
showAlert();


const myCarouselElement = document.querySelector('#myCarousel')

const carousel = new bootstrap.Carousel(myCarouselElement, {
  interval: 3000,
  touch: false
});

// function togglePhotos() {
    
//   }
  
//   $(document).ready(togglePhotos);


function toggleGalleryPhotos() {
    console.log('Button clicked');
    var moreGalleryPhotos = document.getElementById('moreGalleryPhotos');
    if (moreGalleryPhotos.style.display === 'none') {
        moreGalleryPhotos.style.display = 'block';
        showMorePhotos.style.display = 'none';
    } else {
        moreGalleryPhotos.style.display = 'none';
        showMorePhotos.style.display = 'block';
    }
}