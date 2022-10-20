import { Layout, Menu , Col , Row , Table, Button} from 'antd';
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
    const data =[
        {
            key: '1',
            productImage: 'John',
            name: 'Strawberry',
            price: '$' +'85',
            
            total:'1',
        },
        {
            key: '2',
            productImage: 'John',
            name: 'Strawberry',
            price: '$' +'85',
            
            total:'1',
        },
        {
            key: '3',
            productImage: 'John',
            name: 'Strawberry',
            price: '$' +'85',
            
            total:'4',
        },
        {
            key: '4',
            action : buttonDelete,
            productImage: 'John',
            name: 'Strawberry',
            price: '$' +'85',
            
            total:'4',
        }
    ]
    return(
        <>
            <Row>
                <Col span={12}>
                    <Table size='middle' dataSource={data}>
                        <Column title="Action" dataIndex={"action"} key={data.key}>data.action</Column>
                        <Column title="Product Image"></Column>
                        <Column title="Name" dataIndex={"name"} key={data.key}>data.name</Column>
                        <Column title="Price" dataIndex={"price"} key={data.key}>data.price</Column>
                        <Column title="Quantity"></Column>
                        <Column title="Total" dataIndex={"total"} key={data.key}>data.total</Column>
                   
                    </Table>
                </Col>
                <Col span={12}>Table 2</Col>
            </Row>
        </>
    )
}

export default ContentDashBoard;