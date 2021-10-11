CUPCAKE_LISTS = document.getElementById('cupcake-list');
FORM = document.getElementById('cupcake-form');
const FLAVOR = document.getElementById('flavor-input');
const SIZE = document.getElementById('size-input');
const RATING = document.getElementById('rating-input');
const IMAGE = document.getElementById('image-input');

window.addEventListener('load', async () => {
  const resp = await axios.get('api/cupcakes');

  data = resp.data.cupcakes;
  for (const cupcake of data) {
    cupcakeCard = createCard(cupcake);
    CUPCAKE_LISTS.appendChild(cupcakeCard);
  }
})

FORM.addEventListener("submit", async (evt) => {
  evt.preventDefault();

  const flavor = FLAVOR.value;
  const size = SIZE.value;
  const rating = RATING.value;
  const image = IMAGE.value;

  // Post to the Server
  const resp = await axios.post('/api/cupcakes', { flavor, size, rating, image })
  const new_cupcake = resp.data.cupcake

  // Clear the Form
  clearForm()

  // Add new cupcake to list
  const cupcakeCard = createCard(new_cupcake)
  CUPCAKE_LISTS.appendChild(cupcakeCard);
})

const clearForm = () => {
  FLAVOR.value = ''
  IMAGE.value = ''
  SIZE.value = ''
  IMAGE.value = ''
}

const createCard = (data) => {
  let col = document.createElement('div');
  let cardDiv = document.createElement('div');
  let img = document.createElement('img');
  let cardBody = document.createElement('div');
  let h5 = document.createElement('h5');
  let p = document.createElement('p');

  col.className = 'col';
  cardDiv.className = 'card h-100';

  img.setAttribute('src', data.image);
  img.setAttribute('class', 'card-img-top');

  cardBody.className = 'card-body';

  h5.className = 'card-title';
  h5.innerText = data.flavor;

  p.className = 'card-text';
  p.innerText = `Rating: ${data.rating} | Size: ${data.size}`;

  cardBody.appendChild(h5);
  cardBody.appendChild(p);
  cardDiv.appendChild(img);
  cardDiv.appendChild(cardBody);
  col.appendChild(cardDiv);

  return col;
}
