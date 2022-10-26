import { Layout, Menu , Col , Row , Table, Button, Input} from 'antd';
import {
    DeleteOutlined,  SearchOutlined
} from '@ant-design/icons';
import Column from 'antd/lib/table/Column';
import ColumnGroup from 'antd/lib/table/ColumnGroup';
import {useEffect, useState} from "react";
import axios from "axios";

const Cart = () => {
    const buttonDelete =() => {
        return(
            <Button icon={<DeleteOutlined/>}></Button>
        )
    }
    const buttonUpdateQuantity = () => {
        return (
            <Button icon={<DeleteOutlined/>}></Button>
        )
    }
    const data =[
        {
            key: '1',
            action : <Button icon={<DeleteOutlined/>}></Button>,
            productImage: 'John',
            name: 'Strawberry',
            price: '$' +'85',
            quantity: <Input icon={<DeleteOutlined/>}></Input>,
            total:'1',
        },
        {
            key: '2',
            action : <Button icon={<DeleteOutlined/>}></Button>,
            productImage: 'John',
            name: 'Strawberry',
            price: '$' +'85',
            quantity: <Input icon={<DeleteOutlined/>}></Input>,
            total:'1',
        },
        {
            key: '3',
            action : <Button icon={<DeleteOutlined/>}></Button>,
            productImage: 'John',
            name: 'Strawberry',
            price: '$' +'85',
            quantity: <Input icon={<DeleteOutlined/>}></Input>,
            total:'4',
        },
        {
            key: '4',
            action : <Button icon={<DeleteOutlined/>}></Button>,
            productImage: 'John',
            name: 'Strawberry',
            price: '$' +'85',
            quantity: <Input icon={<DeleteOutlined/>}></Input>,
            total:'4',
        }
    ]
    const columns = [
        {
          title: 'Action',
          dataIndex: 'action',
          key: 'name',
        },
        {
          title: 'Image',
          dataIndex: 'productImage',
          key: 'age',
        },
        {
          title: 'Name',
          dataIndex: 'name',
          key: 'address',
        },
        {
            title: 'Price',
            dataIndex: 'price',
            key: 'address',
        },
        {
            title: 'Quantity',
            dataIndex: 'quantity',
            key: 'address',
        },
        {
            title: 'Total',
            dataIndex: 'total',
            key: 'address',
        },
      ];
    const [cart, setCart] = useState([])
    useEffect(() => {
        async function getCart() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/carts');
                console.log(response);
            } catch (error) {
                console.error(error);
            }
        }
        // const fetchData = async () => {
        //     const result = await fetch("https://127.0.0.1:5000/carts", {
        //         "method": "GET",
        //         "headers": {
        //             "content-type": "application/json",
        //         },
        //     }).then(function(response) {
        //         console.log(result)
        //         console.log(response)
        //         return response.json();
        //     });
        //     const jsonResult = result()
        //     setCart(jsonResult)
        // }
        getCart();
    }, [])
    // console.log(cart)
    return(
        <>
            <Row justify='space-between'>
                <Col span={10} offset={2}>
                    <Table size='middle' dataSource={data} columns={columns} />
                </Col>
                <Col span={8} pull={2}>
                    <Table size='middle' dataSource={data} columns={columns} />
                </Col>
            </Row>
        </>
    )
}

export default Cart;