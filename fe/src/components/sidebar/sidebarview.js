import React from 'react';
import {Link} from 'react-router-dom';
import './sidebarstyle.css';
// import ApiConnector from '../../api/apiconnector';
// import ApiEndpoints from '../../api/apiendpoints';
import CategorySkeleton from '../skeleton/category/categoryskeletonview';
import SearchForm from '../form/searchform/searchformview';

export default function SideBar({ setIsShowSidebar }) {
	var isShowSidebar = false
	const state = {
		'categories': [
			{
				'key': 1,
				'name': 'technology'
			}
		]
	}

	var sidebarStyle =  !isShowSidebar ? {left: '-200px'} : {};
	var sidebarShow = sidebarStyle === {} ? true : false 
	setIsShowSidebar(sidebarShow)

	const getCategoryLink = (categoryId) => `/c/${categoryId}`;

	// const categorySuccessHandler = (categories) => {
	// 	setState({state: categories});
	// }

	console.log(state.categories);
	return (
		<div id='sideBarContainer' style={sidebarStyle}>
			<div id='sideBarBody'>
				{state.categories.length > 0 ?
					<ul>
						<li id='sideBarSearchContainer'>
							<SearchForm
								// productSearchHandler={this.props.productSearchHandler}
							/>
						</li>

						{state.categories.map((category) => (
							<Link key={category.id} to={getCategoryLink(category.id)}>
								<li>{category.name}</li>
							</Link>
						))}
					</ul>
					:
					<CategorySkeleton />
				}
			</div>
		</div>
	);
}