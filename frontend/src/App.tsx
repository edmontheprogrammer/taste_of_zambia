import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

import "bootstrap/dist/css/bootstrap.min.css";

import { Button, Alert } from "react-bootstrap";

function App() {
  return (
    <div className="App">
      <Alert variant="primary">This is a button</Alert>
      <Alert variant="secondary">This is a button</Alert>
      <Button>Test Button</Button>
    </div>
  );
}

export default App;
