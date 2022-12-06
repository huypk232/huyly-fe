import React, {Component} from 'react';
import './productstyle.css';

export default function Product() {
	return (
		<div id='productContainer'>
			<div id='productImageContainer'>
				<img id='productImage' src={this.props.product.img_url} alt='Product'/>
			</div>
			<div id='productTitle'>
				<p>{this.props.product.title}</p>
			</div>
			<div id='productPrice'>
				<p>${this.props.product.price}</p>
			</div>
			<div>
				<button
					id='addToCartButton'
					onClick={() => this.props.addToCartHandler(this.props.product)}
				>
					Add To Cart
				</button>
			</div>
		</div>
	);
}