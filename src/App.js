import React, {useState, useEffect } from 'react';
import { Router, Routes, Route, Navigate, Link } from 'react-router-dom';

import './App.css';
import Dashboard from './container/Dashboard';

import 'antd/dist/antd.css'
import Shop from "./container/Dashboard/Header/shop";
import Login from "./container/Login/Login";

const Cart = React.lazy(() => import('./container/Dashboard/Cart'));

function App() {
  return (
    <>
        <div>
            <Dashboard />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/carts" element={
                    <React.Suspense fallback={<>Loading...</>}>
                        <Cart />
                    </React.Suspense>}
                />
                <Route path="/shop" element={<Shop />} />
                <Route path="/orders" element={<Shop />} />
                <Route path="/users" element={<Shop />} />
                <Route path="/login" element={<Login />} />
            </Routes>

        </div>
    </>
  )
}

export default App;

 function Home(props) {

     return <h2>Home</h2>;
}

function About() {
    return <h2>About</h2>;
}

function Users() {
    return <h2>Users</h2>;
}