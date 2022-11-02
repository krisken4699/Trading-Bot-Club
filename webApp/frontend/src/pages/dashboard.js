import React, { useState, useEffect, useRef } from "react"

const Dashboard = () => {



    return (
        <div style={{scrollSnapType:"y mandatory", msScrollSnapPointsY:"repeat(100vh)"}} className="h-[200vh] !overflow-y-scroll snap-y snap-always flex snap-mandatory">
            <div style={{scrollSnapAlign:"center", position:'relative'}} className="snap-start h-[100vh] bg-red-400">afds</div>
            <div style={{scrollSnapAlign:"center", position:'relative'}} className="snap-start h-[100vh] bg-green-500">sfd</div>
        </div>
    )
}

export default Dashboard
