import React from "react";

import "bootstrap/dist/css/bootstrap.min.css";
import { Button, Alert } from "react-bootstrap";
import shawarma_2 from "./images/shawarma_2.jpg"



const Home = () => {
  return (
    <div className="container">
    <div>
      <br />
      <h3> We make the best Shawarmas in Lusaka! </h3>

      <div className="text-center">
        <img
          src={ shawarma_2 }
          className="img-fluid"
          alt="Taste of Zambia"
        />
      </div>
    </div>
    </div>
  );
};

export default Home;
