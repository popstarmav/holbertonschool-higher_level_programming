fetch('https://swapi.dev/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    $('DIV#character').text(data.name);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
