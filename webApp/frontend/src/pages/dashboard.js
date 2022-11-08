import gsap from "gsap"
import React, { useState, useEffect, useRef } from "react"
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const Dashboard = () => {
    const main = useRef(null)

    gsap.registerPlugin(ScrollTrigger)
    useEffect(() => {
        let ctx = gsap.context(() => {
            ScrollTrigger.create({
                trigger: "#test",
                start: 'top top',
                end: "+=100%",
                pin: '#test',
                // markers: true
            })

            return () => ctx.revert(); // cleanup
        }, main); // <- IMPORTANT! Scopes selector text

    }, []);

    return (
        <div ref={main} className="h-[200vh]">
            <div className="w-screen h-[100vh] bg-red-400">
            </div>
            <div className="w-screen h-[100vh] bg-green-500">
                <h1 className="text-5xl h-screen text-center" id="test">adno</h1>

            </div>
            <div className="w-screen h-[100vh] bg-blue-500">sfd</div>
        </div>
    )
}

export default Dashboard
