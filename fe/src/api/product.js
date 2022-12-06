
async function GetPopularProducts() {
    return fetch(domain.concat('products'), {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(data => data.json())
   }

   