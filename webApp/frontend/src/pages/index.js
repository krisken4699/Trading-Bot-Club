import React, { useState, useEffect, useRef } from "react"
import Logo from "../images/Logo2.png"
import Logo2 from "../images/Logo4.png"
import $ from 'jquery'
import { useTopContext } from "../components/ContextProvider"


const IndexPage = () => {
  const background = useRef(null)
  const top = useTopContext()
  useEffect(() => {
    $(window).scroll(() => {
      var scroll = $(window).scrollTop();
      if (scroll > window.innerHeight * 0.3) {
      }
      else {
      }
    })
  });

  return (
    <div className="transition-all blur-none duration-500" style={{ backgroundColor: top ? 'black' : "transparent", margin: `0`, maxWidth: "100vw", padding: `0` }}>
      <section className="h-screen flex align-middle justify-center transition-all duration-300" >
        <div className={`flex align-middle justify-center z-0 absolute top-0 left-0 blur-[0px] w-screen min-h-screen bg-no-repeat bg-center transition-all bg-[length:65vw]`} style={{ backgroundImage: `url(${top ? Logo2 : Logo})`, }}>
          <img ref={background} src={Logo2} className={`z-10 object-contain blur-md w-[65vw]`} style={{ filter: `brightness(${top ? '200%' : '100%'}) ` }} alt="" />
        </div >
        <img ref={background} src={top ? Logo2 : Logo} className={`${top ? 'brightness-150 ' : "brightness-100"} z-10 object-contain ${top ? 'blur-md' : "blur-[8px]"} w-[65vw]`} alt="" />

      </section>
      <section className="h-[40vh] w-screen"></section>
      <section className="bg-transparent flex text-white py-20 xl:px-60 lg:px-40 px-10 md:px-20">
        {/* <div style={{ perspective: "500px", perspectiveOrigin: "50% 50%" }} className="w-[100vw] left-0 top-[140vh] absolute h-[100vw]">
          <div style={{ transform: "rotateX(64deg) rotateZ(327deg) rotateY(28deg) translateY(-100%) translateX(1000px)" }} className="h-[100vw] w-1/3 bg-quaternary"></div>
        </div> */}

        {/* <div className="z-20 flex justify-center align-middle">
          <h1 className="text-8xl text-A1 font-bold text-center mb-10">Trading Bot Club</h1>
          <p className="text-2xl font-Metric-Medium text-secondary mb-4">The Trading Bot Club is made in 2022-2023. We aim to make a functioning trading bot in a year with modest effeciency and ROI.</p>
          <p className="text-2xl font-Metric-Medium text-secondary mb-2">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vero placeat obcaecati perferendis dignissimos ratione eaque, impedit temporibus ea quasi alias repudiandae autem expedita facilis assumenda repellat, corporis facere animi possimus.</p>
        </div> */}
        <div className="z-20 justify-center flex items-center align-middle">
          <div >
          <h1 className="text-6xl sm:text-8xl text-A1 font-bold text-center mb-10">Trading Bot Club</h1>
          <p className="sm:text-3xl text-lg sm:font-Metric-Regular font-Metric-Medium text-secondary mb-4">The Trading Bot Club is made in 2022-2023. We aim to make a functioning trading bot in a year with modest effeciency and ROI.</p>
          <p className="sm:text-3xl text-lg sm:font-Metric-Regular font-Metric-Medium text-secondary mb-2">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vero placeat obcaecati perferendis dignissimos ratione eaque, impedit temporibus ea quasi alias repudiandae autem expedita facilis assumenda repellat, corporis facere animi possimus.</p>
          </div>
        </div>
      </section>
    </div>
  )
}

export default IndexPage

export const Head = () => <title>Home Page</title>
