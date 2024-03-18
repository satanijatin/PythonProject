document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // Here you can perform any validation or send the data to the server for authentication
    
    // For demonstration purposes, just logging the input values
    console.log("Username: " + username);
    console.log("Password: " + password);
  });