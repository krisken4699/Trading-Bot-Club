import React, { useState, useEffect, useRef } from "react"
import Logo from "../images/Logo2.png"
import Logo2 from "../images/Logo4.png"
import $ from 'jquery'
import { useTopContext } from "../components/ContextProvider"


const IndexPage = () => {
  const [blur, setBlur] = useState("");
  const background = useRef(null)
  const top = useTopContext()
  useEffect(() => {
    $(window).scroll(() => {
      var scroll = $(window).scrollTop();
      if (scroll > window.innerHeight * 0.3) {
        setBlur(true)
        // background.current.style.filter = `blur(1px);`;
      }
      else {
        setBlur(false)
        // background.current.style.filter = `blur(5px);`;
      }
    })
  });

  return (
    <div className="transition-all duration-500" style={{ backgroundColor: top ? 'black' : "transparent", margin: `0`, maxWidth: "100vw", padding: `0` }}>
      <section className="h-screen flex align-middle justify-center transition-all duration-300" >
        <div className={`flex align-middle justify-center z-0 absolute top-0 left-0 blur-[0px] w-screen min-h-screen bg-no-repeat bg-center transition-all bg-[length:65vw]`} style={{ backgroundImage: `url(${blur ? Logo2 : Logo})`, }}>
          <img ref={background} src={Logo2} className={`z-10 object-contain blur-md ${blur ? '' : "hidden"} w-[65vw]`} style={{ filter: `brightness(${blur ? '200%' : '100%'}); ` }} alt="" />
        </div >
        <img ref={background} src={blur ? Logo2 : Logo} className={`${blur ? 'brightness-150 ' : "brightness-100"} z-10 object-contain ${blur ? 'blur-sm' : "blur-[8px]"} w-[65vw]`} alt="" />

      </section>
      <section className="h-[40vh] w-screen"></section>
      <section className="bg-transparent text-white py-20 px-60">
        {/* <div className="fixed -top-1/2 z-10 w-[20vw] h-[90vh] bg-tertiary left-0"></div> */}
        <div className="flex-col z-20 flex ">
          <h1 className="text-8xl text-A1 font-bold text-center mb-10">Trading Bot Club</h1>
          <p className="text-3xl font-Metric-SemiBold text-secondary">The Trading Bot Club is made in 2022-2023. We aim to make a functioning trading bot in a year with modest effeciency and ROI.</p>
        </div>
      </section>
    </div>
  )
}

export default IndexPage

export const Head = () => <title>Home Page</title>
