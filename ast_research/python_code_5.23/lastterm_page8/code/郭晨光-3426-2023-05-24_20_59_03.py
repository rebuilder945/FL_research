const f = x => {
  if (x < -10) {
    return -x - 1;
  } else if (x >= -10 && x < 0) {
    return x * x + 2 * x + 3;
  } else if (x >= 0 && x < 10) {
    return Math.sqrt(x);
  } else {
    return x - 1;
  }
}

const x = parseFloat(prompt("请输入x的值："));
const result = f(x).toFixed(2);
console.log(result);

