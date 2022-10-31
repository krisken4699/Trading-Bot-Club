import React, { createContext, useState, useEffect, useContext } from 'react'
import $ from 'jquery'
const TopContext = createContext()
const ContextProvider = ({ children }) => {
    const [top, setTop] = useState(false);
    useEffect(() => {
        $(window).scroll(() => {
            var scroll = $(window).scrollTop();
            // console.log(top)
            if (scroll > window.innerHeight * 0.3)
                setTop(true)
            else
                setTop(false)
        })
    })
    return (
        <TopContext.Provider value={top}>
            {children}
        </TopContext.Provider>
    )
}
export default ContextProvider
export function useTopContext(){
    return useContext(TopContext)
}