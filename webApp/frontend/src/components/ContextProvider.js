import React, { createContext, useState, useEffect, useContext } from 'react'
import $ from 'jquery'
import { globalHistory, useHistory } from '@reach/router'
const TopContext = createContext()

const ContextProvider = ({ location, children }) => {
    const [top, setTop] = useState(false);
    useEffect(() => {
        globalHistory.listen(() => {
            var scroll = $(window).scrollTop();
            if (scroll > window.innerHeight * 0.3) {
                // setTop(false)
                setTop(true)
            }
            else {
                // setTop(true)
                setTop(false)
            }
        })
    });
    useEffect(() => {
        $(window).scroll(() => {
            var scroll = $(window).scrollTop();
            // console.log(top)
            if (scroll > window.innerHeight * 0.3)
                setTop(true)
            else
                setTop(false)
        })
    });
    return (
        <TopContext.Provider value={top}>
            {children}
        </TopContext.Provider>
    )
}
export default ContextProvider
export function useTopContext() {
    return useContext(TopContext)
}