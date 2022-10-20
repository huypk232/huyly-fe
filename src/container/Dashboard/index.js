import React from 'react';
import {Router, Route, Link, RouteHandler} from 'react-router';
import homepage from './assets/img/hero-bg.jpg'
import './index.css';
import { Layout, Menu } from 'antd';
const { Header, Footer, Sider, Content } = Layout;

const Dashboard = () => {
  const items1 = ['1', '2', '3'].map((key) => ({
    key,
    label: `nav ${key}`,
  }));
  return (
    <>
      <Layout>
        <Header>
        <div className="logo" />
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']} items={items1} />
        </Header>
        <Content>Content</Content>
        <Footer>Footer</Footer>
      </Layout>
    </>
  );
}



export default Dashboard;
