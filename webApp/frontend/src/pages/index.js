import React, { useState, useEffect, useRef } from "react"
import Logo from "../images/Logo2.png"
import Logo2 from "../images/Logo4.png"
import $ from 'jquery'
import { useTopContext } from "../components/ContextProvider"
import { gsap, Power0 } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const IndexPage = () => {

  const background = useRef(null)
  const app = useRef(null)
  const top = useTopContext()
  gsap.registerPlugin(ScrollTrigger)
  useEffect(() => {
    $(window).scroll(() => {
      var scroll = $(window).scrollTop();
      if (scroll > window.innerHeight * 0.3) {
      }
      else {
      }
    })
  }, []);
  useEffect(() => {
    // create our context. This function is invoked immediately and all GSAP animations and ScrollTriggers created during the execution of this function get recorded so we can revert() them later (cleanup)
    let ctx = gsap.context(() => {
      gsap.fromTo('#h1', {
        y: '20px',
        opacity: 0
      }, {
        scrollTrigger: {
          trigger: "#h1",
          // start: "top bottom",
          toggleActions: "restart reset restart reset"
        },
        y: "0",
        // delay: ,
        opacity: 1,
        duration: 0.7
      })

      gsap.fromTo('#p1', {
        x: '-20px',
        opacity: 0
      }, {
        scrollTrigger: {
          trigger: "#p1",
          // markers: true,
          start: "top bottom",
          end: "bottom top",
          toggleActions: "restart reset restart pause"
        },
        x: "0",
        delay: 0.2,
        opacity: 1,
        duration: 0.5
      })
      gsap.fromTo('#p2', {
        x: '-20px',
        opacity: 0
      }, {
        scrollTrigger: {
          trigger: "#p2",
          // markers: true,
          start: "top bottom",
          end: "bottom top",
          toggleActions: "restart reset restart pause"
        },
        x: "0",
        delay: 0.2,
        opacity: 1,
        duration: 0.5
      })
      gsap.fromTo('.grit',{
        backgroundColor:"#0b0b0d"
      }, {
        scrollTrigger: {
          trigger: "#grid",
          // markers: true,
          // start: " top",
          // delay: 1,
          // end: "bottom top",
          toggleActions: "restart pause restart pause"
        },
        stagger: {
          axis: 'x',
          amount: 1,
          from: "center",
          grid: [20, 20]
        },
        backgroundColor:"#ebeae8",
        scale: 0.5,
        duration: 1,
      })
      gsap.to('.logo', {
        scrollTrigger: {
          trigger: ".logo",
          start: "15% top",
          end: "100%",
          // markers: true,
          scrub: true,
          // toggleActions:"restart pause reverse pause"
        },
        y: "25vh",
        x: "2vw",
        ease: Power0.easeNone
        // webkitFilter: "brightness(0.5)", 
        // filter: "brightness(0.5)"
      })

    }, app); // <- IMPORTANT! Scopes selector text

    return () => ctx.revert(); // cleanup

  }, []);

  const grids = []

  return (
    <div ref={app} className={`overflow-x-hidden blur-none transition-colors duration-500 ${top? 'bg-primary' : ""}`} style={{margin: `0`, maxWidth: "100vw", padding: `0` }}>
      <section className="h-screen logo flex align-middle justify-center " >
        <div className="flex align-middle justify-center ">
          <div className={`flex align-middle justify-center z-0 absolute top-0 left-0 blur-[0px] w-screen min-h-screen bg-no-repeat bg-center transition-all bg-[length:65vw]`} style={{ backgroundImage: `url(${top ? Logo2 : Logo})`, }}>
            <img ref={background} src={Logo2} className={`z-10 object-contain blur-md w-[65vw]`} style={{ filter: `brightness(${top ? '200%' : '100%'}) ` }} alt="" />
          </div >
          <img ref={background} src={top ? Logo2 : Logo} className={`${top ? 'brightness-150 ' : "brightness-100"} z-10 object-contain ${top ? 'blur-md' : "blur-[8px]"} w-[65vw]`} alt="" />
        </div>
      </section>
      <section className="h-[40vh] w-screen">
      </section>
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
            <h1 id="h1" className="text-6xl sm:text-8xl text-A1 font-bold text-center mb-10">Trading Bot Club</h1>
            <p id="p1" className=" sm:text-3xl text-lg sm:font-Metric-Regular font-Metric-Medium text-secondary mb-4">The Trading Bot Club is made in 2022-2023. We aim to make a functioning trading bot in a year with modest effeciency and ROI.</p>
            <p id='p2' className="sm:text-3xl text-lg sm:font-Metric-Regular font-Metric-Medium text-secondary mb-2">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vero placeat obcaecati perferendis dignissimos ratione eaque, impedit temporibus ea quasi alias repudiandae autem expedita facilis assumenda repellat, corporis facere animi possimus.</p>
          </div>
        </div>
      </section>
      <section className="h-[20vh] w-screen">
      </section>
      <section className=" w-screen bg-gradient-to-b from-primary to-quaternary">
        <div id="grid" className="flex flex-wrap w-screen">
          {[...Array(400)].map((e, i) => (<div key={i} className="w-[5vw] h-[5vw] block grit bg-primary"></div>))}
        </div>

        {/* </div> */}
      </section >
    </div >
  )
}

export default IndexPage

export const Head = () => <title>TBC | Home</title>
