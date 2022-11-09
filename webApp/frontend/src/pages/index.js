import React, { useState, useEffect, useRef } from "react"
import Logo from "../images/Logo2.png"
import Logo2 from "../images/Logo4.png"
import $ from 'jquery'
import { useTopContext } from "../components/ContextProvider"
import { gsap, Power1 } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const IndexPage = () => {

  const app = useRef(null)
  gsap.registerPlugin(ScrollTrigger)

  useEffect(() => {
    let ctx = gsap.context(() => {


    }, app); // <- IMPORTANT! Scopes selector text

    return () => ctx.revert(); // cleanup

  }, []);


  return (
    <div ref={app} className={`overflow-x-hidden blur-none transition-colors duration-500 `}>
      
    </div>
  )
}

export default IndexPage

export const Head = () => <title>TBC | Home</title>
