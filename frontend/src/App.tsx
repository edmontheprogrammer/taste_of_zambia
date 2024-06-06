import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";


import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Contact from "./pages/Contact";
import NoPage from "./pages/NoPage";
import About from "./pages/About";
import Edit_Order from "./pages/Edit_Order";
import Order from "./pages/Order";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="contact" element={<Contact />} />
          <Route path="order" element={<Order />} />
          <Route path="edit-order" element={<Edit_Order />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
