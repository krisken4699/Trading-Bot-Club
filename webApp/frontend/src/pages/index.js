import React, { useState, useEffect, useRef } from "react"
import Logo from "../images/Logo2.png"
import Logo2 from "../images/Logo4.png"
import $ from 'jquery'
import { useTopContext } from "../components/ContextProvider"
import { gsap, Power1, random } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const IndexPage = () => {

  const background = useRef(null)
  const app = useRef(null)
  const gridElem = useRef(null)
  const [gridHeight, setGridHeight] = useState(0)
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
    setGridHeight(gridElem.current.clientHeight)
  }, [gridElem]);
  useEffect(() => {
    // create our context. This function is invoked immediately and all GSAP animations and ScrollTriggers created during the execution of this function get recorded so we can revert() them later (cleanup)
    let ctx = gsap.context(() => {
      gsap.timeline({
        scrollTrigger: {
          trigger: "#h1",
          start: "top bottom",
          end: 'bottom+=100 top',
          // markers:true,
          toggleActions: "restart reset restart reset"
        },
      }).fromTo('#h1', {
        y: '20px',
        opacity: 0
      }, {
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

      gsap.timeline({
        scrollTrigger: {
          trigger: "#h1",
          // markers: true,
          start: "top top",
          endTrigger: "#grid",
          end: "bottom bottom",
          // markers: true,
          start: "top top",
          // delay: 1,
          scrub: true,
          // end: "bottom-=20% bottom",
          // toggleActions: "restart reset restart reset"
        },
      })
        .fromTo('.grit', {
          scale: 2
        }, {
          stagger: {
            axis: 'y',
            amount: 1,
            // ease: Power1.easeInOut(),
            from: "start",
            grid: [window.innerWidth > window.innerHeight ? 20 : 30, 20]
          },
          scale: 0.5,
          // delay: 0.2,
          duration: 1,
        })

      gsap.timeline({
        scrollTrigger: {
          trigger: "#grid",
          // markers: true,
          // start: "bottom-=100vh top",
          start: "bottom bottom",
          // delay: 1,
          // scrub: 2,
          end: "bottom+=20% bottom",
          toggleActions: "play resume none reverse"
        },
      }).to('.grit2', {
        stagger: {
          axis: 'y',
          amount: 0.1,
          // ease: Power1.easeInOut(),
          from: "end",
          grid: [window.innerWidth > window.innerHeight ? 20 : 30, 20]
        },
        scale: 1,
        width: '1px',
        height: '*=2',
        // border: '1px',
        y: '100vh',
        // marginRight: window.innerWidth > window.innerHeight ? "25w-=0.5px" : "10h-=0.5px",
        // marginLeft: window.innerWidth > window.innerHeight ? "25w-=0.5px" : "10h-=0.5px",
        // // delay: 0.2,
        duration: 0.7,
      })

      gsap.timeline({
        scrollTrigger: {
          trigger: "#h1",
          // markers: true,
          start: "top top",
          endTrigger: "#grid",
          end: "bottom bottom",
          // delay: 1,
          scrub: true,
          // end: "bottom-=20% bottom",
          // toggleActions: "restart reset restart reset"
        },
      }).fromTo('.grit2', {
        backgroundColor: "#0b0b0d"
      }, {
        ease: "Power1.easeIn",
        backgroundColor: "#dda74f",
        // duration: 10
      })


      gsap.to('#graph', {
        scrollTrigger: {
          trigger: "#graph",
          start: "top top",
          end: "bottom+=100% bottom",
          markers: true,
          scrub: true,
          // toggleActions:"restart pause reverse pause"
        },
        display: "block",
        ease: "Power1.easeIn",
        y: "+=100vh",
        // x: "2vw",
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
        y: "60vh",
        scale: 0.8,
        // x: "2vw",
        ease: Power1.easeOut
        // webkitFilter: "brightness(0.5)", 
        // filter: "brightness(0.5)"
      })

    }, app); // <- IMPORTANT! Scopes selector text

    return () => ctx.revert(); // cleanup

  }, []);



  const grids = []

  return (
    <div ref={app} className={`overflow-x-hidden blur-none transition-colors duration-500 ${top ? 'bg-primary' : ""}`} style={{ margin: `0`, maxWidth: "100vw", padding: `0` }}>
      {/* <section className={` `}> */}
      <section className={`h-screen logo flex align-middle justify-center`} >
        <div className="flex align-middle justify-center ">
          <div className={`flex align-middle justify-center z-0 absolute top-0 left-0 blur-[0px] w-screen min-h-screen bg-no-repeat bg-center transition-all bg-[length:65vw]`} style={{ backgroundImage: `url(${top ? Logo2 : Logo})`, }}>
            <img ref={background} src={Logo2} className={`z-10 object-contain blur-md w-[65vw]`} style={{ filter: `brightness(${top ? '200%' : '100%'}) ` }} alt="" />
          </div >
          <img ref={background} src={top ? Logo2 : Logo} className={`${top ? 'brightness-150 ' : "brightness-100"} z-10 object-contain ${top ? 'blur-md' : "blur-[8px]"} w-[65vw]`} alt="" />
        </div>
      </section>
      {/* </section> */}
      <section className="h-[40vh] w-screen">
      </section>
      <section className="bg-transparent flex text-white py-20 xl:px-60 lg:px-40 px-10 md:px-20">
        <div className="z-20 justify-center flex items-center align-middle">
          <div className=" z-20">
            <h1 id="h1" className="text-6xl sm:text-8xl relative text-A1 sm:font-thin font-bold text-center mb-10">Trading Bot Club</h1>
            <p id="p1" className=" sm:text-3xl mix-blend-difference z-20 relative text-lg sm:font-Metric-Thin font-Metric-Medium text-secondary mb-4">The Trading Bot Club is made in 2022-2023. We aim to make a functioning trading bot in a year with modest effeciency and ROI.</p>
            <p id='p2' className="sm:text-3xl mix-blend-difference relative z-20 text-lg sm:font-Metric-Thin font-Metric-Medium text-secondary mb-2">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vero placeat obcaecati perferendis dignissimos ratione eaque, impedit temporibus ea quasi alias repudiandae autem expedita facilis assumenda repellat, corporis facere animi possimus.</p>
            <div ref={gridElem} className="absolute z-10 translate-y-[40vh] left-0 w-screen ">
              <div id="grid" className={`flex w-[100v${window.innerWidth > window.innerHeight ? "w" : "h"}] flex-wrap -translate-y-10`}>
                {window.innerWidth > window.innerHeight ? [...Array(400)].map((e, i) => (<div key={i} className={`w-[5vw] h-[5vw] candle2 block grit overflow-y-visible`}><div className="grit2 z-10 w-full h-full mx-auto"></div></div>)) : [...Array(300)].map((e, i) => (<div key={i} className={`w-[10vw] h-[10vw] block grit overflow-y-visible`}><div className="grit2 mx-auto w-full h-full"></div></div>))}
              </div>
            </div>
          </div>
        </div>
      </section>
      <section style={{ height: gridHeight }} className={`text-white w-screen`}>
      </section>
      <section id="graph" className="text-white">
        <div style={{width:`100v${window.innerWidth > window.innerHeight ? "w" : "h"}`}} className={`flex flex-wrap -translate-y-10`}>
          {window.innerWidth > window.innerHeight ? [...Array(20)].map((e, i) => (
             <div key={i} style={{ transform: `translateY(${Math.round(Math.random() * 50) + "vh"})` }} className={`w-[5vw] min-h-[5vw] candle overflow-y-visible flex items-center`}>
              <div style={{ height: Math.round(Math.random() * 50) + "vh" }} className={`z-0 ${["bg-accent2", 'bg-accent3'][Math.round(Math.random())]} rounded-lg w-1/3 mx-auto`}></div>
            </div>))
            : [...Array(10)].map((e, i) => (
              <div key={i} style={{ transform: `translateY(${Math.round(Math.random() * 50) + "vh"})` }} className={`w-[10vh] min-h-[10vh] candle overflow-visible flex items-center`}>
                <div style={{ height: Math.round(Math.random() * 50) + "vh" }} className={`z-0 ${["bg-accent2", 'bg-accent3'][Math.round(Math.random())]} rounded-lg w-1/3 mx-auto`}></div>
              </div>))}
        </div>
      </section>
      <section className={`h-10 text-white w-screen`}>
      </section>

    </div >
  )
}

export default IndexPage

export const Head = () => <title>TBC | Home</title>
