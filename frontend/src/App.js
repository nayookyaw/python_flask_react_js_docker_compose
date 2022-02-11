import React, {Component} from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Title from './views/Header/Title';
import Login from './views/Login/Login';
import Home from './views/Home/Home';
import SensorDetail from './views/Sensor/SensorDetail';

import './App.css';

class App extends Component {
  render () {
    return (
      <div className="">
        <Title/>

        <BrowserRouter>
          <div className="wrapper">
            <Routes>
              <Route path="/login" element={ <Login />} />
              <Route path="/" element={ <Home />} />
              <Route path="/sensor/detail" element={ <SensorDetail />} />
            </Routes>
          </div>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;