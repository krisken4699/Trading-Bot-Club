import React from 'react';
import $ from 'jquery';
import '../styles/Burger.css';
import { useRef } from 'react';

const Burger = ({ className, id, onClick }) => {
    const Ham = useRef(null);
    function Hamburger(e) {
        // console.log(Ham.current)
        // $(Ham.current).toggleClass('not-active');
        // $(Ham.current).toggleClass('active');
    }

    return (
        <div ref={Ham} onClick={()=>{Hamburger(); onClick()}} className={`burger btn not-active ${className}`} id={id}>
            <span></span>
            <span></span>
            <span></span>
        </div>
    );
}

export default Burger;
