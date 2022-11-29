#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log(1);
} else {
  let m = 1;
  for (let i = parseInt(process.argv[2]); i > 0; i--) {
    m = m * i;
  }
  console.log(m);
}
