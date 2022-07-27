// Onclick of the button
document.querySelector("button").onclick = function () {  
    // Call python's random_python function
    length = document.getElementById("length").value
    console.log(length)
    eel.generate(length)(function(password){                        
      // Update the div with a random number returned by python
      document.querySelector(".output").innerHTML = password;
    })
  }
