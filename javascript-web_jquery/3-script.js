document.querySelector('div#red_header').addEventListener('click', function () {
    var headerElement = document.querySelector('header');

    if (headerElement) {
        // Add the 'red' class to the header element
        headerElement.classList.add('red');
    }
});

