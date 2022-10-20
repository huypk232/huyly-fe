import logo from './logo.svg';
import React from 'react';
import {Router, Route, Link, RouteHandler} from 'react-router';

import './App.css';
import Dashboard from './container/Dashboard';
import 'antd/dist/antd.css'

function App() {
  return (
    <div>
      <Dashboard />
    </div>
  )
}

export default App;
