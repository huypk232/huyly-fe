const Shop = () => {
    return (
        <p>hello</p>
    )
};

export default Shop;

// import React from "react";
// import {
//     BrowserRouter as Router,
//     Routes,
//     Route,
//     Link
// } from "react-router-dom";
// import { Menu } from "antd"
//
//
// export default function App() {
//     return (
//         <Router>
//             <div>
//                 <Menu>
//                     <Menu.Item>
//                         <Link to="/">Home.css</Link>
//                     </Menu.Item>
//                     <Menu.Item>
//                         <Link to="/about">About</Link>
//                     </Menu.Item>
//                     <Menu.Item>
//                         <Link to="/users">Users</Link>
//                     </Menu.Item>
//                 </Menu>
//
//                 {/* A <Switch> looks through its children <Route>s and
//             renders the first one that matches the current URL. */}
//                 <Routes>
//                     <Route path="/about" element={<About />} />
//                     <Route path="/users" element={<Users />} />
//                     <Route path="/" element={<Home.css />} />
//                 </Routes>
//             </div>
//         </Router>
//     );
// }
//
// function Home.css() {
//     return <h2>Home.css</h2>;
// }
//
// function About() {
//     return <h2>About</h2>;
// }
//
// function Users() {
//     return <h2>Users</h2>;
// }