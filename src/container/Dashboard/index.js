import React, { useState } from 'react';
import {Router, Route, Link, RouteHandler} from 'react-router';
import homepage from './assets/img/hero-bg.jpg'
import './index.css';
import { Layout, Menu } from 'antd';
import HeaderDashBoard from './Header/Header';
import Index from './Cart';
const { Header, Footer, Sider, Content } = Layout;

const Dashboard = (props) => {
    const [user, setUser] = useState()

  return (
    <>
      <Layout>
        <Header >
          <HeaderDashBoard />
        </Header>
      </Layout>
    </>
  );
}



export default Dashboard;
