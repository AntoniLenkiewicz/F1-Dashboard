function TransformDate(date) {
  let d = new Date(date).toLocaleDateString("en-GB", {
    month: "long",
    day: "numeric",
  });
  return d;
}

export default TransformDate;