const express = require("express");
const cors = require("cors");
const proxy = require("express-http-proxy");

const app = express();

app.use(cors());
app.use(express.json());

app.use("/customer", proxy("http://3.81.56.56:8001"));
app.use("/shopping", proxy("http://54.146.248.186:8003"));
app.use("/", proxy("http://34.229.222.142:8002")); // products

app.listen(8000, () => {
  console.log("Gateway is Listening to Port 8000");
});
  