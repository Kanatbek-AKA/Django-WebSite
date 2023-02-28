"use strict";

// import { createReadStream } from "fs";
// const readstream = createReadStream(".../ path/to/video/file");
//
var fs = require("fs");
const { PathThrough } = require("stream");

const writestream = fs.createReadStream("../copy/save/here.mp4");
const readstream = fs.createReadStream(".../ path/to/video/file.mp4", {
  highWaterMark: 136232623, // it takes more memory just for difference
});

readstream.on("data", (chunk) => {
  const res = writestream.write(chunk);
  if (res) console.log("backpressure");
  readstream.pause();
});

readstream.on("data", (chunk) => {
  console.log("size", chunk.length);
});
readstream.on("end", () => {
  console.log("read stream finished");
});
readstream.on("error", (error) => {
  console.log("Error ", error);
});
readstream.stdin.on("data", (chunk) => {
  console.log("size", chunk.length);
});

readstream.pause(); // click Enter

readstream.on("data", (chunk) => {
  if (chunk.toString().trim() == "finish") readstream.resume();
  readstream.read();
});
// Save copy file
writestream.on("close", () => {
  process.stdout.write("file copied. Check the directory/folder");
});

// Read and write
const writestream2 = fs.createReadStream("../copy/save/here.txt");
fs.createReadStream.pipe(writestream2).on("error", console.error());
//
process.stdin.pipe(writestream);
//
//  transform stream
const report = new PathThrough(); // reads / writes
let total = 0;
report.on("data", (chunk) => {
  total += chunk.length;
  console.log("bytes", total);
});
readstream.pipe(report).pipe(writestream);
