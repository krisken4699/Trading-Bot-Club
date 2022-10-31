import React, { useEffect, useState, useContext } from "react"
import $ from 'jQuery'
import Navbar from "./Nav";
import ContextProvider, { useTopContext } from "./ContextProvider";
import { useLayoutEffect } from "react";


export default function Layout({ children }) {

  // const [top, setTop] = useState("");
  return (
    <ContextProvider>
      <main className={`bg-transparent duration-500 transition-all`} >

        <Navbar />
        {children}

      </main>
    </ContextProvider>
  )
}