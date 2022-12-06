import React, {Component, useState} from 'react';
import './bodystyle.css'
import Product from '../product/productview';
import ProductSkeleton from '../skeleton/product/productskeletonview';
import ApiEndpoints from '../../api/apiendpoints';


async function GetPopularProducts() {
    let res = await fetch(ApiEndpoints.PRODUCT_URL, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(data => data.json())
	  return res
   }

export default function Body() {
	const getBodyStyle = () => {
		return true ? {marginLeft: '230px'} : {};
	}

	const getBodyStyleClass = () => {
		return true ?
			'bodyContainer bodyContainerWithCart' : 'bodyContainer';
	}
	const [products, setProducts] = useState()
	var productsRes = GetPopularProducts()
	productsRes.then(function(result) {
		console.log(result) // "Some User token"
		setProducts(result)
	 })
	 console.log(products)
	return (
		<div className={getBodyStyleClass()} style={getBodyStyle()}>
			<div id='body'>
				{products ?
					products.products.map((product) => (

						<Product
							key={product.id}
							product={product}
							// addToCartHandler={this.props.addToCartHandler}
						/>
					))
					:
					<ProductSkeleton />
				}
			</div>
		</div>
	);
}