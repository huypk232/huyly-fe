import ApiEndpoints from "../api/apiendpoints";

export function getCurrentCart() {
    return fetch('http://localhost:3333/carts', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(data => data.json())
}

export function addToCurrentCart(item) {
    return fetch('http://localhost:3333/carts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({item})
    })
        .then(data => data.json())
}