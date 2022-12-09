export function getList() {
    return fetch('http://localhost:3333/products')
        .then(data => data.json())
}