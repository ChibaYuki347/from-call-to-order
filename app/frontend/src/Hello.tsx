import React from "react";
import { useEffect, useState } from "react";

const Hello = () => {
  const [message, setMessage] = useState({});
  useEffect(() => {
    fetch("/api/v1/hello")
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message);
        setMessage(data.message);
      });
  }, []);
  return <div>Message is {JSON.stringify(message)}</div>;
};

export default Hello;
