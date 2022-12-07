import React, { useState, useEffect, useRef } from 'react';
import {
    DesktopOutlined,
    FileOutlined,
    PieChartOutlined,
    TeamOutlined,
    UserOutlined,
    LaptopOutlined,
    NotificationOutlined,
} from '@ant-design/icons';
import { Breadcrumb, Layout, Menu, Row, Col, theme } from 'antd';
import ApiEndpoints from "./api/apiendpoints";
import Product from "./components/product/productview";
const { Header, Content, Footer, Sider } = Layout;
function getItem(label, key, icon, children) {
    return {
        key,
        icon,
        children,
        label,
    };
}
const items1 = [
    getItem('Home', '1', <PieChartOutlined />),
    getItem('Product', '2', <DesktopOutlined />),
    getItem('User', 'sub1', <UserOutlined />, [
        getItem('Customer', '3'),
        getItem('Partner', '4'),
        getItem('Vendor', '5'),
    ]),
    getItem('Warehouse', 'sub2', <TeamOutlined />, [getItem('Team 1', '6'), getItem('Team 2', '8')]),
    getItem('Me', '9', <FileOutlined />),
];

const items2 = [UserOutlined, LaptopOutlined, NotificationOutlined].map(
    (icon, index) => {
        const key = String(index + 1);

        return {
            key: `sub${key}`,
            icon: React.createElement(icon),
            label: `subnav ${key}`,

            children: new Array(4).fill(null).map((_, j) => {
                const subKey = index * 4 + j + 1;
                return {
                    key: subKey,
                    label: `option${subKey}`,
                };
            }),
        };
    },
);

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
const productsRes = GetPopularProducts()
const App = () => {
    const {
        token: { colorBgContainer },
    } = theme.useToken();
    const [products, setProducts ] = useState(null)

    useEffect(() => {
        productsRes.then(result =>
            setProducts(result)
        )
    }, []);
    console.log(products)
    if (products) {
        return <div>Loading ...</div>
    }
    return (
        <Layout>
            <Header className="header">
                <div className="logo" />
                <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']} items={items1} />
            </Header>
            <Layout>
                <Sider width={200} style={{ background: colorBgContainer }}>
                    <Menu
                        mode="inline"
                        defaultSelectedKeys={['1']}
                        defaultOpenKeys={['sub1']}
                        style={{ height: '100%', borderRight: 0 }}
                        items={items2}
                    />
                </Sider>
                <Layout style={{ padding: '0 24px 24px' }}>
                    <Breadcrumb style={{ margin: '16px 0' }}>
                        <Breadcrumb.Item>Home</Breadcrumb.Item>
                        <Breadcrumb.Item>List</Breadcrumb.Item>
                        <Breadcrumb.Item>App</Breadcrumb.Item>
                    </Breadcrumb>
                    <Content
                        style={{
                            padding: 24,
                            margin: 0,
                            minHeight: 280,
                            background: colorBgContainer,
                        }}
                    >
                        Content
                        <Row gutter={[16, 16]} wrap={true} >
                            {
                                products?.map(item => {
                                    console.log(products)
                                    return (
                                        <Col span={6} key={item.id}>
                                            <div>{item.id}</div>
                                            {/*<Product key={item.id} product={item} />*/}
                                        </Col>
                                    )
                                })
                            }
                        </Row>
                    </Content>
                </Layout>
            </Layout>
        </Layout>
    );
};
export default App;