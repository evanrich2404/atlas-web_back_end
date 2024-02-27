const Utils = {
  calculateNumber(type, a, b) {
    // Your previous calculateNumber function code here
    const roundA = Math.round(a);
    const roundB = Math.round(b);

    if (type === 'SUM') {
      return roundA + roundB;
    } else if (type === 'SUBTRACT') {
      return roundA - roundB;
    } else if (type === 'DIVIDE') {
      if (roundB === 0) return 'Error';
      return roundA / roundB;
    }
  }
};

module.exports = Utils;
