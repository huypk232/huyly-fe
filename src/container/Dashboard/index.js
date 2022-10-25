import React from 'react';
import {Router, Route, Link, RouteHandler} from 'react-router';
import homepage from './assets/img/hero-bg.jpg'
import './index.css';
import { Layout, Menu } from 'antd';
import HeaderDashBoard from './Header/Header';
import ContentDashBoard from './Content/Content';
const { Header, Footer, Sider, Content } = Layout;

const Dashboard = ({children}) => {

  return (
    <>
      <Layout>
        <Header >
          <HeaderDashBoard />
        </Header>
        <Content>
          <ContentDashBoard/>
        </Content>
        <Footer>Footer</Footer>
      </Layout>
      {/*{children}*/}
    </>
  );
}



export default Dashboard;
