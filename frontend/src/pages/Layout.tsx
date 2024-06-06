import React from "react";
import { Outlet, Link } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";

import "./css/Layout.css";

import "./css/Layout.css";

const Layout = () => {
  return (
    <>
      
        <nav
          className="navbar navbar-expand-lg navbar-dark"
          style={{ backgroundColor: "#238a44" }}
        >
          <div className="container">
            <Link className="navbar-brand" to="/">
              Taste of Zambia
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div
              className="collapse navbar-collapse"
              id="navbarSupportedContent"
            >
              <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item active">
                  <Link className="nav-link" to="/order">
                    Order Shawarma
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/about">
                    About
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/contact">
                    Contact
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      
      <Outlet />
    </>
  );
};

export default Layout;
