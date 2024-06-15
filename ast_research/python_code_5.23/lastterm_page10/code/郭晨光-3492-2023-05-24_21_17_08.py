function findFirstNonRepeatChar(str) {
  if (!str) {
    return "None";
  }
  const charCount = new Map();
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    charCount.set(char, (charCount.get(char) || 0) + 1);
  }
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    if (charCount.get(char) === 1) {
      return char;
    }
  }
  return "None";
}

console.log(findFirstNonRepeatChar("helloworldhahaha!")); // 输出 e
console.log(findFirstNonRepeatChar("")); // 输出 None

