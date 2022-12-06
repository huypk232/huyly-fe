import React, { useState } from 'react';
import './homescreenstyle.css';
import Header from '../../components/header/headerview';
import SideBar from '../../components/sidebar/sidebarview';
import Body from '../../components/body/bodyview';
import ShoppingCart from '../../components/shoppingcart/shoppingcartview';
// import ApiConnector from '../../api/apiconnector';
// import ApiEndpoints from '../../api/apiendpoints';
// import QueryParam from '../../api/apiqueryparams';
// import ServerURL from '../../lib/serverurl';

export default function HomeScreen()  {
	// const [ state, setState ] = useState()
	// const [ toggleSidebar, setToggleSidebar ] = useState()
	// const [ toggleShoppingCart, setTtoggleShoppingCart ] = useState()
	// const [ totalCartItem, setTotalCartItem ] = useState()
	// const [ productSearchHandler, setProductSearchHandler ] = useState()
	const [ isShowSidebar, setIsShowSidebar ] = useState(false);
	
	// const [ products, setProducts ] = useState()
	// const [ addToCartHandler, setAddToCartHandler ]= useState()
	// const [ isShowShoppingCart, setIsShowShoppingCart ] = useState()
	// const [ cart, setCart ] = useState()
	// const [ productQuantityToCart, setProductQuantityToCart ] = useState()
	// const [ productRemoveHandler, setProductRemoveHandler ] = useState()
	return (
		<React.Fragment>
			<Header
				// toggleSidebar={setToggleSidebar}
				// toggleShoppingCart={setTtoggleShoppingCart}
				// totalCartItem={setTotalCartItem(10)}
				// productSearchHandler={setProductSearchHandler}
			/>
			<div id='bodyContainer'>
				<SideBar
					setIsShowSidebar={setIsShowSidebar}
					// productSearchHandler={setProductSearchHandler}
				/>
				<Body
					// products={setProducts}
					// addToCartHandler={setAddToCartHandler}
					// isShowSidebar={setIsShowSidebar}
					// isShowShoppingCart={setIsShowShoppingCart}
				/>
				<ShoppingCart
					// isShowShoppingCart={setIsShowShoppingCart}
					// cart={setCart}
					// products={setProducts}
					// setProductQuantityToCart={setProductQuantityToCart}
					// productRemoveHandler={setProductRemoveHandler}
				/>
			</div>
		</React.Fragment>
	);
	
}