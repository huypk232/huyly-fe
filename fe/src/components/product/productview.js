import React, {Component} from 'react';
import './productstyle.css';

export default function Product({ product }) {
	console.log(this)
	return (
		<div id='productContainer'>
			<div id='productImageContainer'>
				<img id='productImage' src={product.img_url} alt='Product'/>
			</div>
			<div id='productTitle'>
				<p>{product.title}</p>
			</div>
			<div id='productPrice'>
				<p>${product.price}</p>
			</div>
			<div>
				<button
					id='addToCartButton'
					onClick={() => {

					}}
				>
					Add To Cart
				</button>
			</div>
		</div>
	);
}