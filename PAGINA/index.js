const express = require("express");
const app = express();
const port = 3000;

app.get("/api",(res,res) => {
    console.log("Get API");
    res.json({ id : "1234" , name: "Daniel"});
});

app.use("/",express.static("public"));
app.use(express.json());

