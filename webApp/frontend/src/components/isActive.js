function isActive({ isCurrent }) {
  return isCurrent ? { style: { color: "#dda74f", fontWeight: "600", fontFamily: "Gothic A1" } } : { style: {color:'#0b0b0d',  fontWeight: "500", fontFamily: "Gothic A1" } }
}
export default isActive;