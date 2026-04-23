async function sendMessage() {
    let input = document.getElementById("userInput").value;

    if (input.trim() === "") {
        alert("Please enter a question");
        return;
    }

    document.getElementById("response").innerText = "Loading...";

    try {
        let res = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: input })
        });

        let data = await res.json();
        document.getElementById("response").innerText = data.reply;

    } catch (error) {
        document.getElementById("response").innerText = "Error connecting to server";
    }
}
