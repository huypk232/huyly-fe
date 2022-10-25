import logo from './logo.svg';
import React from 'react';
import { Router, Routes, Route, Navigate, Link } from 'react-router-dom';
import { BrowserRouter } from 'react-router-dom';
import {Menu} from 'antd';

import './App.css';
import Dashboard from './container/Dashboard';
import 'antd/dist/antd.css'
import Shop from "./container/Dashboard/Header/shop";

function Shopee() {
    return (
        <h1>hello</h1>
    )
};

function App() {
  return (
    <>
        <div>

                    <Routes>
                        <Route path="/" element={<Dashboard/>} />
                        <Route  path="/shop" element={<Shop />} />
                    </Routes>

        </div>
    </>
  )
}

export default App;


 function Home() {
     return <h2>Home</h2>;
}

function About() {
    return <h2>About</h2>;
}

function Users() {
    return <h2>Users</h2>;
}