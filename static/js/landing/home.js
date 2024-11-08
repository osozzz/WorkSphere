document.addEventListener('DOMContentLoaded', () => {
    const mainImage = document.getElementById('mainImage');
    const previewImages = document.querySelectorAll('.preview-image');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const previewScroll = document.querySelector('.preview-scroll');

    let currentIndex = 0;

    function updateMainImage(index) {
        const selectedPreview = previewImages[index];
        mainImage.src = selectedPreview.getAttribute('data-main');
        mainImage.alt = selectedPreview.alt.replace('Vista previa del', 'Imagen principal del');
        previewImages.forEach(img => img.classList.remove('active'));
        selectedPreview.classList.add('active');
        currentIndex = index;
    }

    previewImages.forEach((img, index) => {
        img.addEventListener('click', () => updateMainImage(index));
    });

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + previewImages.length) % previewImages.length;
        updateMainImage(currentIndex);
        previewScroll.scrollLeft -= 90;
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % previewImages.length;
        updateMainImage(currentIndex);
        previewScroll.scrollLeft += 90;
    });

    // Inicializar con la primera imagen
    updateMainImage(0);
});