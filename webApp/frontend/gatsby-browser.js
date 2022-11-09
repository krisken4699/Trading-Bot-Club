import React from "react";
import Layout from "./src/components/layout";
// const React = require('react')
// const Layout = require('./src/components/layout')
import { useTopContext } from "./src/components/ContextProvider";

import "./src/styles/app.css"


// Logs when the client route changes
export const onRouteUpdate = ({ location, prevLocation }) => {
    console.log("new pathname", location.pathname);
    console.log("old pathname", prevLocation ? prevLocation.pathname : null);
}

// Wraps every page in a component
export const wrapPageElement = ({ element, props }) => {
    return <Layout {...props}>{element}</Layout>
}