import React from 'react';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import AppPath from './lib/path';
import HomeScreen from './screens/home/homescreen';
import Login from './screens/login/login';
import './style.css';
import useToken from './useToken';

export default function Routes() {
	const { token, setToken } = useToken();
	console.log(token)

	if(typeof token === 'undefined') {
		return <Login setToken={ setToken } />
	}
	return (
		<Router>
			<Switch>
				<Route path={AppPath.LOGIN} exact component={Login} />
				<Route path={AppPath.HOME} exact component={HomeScreen} />
				<Route path={AppPath.CATEGORY} exact component={HomeScreen} />
			</Switch>
		</Router>
	);
	
}
