import React, { useState, useEffect, useRef } from "react"
import Logo from "../images/Logo2.png"
import Logo2 from "../images/Logo4.png"
import $ from 'jquery'
import { useTopContext } from "../components/ContextProvider"
import { gsap, Power1 } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const IndexPage = () => {

  const background = useRef(null)
  const app = useRef(null)
  const gridElem = useRef(null)
  const [gridHeight, setGridHeight] = useState(0)
  const top = useTopContext()
  gsap.registerPlugin(ScrollTrigger)
  
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
          scrub: 1,
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
        // filter:"drop-shadow(#dda74f 0 0 0.4rem)" ,
        // boxShadow: "0 0 0.6rem 0.2rem rgba(221, 167,  79, 0.8)",
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
          end: "bottom-=30% bottom",
          // delay: 1,
          scrub: true,
          // end: "bottom-=20% bottom",
          // toggleActions: "restart reset restart reset"
        },
      }).fromTo('.grit2', {
        backgroundColor: "#100c0c"
      }, {
        ease: "Power3.easeIn",
        backgroundColor: "#dda74f",
        // duration: 10
      })


      gsap.timeline({
        scrollTrigger: {
          trigger: "#grid",
          start: "bottom-=50% top",
          end: "bottom+=90% bottom",
          // markers: true,
          scrub: true,
          // toggleActions:"restart pause reverse pause"
        }
      }).from('#graph', {

        display: "block",
        // opacity: 1,
        y: "-=50vh",
        // x: "2vw",
      }).to("#graph", {
        ease: "Power1.easeInOut",
        y: "+=120vh",
        clear: "all"
      })

      // gsap.to("#h2", {
      //   scrollTrigger: {
      //     trigger: "#h2",
      //     // scrub: true,
      //     start: "top top",
      //     end: "+=100%",
      //     markers: true,
      //     pin:"#h2",
      //     // toggleActions:"restart pause resume pause"
      //   },
      //   // y: '100vh',
      //   ease: "none",
      //   // zIndex: 0,
      //   // clearProps: "all"
      // })

      ScrollTrigger.create({
        trigger: "#h2",
        start: "center center",
        endTrigger: "#h2",
        end: "center+=100% center",
        // pin: "#h2",
        // markers: true
      })

      gsap.to('#graph', {
        scrollTrigger: {
          trigger: "#grid",
          end: "bottom+=200% bottom",
          start: "bottom+=100% bottom",
          // markers: true,
          // scrub: true,
          // pin: true,
          // toggleActions:"restart pause reverse pause"
        },
      })
      gsap.timeline({
        scrollTrigger: {
          trigger: "#grid",
          start: "bottom-=50%-=10px top",
          end: "bottom+=50%-=10px bottom",
          // markers: true,
          scrub: true,
          // toggleActions:"restart pause reverse pause"
        },
      })
        .from('.candle2, .tail', {
          stagger: {
            amount: 1,
            from: 'random',
            grid: 'auto',
          },
          css: {
            backgroundColor: "#100c0c",
          },
        })
      gsap.timeline({
        scrollTrigger: {
          trigger: "#grid",
          start: "bottom-=50%-=10px top",
          end: "bottom+=50%-=10px bottom",
          // markers: true,
          scrub: true,
          // toggleActions:"restart pause reverse pause"
        }
      }).to('.candle2', {
        stagger: {
          amount: 1,
          from: 'random',
          grid: 'auto',
        },
        // z:"-  100px",
        filter: "drop-shadow(0 0 10px rgba(221,169,79,1))"
      })
      // .to('.candle2', {
      //   css: { filter: "drop-shadow(#dda74f 0 0 0.3rem)" },
      // }, "<")
      // .fromTo('.candle2', { css: { backgroundColor: "#100c0c", filter: "drop-shadow(rgba(221,169,79,0) 0 0 0)" } }, { css: { filter: "drop-shadow(#dda74f 0 0 0.3rem)" } })


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
      <section className="bg-transparent relative z-20 flex text-white py-20 xl:px-60 lg:px-40 px-10 md:px-20">
        <div className="z-20 justify-center flex items-center align-middle">
          <div className=" z-20">
            <h1 id="h1" className="text-6xl sm:text-8xl relative text-A1 sm:font-thin font-bold text-center mb-10">Trading Bot Club</h1>
            <p id="p1" className=" sm:text-3xl mix-blend-difference z-20 relative text-lg sm:font-Metric-Thin font-Metric-Medium text-secondary mb-4">The Trading Bot Club is made in 2022-2023. We aim to make a functioning trading bot in a year with modest effeciency and ROI.</p>
            <p id='p2' className="sm:text-3xl mix-blend-difference relative z-20 text-lg sm:font-Metric-Thin font-Metric-Medium text-secondary mb-2">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vero placeat obcaecati perferendis dignissimos ratione eaque, impedit temporibus ea quasi alias repudiandae autem expedita facilis assumenda repellat, corporis facere animi possimus.</p>
            <div ref={gridElem} className="absolute z-10 translate-y-[40vh] left-0 w-screen ">
              <div id="grid" className={`flex w-[100v${window.innerWidth > window.innerHeight ? "w" : "h"}] flex-wrap -translate-y-10`}>
                {window.innerWidth > window.innerHeight ? [...Array(400)].map((e, i) => (
                  <div key={i} className={`w-[5vw] h-[5vw] flex justify-center grit overflow-y-visible`}>
                    <div className="grit2 z-10 w-full absolute h-full mx-auto"></div>
                  </div>)) : [...Array(300)].map((e, i) => (
                    <div key={i} className={`w-[10vw] h-[10vw] flex justify-center grit overflow-y-visible`}>
                      <div className="grit2 z-10 mx-auto absolute w-full h-full"></div>
                    </div>))}
              </div>
            </div>
          </div>
        </div>
      </section>
      <section style={{ height: gridHeight }} className={`text-white w-screen`}>
      </section>
      <section id="graph" className=" text-white w-screen">
        {/* <div style={{ width: `100v${window.innerWidth > window.innerHeight ? "w" : "h"}` }} className={`flex flex-wrap -translate-y-10`}> */}
        <div className={` w-[100v${window.innerWidth > window.innerHeight ? "w" : "h"}] flex flex-wrap relaive -translate-y-10`}>
          {window.innerWidth > window.innerHeight ? [...Array(20)].map((e, i) => (
            <div key={i} style={{ transform: `translateY(${Math.round(Math.random() * 40) + "vh"})` }} className={`w-[5vw] min-h-[5vw] candle overflow-y-visible relative flex justify-center items-center`}>
              <div style={{ height: Math.round(Math.random() * 30 + 1) + "vh" }} className={`candle2 flex justify-center items-center ${["bg-[#dda74f]", 'bg-[#a76b09]'][Math.round(Math.random())]} relative w-1/3 mx-auto `}>
                <div style={{ zIndex: -1, height: (Math.random() * 80 + 100) + "%" }} className="w-[2px] tail z-0 absolute mx-auto bg-secondary"></div>
              </div>
            </div>))
            : [...Array(10)].map((e, i) => (
              <div key={i} style={{ transform: `translateY(${Math.round(Math.random() * 30) + "vh"})` }} className={`w-[10vw] min-h-[10vh] justify-center candleoverflow-y-visible relative overflow-visible flex items-center`}>
                <div style={{ height: Math.round(Math.random() * 18 + 1) + "vh" }} className={`flex justify-center items-center ${["bg-[#dda74f]", 'bg-[#a76b09]'][Math.round(Math.random())]} relative candle2 w-1/3 mx-auto `}>
                  <div style={{ zIndex: -1, height: (Math.random() * 80 + 100) + "%" }} className="w-[2px] tail z-0 absolute mx-auto bg-secondary"></div>
                </div>
              </div>))}
        </div>
      </section>
      <div className="h-[20vh]"></div>
      <section className={` relative mix-blend-difference  text-white w-screen`}>
        <div id="h2" className="h-screen w-screen flex justify-center items-center">
          <h1 id="h2t" className="text-[6rem] text-white h-screen z-40 sm:text-[7rem] md:text-[10rem] lg:text-[14rem] xl:text-[16rem] 2xl:text-[17rem] tracking-tighter font-Metric-SemiBold font-extrabold">Be in <i>Ctrl</i></h1>
        </div>
      </section>
      <section className="h-[100vh]"></section>
    </div >
  )
}

export default IndexPage

export const Head = () => <title>TBC | Home</title>
