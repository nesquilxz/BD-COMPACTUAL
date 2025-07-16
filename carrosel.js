let index = 0;
function mover(direcao) {
  const slides = document.getElementById("slides");
  const totalSlides = slides.children.length;
  index = (index + direcao + totalSlides) % totalSlides;
  slides.style.transform = `translateX(-${index * 100}%)`;
}

setInterval(() => {
  mover(1);
}, 5000);
