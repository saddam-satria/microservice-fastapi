import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import ReduxProvider from './redux';
import './tailwind.css'


const container = document.getElementById('root');
const root = createRoot(container);

root.render(
  <ReduxProvider>
    <App />
  </ReduxProvider>
);
