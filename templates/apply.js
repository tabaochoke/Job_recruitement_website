var myButton = document.getElementById("apply_button");
            var myForm = document.getElementById("my-form");
            var myCloseButton = document.getElementById("my-close-button");
        
            myForm.style.display = "none";
        
            myButton.onclick = function() {
              myForm.style.display = "block";
            }
        
            myCloseButton.onclick = function() {
              myForm.style.display = "none";
            }
        
            window.onclick = function(event) {
              if (event.target == myForm) {
                myForm.style.display = "none";
              }
            }