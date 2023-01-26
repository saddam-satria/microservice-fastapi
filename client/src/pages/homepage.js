import React from 'react';
import UseFetch from "../hooks/useFetch"

function Homepage() {

  let products = UseFetch("product")
  products = products.data

  return (
    <div className="container mx-auto px-2">
      <div className="grid grid-cols-1 sm:grid-cols-2">
        {
          products && products.data.map((product, index) => {
            return (<div key={index}>
              <span>name: {product.name}</span>
            </div>)
          })
        }
      </div>
    </div>
  );
}

export default Homepage;
