import { io } from "https://cdn.socket.io/4.8.1/socket.io.esm.min.js"
desc_box = document.getElementById("desc_box_txt")
gen_btn = document.getElementById("gen_btn")
style_op = document.getElementById("style_op")


gen_btn.addEventListener("click", () => {
    data_to_send = {
        desc: desc_box.value, 
        style: style_op.value
    }

    console.log(data_to_send)
    
    
})