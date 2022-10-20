import { Layout, Menu , Col , Row , Table, Button, Input} from 'antd';
import {
    DeleteOutlined,  SearchOutlined
} from '@ant-design/icons';
import Column from 'antd/lib/table/Column';
import ColumnGroup from 'antd/lib/table/ColumnGroup';

const ContentDashBoard = () => {
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

export default ContentDashBoard;