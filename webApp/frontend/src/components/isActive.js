function isActive(data) {
  // const top = useTopContext()

  // useEffect(() => {
    // console.log(data)
  // }, []);
  // top ? '#a76b09' : '#0b0b0d',
  return data.isCurrent ? { style: { color: "#dda74f", fontWeight: "600", fontFamily: "Gothic A1" } } : { }
}
export default isActive;