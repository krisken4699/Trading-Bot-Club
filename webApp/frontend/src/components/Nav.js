
import { Link } from "gatsby";
import styled from 'styled-components';
import React, { useRef, useState, useLayoutEffect, useEffect, useContext } from "react";
import Burger from './Burger';
import $ from 'jquery';
import isActive from './isActive';
import { useCookies } from 'react-cookie';
import ContextProvider, { useTopContext } from "./ContextProvider";

function Navbar() {
  const dropdownRef = useRef(null);
  const [cookies, setCookie, removeCookie] = useCookies(["user"]);
  const [shown, setShown] = useState(false);
  const [dark, setDark] = useState(false);
  const top = useTopContext()
  const toggleDropdown = () => {
    setShown((prev) => !prev);
    $(".burger").toggleClass('not-active');
    $(".burger").toggleClass('active');
  };
  useEffect(() => {
    if (window.location.href.replace("https://" + window.location.hostname, "").replace("http://" + window.location.hostname, "").replace(":8000", "") == '/OldIndex/') {
      setDark(top)
    }
    else {
      setDark(false)
    }
  }, [top])
  useLayoutEffect(() => {
    if (!dropdownRef.current)
      return;

    const el = dropdownRef.current;
    requestAnimationFrame(() => {
      if (shown) {
        // el.style.display = "block";
        el.style.transition = "max-height 0.5s"
        el.style.maxHeight = "220px";
      } else {
        // el.style.display = "none"
        el.style.transition = "max-height .5s"
        el.style.maxHeight = "0px";
      }
    })
  })
  return (
    <Nav className={`z-50 fixed px-10 hover:opacity-100 opacity-0 ${dark ? "bg-quaternary" : "bg-tertiary"} border-b transition-all duration-500`}>
      <div>
        <div className="grid lg:px-36 grid-cols-3 grid-rows-1 gap-x-0 ">
          <div className={`nav-collapse hidden lg:col-start-1 text- grid-rows-1 col-span-1 lg:grid grid-cols-3 gap-0 content-center text-center`}>
            <div className="a col-start-1 col-span-1 flex"><Link getProps={isActive} className={`self-center ${dark ? "text-secondary" : "text-primary"} text-center px-3 link`} to="/" href="#1">Home</Link></div>
            <div className="a col-start-2 col-span-1 flex"><Link getProps={isActive} className={`self-center ${dark ? "text-secondary" : "text-primary"} text-center px-3 link`} to="/dashboard/" href="#2">Dashboard</Link></div>
            <div className="a col-start-3 col-span-1 flex"><Link getProps={isActive} className={`self-center ${dark ? "text-secondary" : "text-primary"} text-center px-3 link`} to="/OldIndex/" href="#3">Old Landing</Link></div>
          </div>
          <div className='col-start2 col-span-1 flex items-center pl-[10%] justify-start lg:justify-center'>
            <Link to='/' className={`link lg:hidden inline text-primary  dark:text-white !font-A1 text-md align-baseline ${dark ? "text-accent3" : "text-primary"} font-semibold`}>TBC</Link>
            <Link to='/' className={`link hidden lg:inline dark:text-white text-primary !font-A1 text-md align-baseline ${dark ? "text-accent3" : "text-primary"} font-normal`}>Trading Bot Club</Link>
          </div>
          <div className="nav-collapse hidden lg:col-start-3 col-span-1 lg:grid grid-cols-1 gap-0 content-center text-center">
            <div className="col-start-3 flex">
              <a className={`self-center text-center px-3 font-Metric-Medium tracking-1px text-[0.8em] ${dark ? "text-secondary" : ""}  leading-5 not-italic tracking-[0.4px] font-light cursor-pointer uppercase text-333 hover:text-A29F9A font-500`}>{cookies.user ? "Logout" : "Sign in"}</a>
              {/* <button className="focus:outline-none text-black bg-F9C74F focus:ring rounded-xl text-xs py-2 px-4 self-center Poppins mr-2">Sign in</button>
              <button className="focus:outline-none text-gray-450 border-gray-350 border focus:ring rounded-xl text-xs py-2 px-4 self-center Poppins">Sign in</button> */}
            </div>
          </div>
          <div className="relative text-left col-start-11 flex">
            {/* <div className="flex self-center justify-self-auto"> */}
            {/* <button onClick={() => {
                toggleDropdown()
              }} type="button"
                className="
                  hidden self-center justify-self-auto min-w-8 p-2 h-full justify-center rounded-md 
                  border border-gray-300 shadow-sm bg-white text-sm font-medium text-gray-700 
                  hover:bg-gray-50 
                  focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500"
                id="options-menu" aria-expanded="true" aria-haspopup="true">
                </button> */}
            <Burger id="options-menu" className="lg:hidden absolute top-1/2 -translate-y-1/2 right-0 transform" style={{ maxHeight: "28px" }} onClick={() => { toggleDropdown() }} />
            {/* </div> */}
          </div>
          {/* rounded-md ring-1 shadow-lg ring-black ring-opacity-5 */}
          <div ref={dropdownRef} id="dropdown-menu" className="max-h-screen overflow-y-hidden lg:inline origin-top-right right-0 mt-0 w-56 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
            <div className="py-1" role="none">
              <Link getProps={isActive} onClick={toggleDropdown} href="#1" className={`link ${dark ? "text-secondary" : "text-primary"} block px-4 py-2`} role="menuitem" to="/">Home</Link>
              <Link getProps={isActive} onClick={toggleDropdown} href="#2" className={`link ${dark ? "text-secondary" : "text-primary"} block px-4 py-2`} role="menuitem" to="/dashboard/">Dashboard</Link>
              <Link getProps={isActive} onClick={toggleDropdown} href="#3" className={`link ${dark ? "text-secondary" : "text-primary"} block px-4 py-2`} role="menuitem" to="/OldIndex/">Old Landing</Link>
              <a className={`cursor-pointer self-center text-center py-2 px-4 font-Metric-Medium tracking-1px text-xs uppercase text-333 ${dark ? "text-secondary" : ""} hover:text-A29F9A font-500`}>{cookies.user ? "Logout" : "Sign in"}</a>
            </div>
          </div>

        </div>
      </div>
    </Nav>
  );
}

export default Navbar;

const Title = styled.h1`
  font-family: Poppins;
  font-size: 30px;
  font-style: bold;
  font-weight: 900;
  letter-spacing: 0em;
  text-align: left;
`;

const Nav = styled.nav`
  // background-color: rgba(247,247,247,1);
  // opacity:0;
  display: block;
  padding-top:18px;
  padding-bottom:18px;
  position:fixed;
  margin-left: auto;
  margin-right: auto;
  margin:auto;
  width:100vw;
  :hover{
    opacity:1;
    // background-color: rgba(234,233,231,0);
    // background-color: rgba(24,22,25);
    // background-color: rgba(234,233,231,.9);
  }
`;